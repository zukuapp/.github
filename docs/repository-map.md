# 공개 저장소 지도

[한국어](repository-map.md) · [English](repository-map.en.md) · [정식 문서 / Developer docs](https://docs.zuzunza.com/)

공개 저장소 15개의 역할과 소유 계약입니다. 공개 소스, 로컬 검증, 릴리스와 운영 활성은 서로 다른 증거를 요구합니다. 비공개 서비스의 소스나 권한을 이 지도에서 공개하지 않습니다.

| Repository | 역할 | 기준 문서 |
| --- | --- | --- |
| [`zukujs-cli`](https://github.com/zukuapp/zukujs-cli) | 로컬 게임 개발 CLI·단일 Agent Core·Studio·Browser Adapter | [README.md](https://github.com/zukuapp/zukujs-cli/blob/main/README.md) |
| [`zuku-api`](https://github.com/zukuapp/zuku-api) | 공개 OpenAPI 계약·SDK 소스; 서버와 릴리스 상태는 별도 | [README.md](https://github.com/zukuapp/zuku-api/blob/main/README.md) |
| [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | Jump ZIP 검증·매니페스트·Next2D 어댑터 계약 | [README.md](https://github.com/zukuapp/zuku-engine-next2d/blob/main/README.md) |
| [`zwf`](https://github.com/zukuapp/zwf) | ZWF2 HTML5 패키지 컴파일·검사 | [SPEC.md](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime) | ZWF1 Rust 파서·ABI·WASM 런타임 | [README.md](https://github.com/zukuapp/zukbox-runtime/blob/main/README.md) |
| [`zukbox-player`](https://github.com/zukuapp/zukbox-player) | Next2D 플레이어 포크·브라우저 렌더러 | [DEVELOP.md](https://github.com/zukuapp/zukbox-player/blob/main/DEVELOP.md) |
| [`zukbox`](https://github.com/zukuapp/zukbox) | Next2D 에디터 포크·저장·내보내기 소스 | [README.md](https://github.com/zukuapp/zukbox/blob/main/README.md) |
| [`zukbox-lang`](https://github.com/zukuapp/zukbox-lang) | 에디터 UI 언어 리소스; 에디터 파일과 별도 확인 | [README.md](https://github.com/zukuapp/zukbox-lang/blob/main/README.md) |
| [`zukujs`](https://github.com/zukuapp/zukujs) | Next.js 상류 포크와 ZUKU 변환·제품 식별 정보 | [ZUKUJS.md](https://github.com/zukuapp/zukujs/blob/zukujs/v27.0.0/ZUKUJS.md) |
| [`zukujs-core`](https://github.com/zukuapp/zukujs-core) | ESM 명령 파서·제한된 진단 라이브러리; UNLICENSED·private 패키지 | [README.md](https://github.com/zukuapp/zukujs-core/blob/main/README.md) |
| [`zuku-agent-skills`](https://github.com/zukuapp/zuku-agent-skills) | 공개 API·게임 연동·접근성 스킬 | [README.md](https://github.com/zukuapp/zuku-agent-skills/blob/main/README.md) |
| [`zuku-developer-docs`](https://github.com/zukuapp/zuku-developer-docs) | 한국어·영어 MkDocs 정식 문서 소스 | [README.md](https://github.com/zukuapp/zuku-developer-docs/blob/main/README.md) |
| [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io) | 정적 개발자 허브·제품 소개 | [README.md](https://github.com/zukuapp/zukuapp.github.io/blob/main/README.md) |
| [`.github`](https://github.com/zukuapp/.github) | 조직 프로필·공통 기여·문서 지도 | [README.md](https://github.com/zukuapp/.github/blob/main/README.md) |
| [`shizuku`](https://github.com/zukuapp/shizuku) | 공개 아키텍처와 문서 인덱스; 운영 서버가 아님 | [README.md](https://github.com/zukuapp/shizuku/blob/main/README.md) |

`zuku`와 `zukujs`는 `zukujs-cli`의 같은 진입점을 사용합니다. `zukujs-core`의 명령 파서는 CLI 내부 Agent Core와 역할이 다릅니다. ZWF2 HTML5, ZUKBOX ZWF1과 Jump ZIP 매니페스트는 별도 형식이며 확장자만으로 호환을 판단하지 않습니다.

실제 기본 브랜치: `zukujs`는 `zukujs/v27.0.0`, 나머지 공개 저장소는 조사 시점의 `main`입니다. 설치 명령·지원 플랫폼·패키지 라이선스·테스트와 릴리스는 연결된 저장소의 현재 문서 및 산출물에서 확인하세요.

## ZUKBOX 저작·재생

에디터, ZWF1 런타임과 픽셀 렌더러는 위 표의 각 저장소가 소유합니다. 형제 디렉터리 배치와 내보내기·재생 검증은 각 README와 DEVELOP.md를 따릅니다.
