# Mapbox SDK — Research Notes

**Status:** Working notes · external research · not authoritative spec
**Why this file exists:** Trackaroo Phase 1 leans on Mapbox in two places (mobile NAV runtime + backend TrackIQ ingest), so we need a shared baseline of *what the SDK actually does*, *how it works under the hood*, and *how it compares to Google Maps*. Use this when deciding what to call out in spec, vendor briefs, or RFT responses.

**Related project artifacts:**
- `../diagrams/1-overview/trackaroo-phase1-architecture.md` — see `MOB-2001` (Offline Navigation Engine), `EXT-9001a` (Basemap), `EXT-9001b` (Track Data Feeds)
- `../diagrams/2-subsystems/mob-survival-core.md` — NAV + Map Bundle Download Manager deep-dive
- `../diagrams/3-flows/data-flow/dfd-survival-core.md` — pre-journey download flow
- `../diagrams/3-flows/data-flow/dfd-trackiq-pipeline.md` — `CBE-5001` (Ingestion Adapter)
- `../diagrams/4-cross-cutting/tile-lifecycle.md` — full tile journey Mapbox → Bundle → NAV cache

---

## 1. What the Mapbox SDK actually is

A collection of code libraries developers embed into mobile apps, web apps, and automotive systems to render **highly customizable, interactive maps** and **turn-by-turn navigation**.

Instead of writing a 3D graphic rendering engine and a geospatial data decoder from scratch, you drop the Mapbox SDK into your codebase. It handles:
- Talking to map hardware (GPU)
- Downloading + decoding geospatial data
- Rendering map tiles in real-time

So the app team can focus on UX and business logic rather than reinventing cartography.

---

## 2. How it works under the hood

Two industry-standard concepts deliver Mapbox's performance:

### 2.1 Vector Tiles (vs. raster tiles)

| Approach | What gets downloaded | Trade-off |
|---|---|---|
| **Raster tiles** (older Google Maps style) | PNG image squares stitched together | Heavy bandwidth, pixelated when zoomed, can't restyle on-device |
| **Vector tiles** (Mapbox approach) | Raw geometric instructions — points, lines, polygons, mathematical attributes | Lightweight, infinitely zoomable, restylable at runtime |

### 2.2 Client-side rendering

Because data arrives as raw geometry (math, not pixels), the SDK uses the device's GPU to draw the map *live*:

| Platform | Graphics API |
|---|---|
| iOS | Metal |
| Android | OpenGL / Vulkan |
| Web | WebGL |

This is what enables runtime styling, smooth zoom/pan, and 3D terrain — the GPU is doing the work, not a remote tile server.

---

## 3. Key capabilities of the SDK

| Capability | What it means |
|---|---|
| **Dynamic 3D terrain & landmarks** | Native support for high-resolution **Digital Elevation Models (DEM)** — render realistic 3D mountains, valleys, contour lines, architectural landmarks with dynamic shadows and lighting |
| **Runtime styling** | Because the map is drawn live on-device, you can alter appearance on the fly — hide specific roads, change forest color based on weather data, swap UI per user preference, etc. |
| **Offline maps (Ambient Caching & Tile Stores)** | Programmatically pre-download full regional map bundles. App stays fully functional (detailed maps + routes) when disconnected from cellular |
| **Advanced routing & navigation** (Navigation SDK) | Turn-by-turn voice guidance · lane-level assistance (3D lane visuals for highway exits) · automatic off-route recalculation · predictive location tracking for long tunnels / canyons where GPS drops out |

---

## 4. Mapbox SDK vs. Google Maps SDK

| Feature | Mapbox SDK | Google Maps SDK |
|---|---|---|
| **Design flexibility** | **Total control.** Every layer, color, font can be customized down to raw data level via Mapbox Studio | **Restricted.** Custom color themes possible, but generally locked into Google's baseline look + map data |
| **Data ingestion** | **Highly agnostic.** Upload custom GeoJSON, Shapefiles, custom vector attributes directly into custom map styles | Harder to overlay custom global datasets — primarily designed around Google's proprietary Places POIs |
| **Offline engine** | **Excellent native support** for managing large custom local vector tile packages (TileStore) | Limited offline bounding-box downloads, mostly black-box background caching managed by Google |
| **Pricing model** | Generous **free tier based on Monthly Active Users (MAU)**, then pay-as-you-go | Charged per thousands of map loads / API hits |

---

## 5. Why this matters for Trackaroo Phase 1

Cross-references to the architecture so it's obvious *where* Mapbox shows up in the system:

### 5.1 On-device — Offline Navigation Engine (`MOB-2001`)
- Uses Mapbox SDK at runtime to render the basemap and run local search + routing.
- Relies on **vector tiles + offline tile store** capability — without these, the "100% offline-first · zero network" Survival Core constraint wouldn't be feasible with a third-party map provider.
- Relies on **client-side GPU rendering** — no network round-trip per map redraw.

### 5.2 External data source — Basemap (`EXT-9001a`)
- Mapbox is the vector basemap provider — pulled **once during pre-journey download**, never at runtime.
- Trackaroo holds the API keys (not the vendor).

### 5.3 External data source — Track Data Feeds (`EXT-9001b`)
- Spec lists **Mapbox / OSM vector tiles** as a primary source for `CBE-5001 Ingestion Adapter`.
- This is the *backend* ingest path — separate from the mobile runtime usage above. Same SDK family, different deployment surface.

### 5.4 Capabilities we explicitly rely on

| Mapbox capability | Where Trackaroo depends on it |
|---|---|
| Offline regional bundles (TileStore) | `MOB-2001` NAV — entire Survival Core offline mandate hinges on this |
| Vector tiles (not raster) | Both NAV runtime *and* TrackIQ ingestion adapter |
| DEM support | `CBE-5002 DEM Enrichment Engine` — although Trackaroo uses AWS Terrain Tiles / SRTM (`EXT-9002`) as the DEM source, not Mapbox's bundled DEM |
| Custom styling | Lets us blend Mapbox basemap with Trackaroo-licensed track data + authority hazard overlays without recompiling |

### 5.5 Capabilities we explicitly do **not** use (Phase 1)

- **Mapbox Navigation SDK turn-by-turn voice guidance** — Trackaroo NAV does routing locally; voice guidance is out of Phase 1 scope.
- **Runtime restyling based on weather/external data** — Survival Core is deterministic, no adaptive map appearance.
- **Cloud rerouting** — explicitly prohibited per `RT-09` compliance constraint.

---

## 6. Open questions / things to verify with vendor

- [ ] Exact Mapbox SDK pricing tier we'll fall into (MAU-based) once Phase 1 user base is projected.
- [ ] Whether the vendor will use the **Mapbox Maps SDK** alone or the **Mapbox Navigation SDK** add-on (we likely only need Maps SDK + custom routing logic).
- [ ] Tile bundle size estimates for typical Australian regional downloads (impacts on-device storage budget + pre-journey download UX).
- [ ] Whether Mapbox's offline tile expiration policy (default ~12 months) conflicts with our "pre-journey download only" model.
- [ ] License terms for redistributing Mapbox vector tiles inside our regional bundles vs. requiring per-device download.

---

## 7. Sources

Notes compiled from general developer documentation and comparative reviews encountered during research (not a single source — synthesis). Treat as **working knowledge**, verify any specific claim against the official Mapbox docs (https://docs.mapbox.com/) before quoting in vendor briefs or RFT submissions.
