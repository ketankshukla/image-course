# Original-artwork animation pilot

[Watch the pilot](https://course.ketanshukla.dev/presentations/original-artwork-pilot.html)

This separate 75-second pilot preserves the actual pixels of the original article hero image. The person, application window, toolbox, specialist robots, database, shield, labels and receipt come from clipped regions of that image. No generated replacements are used. Supporting request packets, callouts, permission indicators and travelling paths are code-drawn overlays.

The animation uses layer entrance, selective brightness, gentle lift, moving requests, a returning fact packet, a delegated task, an approval stop and a moving original receipt. Because the source is flattened, this is object-layer animation rather than new character poses or articulated robot movement. Some source background remains around the clipped layers.

## Voice and timing

HeyGen's Annie – Lifelike voice supplies 72.829 seconds of narration, followed by a short ending hold. The voice service's word timestamps guided the major scene boundaries: request at 6.5 seconds, MCP at 15.4, A2A at 25.5, policy at 37.5, evidence at 52.3. It is generated narration, not a human recording.

## Files and reproduction

- Original: `courses/Visual Course 01/diagrams/01-agent-architecture.png` (unchanged).
- Renderer: `scripts/render_artwork_pilot.mjs`.
- Delivered assets: `public/presentations/artwork-pilot/`.
- Player: `public/presentations/original-artwork-pilot.html`.

The renderer requires Node, Sharp and FFmpeg. Set `RUNTIME_NODE_MODULES` to the dependency directory containing Sharp, retain `narration.wav` in the output folder and run the renderer from the repository root. This rendering step is separate from the website's build. The website serves the completed H.264/AAC MP4 and does not call HeyGen or expose credentials.

The earlier slide video remains available. This pilot does not replace it, and no other article images have been modified.
