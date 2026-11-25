# NUNO — interactive headphone concept

Next.js 15 / React 19 / TypeScript / Tailwind / Three.js / R3F / Drei / GSAP / Motion / Lenis.

## Start
Use Node 22 LTS or a supported newer Node release.

```sh
npm install
npm run dev
```
Open http://localhost:3000. Run `npm run typecheck` and `npm run build` before deployment.

## Routes
Home `/`, products `/products`, individual product `/products/nuno-one` and `/products/nuno-studio`, configurator `/experience`, technology `/technology`, story `/about`, contact `/contact`, cart `/cart`, checkout `/checkout`.

## Model
`public/models/nuno.glb` is an original procedural concept asset with 18 individually named meshes and material assignments. Mesh positions are stored in `Scene.tsx` and explosion offsets are derived from mesh names. The scroll position is the source of truth for explosion and reassembly. The configurator uses orbit controls, a finish picker and component inspection buttons. To regenerate the asset, install Python numpy and trimesh and run `python scripts/generate_model.py`.

## Customize
Edit `data/products.ts` for the catalog, illustrative prices, finishes and verified technical information when available. Replace the GLB with a manufacturer-approved asset preserving node names or update the offset mapping. The two demo editions currently share the same model. The visual brand direction (warm white, charcoal, lime accent) is a design proposal, not official brand guidelines.

## Demo limitations
No official product dimensions, specifications, photography, reviews or offers were supplied. The model is a stylized 3D concept, not a manufacturer CAD model. Prices are illustrative USD amounts. No payment gateway, server-side order system, stock management or email delivery is connected. Inquiry storage is local to the browser; checkout simulates an order without collecting shipping or payment details. Do not use this as a live store before replacing these integrations. The hero has scroll-controlled camera zoom and rotation, while individual interactive hotspots are in the configurator; full per-component camera choreography is not implemented. Device performance and browser compatibility have not been measured. Dependency installation could not be completed in the build environment because the npm cache was unavailable, so the project has not been compiled or browser-tested.
