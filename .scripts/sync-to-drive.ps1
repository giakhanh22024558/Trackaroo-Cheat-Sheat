# File watcher that syncs local diagram files → Google Drive folder
# Auto-copies on save. Run on Windows startup via Task Scheduler.

$SourceFolder = 'C:\Users\Admin\Desktop\Trackagroo local management\diagrams'
$DestFolder = 'G:\.shortcut-targets-by-id\1fqaX3DE_KT88tT7ElgewcBM0bKzTvkZp\TRACKAROO 2026 RFT Phase 1\9 Docs\diagrams'
$LogFile = 'C:\Users\Admin\Desktop\Trackagroo local management\.scripts\sync.log'

# Ensure destination folder exists
if (-not (Test-Path $DestFolder)) {
    New-Item -ItemType Directory -Path $DestFolder -Force | Out-Null
}

function Write-Log {
    param([string]$msg)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$ts  $msg" | Tee-Object -FilePath $LogFile -Append
}

Write-Log "Watcher started. Source: $SourceFolder → Dest: $DestFolder"

# Initial full sync (mirror current state)
robocopy $SourceFolder $DestFolder /MIR /XF *.tmp *.bak /R:2 /W:3 /NJH /NJS /NDL /NC /NS | Out-Null
Write-Log "Initial mirror complete"

# Setup FileSystemWatcher
$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $SourceFolder
$watcher.Filter = '*.*'
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor `
                       [System.IO.NotifyFilters]::FileName -bor `
                       [System.IO.NotifyFilters]::DirectoryName

# Debounce: track last change time per file
$script:lastChange = @{}
$debounceMs = 500

$action = {
    $file = $Event.SourceEventArgs.FullPath
    $changeType = $Event.SourceEventArgs.ChangeType
    $now = (Get-Date).Ticks

    # Skip temp / backup / hidden files
    if ($file -match '\.(tmp|bak|swp|crdownload)$' -or $file -match '\\\.') { return }

    # Debounce — ignore if same file changed within debounceMs
    if ($script:lastChange.ContainsKey($file)) {
        $elapsed = ($now - $script:lastChange[$file]) / 10000  # ticks → ms
        if ($elapsed -lt $debounceMs) { return }
    }
    $script:lastChange[$file] = $now

    # Compute relative path → destination
    $relPath = $file.Substring($SourceFolder.Length).TrimStart('\')
    $destFile = Join-Path $DestFolder $relPath

    Start-Sleep -Milliseconds 300  # let writer finish

    try {
        if ($changeType -eq 'Deleted') {
            if (Test-Path $destFile) { Remove-Item $destFile -Force }
            Write-Log "DELETED: $relPath"
        } else {
            $destDir = Split-Path $destFile -Parent
            if (-not (Test-Path $destDir)) {
                New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            }
            Copy-Item -Path $file -Destination $destFile -Force
            Write-Log "$($changeType.ToString().ToUpper()): $relPath"
        }
    } catch {
        Write-Log "ERROR copying $relPath`: $_"
    }
}

Register-ObjectEvent $watcher 'Changed' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Created' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Deleted' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Renamed' -Action $action | Out-Null

Write-Log "Watcher armed. Monitoring..."

# Keep alive
try {
    while ($true) { Start-Sleep -Seconds 60 }
} finally {
    $watcher.Dispose()
    Write-Log "Watcher stopped"
}
