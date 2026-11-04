# Embedded SME visualizations: build notes

The Learning Path at `content/learning-paths/cross-platform/explore-sme-visualisations/` embeds a static build of [Scalable Visualisations](https://github.com/Arm-Debug/visualising-sme). The checked-in bundle is under `static/apps/sme-visualisations/` and was built from commit `b0f79ae1a309e4cd0a8ae8ea4a70b93e591a3a04`.

The upstream React app assumes that it owns the site root. For this static snapshot, the build used a temporary copy of the source with two changes:

1. `createBrowserRouter` became `createHashRouter` in `src/index.tsx`. This keeps all app routes under one static `index.html` URL without requiring a server fallback.
2. The home page's `/matrix-chip.png` reference became `process.env.PUBLIC_URL + "/matrix-chip.png"` so the image resolves below `/apps/sme-visualisations/`.

The build used the upstream `npm run build` command with `PUBLIC_URL=/apps/sme-visualisations`, `DISABLE_ESLINT_PLUGIN=true`, and the upstream repository's installed dependencies. Source maps and the upstream `robots.txt` were omitted from the copied bundle. The Lato font license was copied from `src/fonts/OFL.txt`. The app source itself was not changed.

To refresh the snapshot, apply those two source changes in a temporary copy, build with the same public URL, and replace the files under `static/apps/sme-visualisations/`. Check both embedded routes and their full-tab links after rebuilding.

The upstream repository has no root license file. Confirm redistribution terms before publishing this bundled copy beyond the experiment.
