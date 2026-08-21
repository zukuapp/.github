<div align="center">

<img src="https://zukuapp.github.io/assets/zuku-mark.svg" alt="ZUKU" width="72">

# ZUKU

**Create what moves next.**

인터랙티브 UGC 미디어 플랫폼 — **Tresillo(트레실로)** 가 만듭니다.

[![Website](https://img.shields.io/badge/zukuapp.github.io-0a0a0f?style=flat-square&logo=github&logoColor=5CE1E6)](https://zukuapp.github.io/)
[![Service](https://img.shields.io/badge/zuzunza.com-0a0a0f?style=flat-square&logo=googlechrome&logoColor=5CE1E6)](https://zuzunza.com)

</div>

---

## 미디어 3종

보는 것에서 뛰어드는 것까지, 하나의 흐름으로 이어집니다.

| | 포맷 | 설명 |
|---|---|---|
| **01** | **Hype** | 인터랙티브 롱폼 · 가로형 영상 · 사진 |
| **02** | **Swipe** | 세로형 숏폼 영상 |
| **03** | **Jump** | 브라우저에서 바로 실행되는 WASM · HTML5 게임 |

## 기술 원칙

- **Unprivileged by design** — 인터랙티브 워크로드는 권한 없는 격리 경계 안에서만 실행됩니다.
- **Explicit contracts** — 서비스 의존성 · API 버전 · 스키마를 문서 계약으로 명시합니다.
- **Resource-aware** — CPU · 메모리 · PID · FD에 계약된 한도를 적용합니다.
- **Standards first** — WebAssembly, Rust, Next.js 등 표준 웹 기술 위에서 설계합니다.

> 보안 계약과 공개 표준은 투명하게 공개하고, 격리 핵심 구현은 사유 영역으로 보호합니다.

## 공개 저장소

| 저장소 | 설명 |
|---|---|
| [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | Next2D 기반 공개 Jump 엔진 및 패키지 계약 |
| [`zuku-cli`](https://github.com/zukuapp/zuku-cli) | Jump 프로젝트 검증 · 패키징 CLI |
| [`zuku-api`](https://github.com/zukuapp/zuku-api) | Jump API OpenAPI 3.1 계약 |
| [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io) | Tresillo × ZUKU 기업 사이트 |

## 스택

`Next.js` · `WebAssembly` · `Rust` · `PostgreSQL` · `Redis` · `nginx` · `Cloudflare`

---

<div align="center">

**Tresillo** · Seoul, Korea · [contact@zuzunza.com](mailto:contact@zuzunza.com)

© 2026 Tresillo. All rights reserved.

</div>
