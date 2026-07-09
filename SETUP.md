# Generating & maintaining the FlyPix Python SDK

This repo produces the public `flypix` Python SDK from the FlyPix OpenAPI spec
using [Speakeasy](https://www.speakeasy.com). The generated SDK is committed to
the repo; we never hand-edit it. All customization happens in the **inputs**:

| File | Purpose | Hand-edited? |
| --- | --- | --- |
| `.speakeasy/workflow.yaml` | Wires the live spec + overlay → Python target | Yes (rarely) |
| `.speakeasy/gen.yaml` | Package name, SDK class name, generation options | Yes |
| `openapi/overlay.yaml` | Polish layer: adds `servers`, clean method names | **Yes — this is the quality lever** |
| `openapi/flypix.openapi.yaml` | Resolved+overlaid spec (generated) | No |
| `src/flypix/**` | The generated SDK | **Never** |

The upstream spec (`https://api.flypix.ai/openapi.json`) is a FastAPI export, so
its `operationId`s are machine names like
`get_file_download_link_files__file_id__download_get`. The overlay rewrites all
52 of them to clean, tag-scoped names (`client.files.get_download_link(...)`) and
adds the missing production server URL — without editing the upstream spec.

## One-time setup

1. **Install the CLI**

   ```sh
   brew install speakeasy-api/homebrew-tap/speakeasy
   # or: curl -fsSL https://go.speakeasy.com/cli-install.sh | sh
   ```

2. **Authenticate** (creates/links a free Speakeasy account — free tier covers a
   single published SDK):

   ```sh
   speakeasy auth login
   ```

3. **Generate the SDK for the first time.** The workflow + overlay are already
   committed, so this reads them and generates into the repo:

   ```sh
   speakeasy run
   ```

   If you'd rather answer the interactive prompts (and let the CLI finalize
   `gen.yaml`), run `speakeasy quickstart` instead — accept package name
   `flypix` and SDK class name `FlyPix`.

4. **Wire up CI secrets.** In GitHub → repo Settings → Secrets and variables →
   Actions, add:
   - `SPEAKEASY_API_KEY` — from `speakeasy auth` / the Speakeasy dashboard.
   - `PYPI_TOKEN` — a PyPI API token scoped to the `flypix` project.

5. **(Optional) Let the CLI generate canonical CI workflows** pinned to your
   installed version — this refreshes the starters in `.github/workflows/`:

   ```sh
   speakeasy configure github
   ```

## Day-to-day

- **The API changed** → the scheduled `Generate SDK` workflow re-fetches the
  spec, re-applies the overlay, and opens a PR with the diff. You can also run
  it on demand from the Actions tab, or locally with `speakeasy run`.
- **A method name reads poorly** → edit `openapi/overlay.yaml`, run
  `speakeasy run`, review the diff. Never edit `src/flypix/`.
- **Publish** → merging a generation PR to `main` triggers `Publish SDK`, which
  releases to PyPI.

## Why this layout

- **Generated code is committed** — reviewers and IDEs see real code; PRs show
  exactly how a spec change reshapes the SDK.
- **Overlay, not spec edits** — upstream stays the source of truth; our polish
  is a reviewable, re-appliable patch.
- **Pinned generator version** (`.speakeasy/workflow.yaml`) — reproducible
  output across local and CI runs.
