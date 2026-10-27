# Public repository map

[한국어](repository-map.md) · [English](repository-map.en.md) · [정식 문서 / Developer docs](https://docs.zuzunza.com/)

These are the 15 public repositories and their owned contracts.

| Repository | Role | Owned documentation |
| --- | --- | --- |
| [`zukujs-cli`](https://github.com/zukuapp/zukujs-cli) | Local game CLI, shared Agent Core, Studio, and Browser Adapter | [README.md](https://github.com/zukuapp/zukujs-cli/blob/main/README.md) |
| [`zuku-api`](https://github.com/zukuapp/zuku-api) | Public OpenAPI draft and SDK source (live API: [ZUKU API guide](https://docs.zuzunza.com/en/)) | [README.md](https://github.com/zukuapp/zuku-api/blob/main/README.md) |
| [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | Jump ZIP validation, manifest, and Next2D adapter contracts | [README.md](https://github.com/zukuapp/zuku-engine-next2d/blob/main/README.md) |
| [`zwf`](https://github.com/zukuapp/zwf) | Compile and inspect ZWF2 HTML5 packages | [SPEC.md](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime) | ZWF1 Rust parser, ABI, and WASM runtime | [README.md](https://github.com/zukuapp/zukbox-runtime/blob/main/README.md) |
| [`zukbox-player`](https://github.com/zukuapp/zukbox-player) | Next2D player fork and browser renderers | [DEVELOP.md](https://github.com/zukuapp/zukbox-player/blob/main/DEVELOP.md) |
| [`zukbox`](https://github.com/zukuapp/zukbox) | Next2D editor fork, save, and export source | [README.md](https://github.com/zukuapp/zukbox/blob/main/README.md) |
| [`zukbox-lang`](https://github.com/zukuapp/zukbox-lang) | Editor locale resources | [README.md](https://github.com/zukuapp/zukbox-lang/blob/main/README.md) |
| [`zukujs`](https://github.com/zukuapp/zukujs) | Next.js upstream fork and ZUKU distribution identity | [ZUKUJS.md](https://github.com/zukuapp/zukujs/blob/zukujs/v27.0.0/ZUKUJS.md) |
| [`zukujs-core`](https://github.com/zukuapp/zukujs-core) | ESM command parser and bounded diagnostics; UNLICENSED private package | [README.md](https://github.com/zukuapp/zukujs-core/blob/main/README.md) |
| [`zuku-agent-skills`](https://github.com/zukuapp/zuku-agent-skills) | Public API, game integration, and accessibility skills | [README.md](https://github.com/zukuapp/zuku-agent-skills/blob/main/README.md) |
| [`zuku-developer-docs`](https://github.com/zukuapp/zuku-developer-docs) | Korean and English MkDocs developer documentation | [README.md](https://github.com/zukuapp/zuku-developer-docs/blob/main/README.md) |
| [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io) | Static developer hub and product introduction | [README.md](https://github.com/zukuapp/zukuapp.github.io/blob/main/README.md) |
| [`.github`](https://github.com/zukuapp/.github) | Organization profile, contribution guidance, and repository map | [README.md](https://github.com/zukuapp/.github/blob/main/README.md) |
| [`shizuku`](https://github.com/zukuapp/shizuku) | Public architecture and documentation index | [README.md](https://github.com/zukuapp/shizuku/blob/main/README.md) |

`zuku` and `zukujs` share the `zukujs-cli` entry point.

The default branch is `zukujs/v27.0.0` for `zukujs` and `main` for the other repositories.

## ZUKBOX authoring and playback

When building the editor (`zukbox`), ZWF1 runtime (`zukbox-runtime`), and renderer (`zukbox-player`) together, follow their README and DEVELOP.md for sibling checkout layout and export/playback verification.
