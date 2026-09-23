# 공개 저장소 지도

하나의 이름이나 `.zwf` 확장자가 모든 도구의 입력 형식을 뜻하지는 않습니다. 작업 대상에 맞는 **계약 문서**를 먼저 찾으세요.

## 게임 패키지와 공개 인터페이스

| 저장소 | 역할 | 먼저 읽을 곳 |
| --- | --- | --- |
| [`zwf`](https://github.com/zukuapp/zwf) | HTML5 ZIP을 ZWF2로 컴파일·검사 | [README](https://github.com/zukuapp/zwf/blob/main/README.md) · [ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | Jump 매니페스트 검증기, Next2D 어댑터와 런타임 계약. 호스트 샌드박스는 포함하지 않음 | [README](https://github.com/zukuapp/zuku-engine-next2d/blob/main/README.md) · [매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) |
| [`zuku-cli`](https://github.com/zukuapp/zuku-cli) | **시제품**. create/validate/package/upload 명령은 실제 작업 없이 성공 문구를 출력함 | [현재 상태](https://github.com/zukuapp/zuku-cli/blob/main/README.md) |
| [`zuku-api`](https://github.com/zukuapp/zuku-api) | OpenAPI 3.1 계약과 SDK 소스 골격. 운영 서비스·npm 배포 여부는 별도 | [OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |

`zwf`의 ZWF2 매니페스트와 `zuku-engine-next2d`의 Jump 매니페스트는 별도 문서입니다. 한쪽 필드를 다른 쪽에 그대로 적용하지 마세요. 공개 계약을 실제 서비스 가용성이나 CLI 기능 완료로 해석하지 마세요.

## ZUKBOX 저작·재생

| 저장소 | 역할 | 먼저 읽을 곳 |
| --- | --- | --- |
| [`zukbox`](https://github.com/zukuapp/zukbox) | 브라우저 기반 저작 도구 | [README](https://github.com/zukuapp/zukbox/blob/main/README.md) |
| [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime) | 이전 `ZWF1` 형식의 파싱·타임라인 평가를 맡는 WebAssembly 코어 | [README](https://github.com/zukuapp/zukbox-runtime/blob/main/README.md) · [형식 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md) |
| [`zukbox-player`](https://github.com/zukuapp/zukbox-player) | Next2D 렌더링 플레이어 | [README](https://github.com/zukuapp/zukbox-player/blob/main/README.md) · [개발 가이드](https://github.com/zukuapp/zukbox-player/blob/main/DEVELOP.md) |
| [`zukbox-lang`](https://github.com/zukuapp/zukbox-lang) | 에디터 언어 리소스 | [저장소](https://github.com/zukuapp/zukbox-lang) |

`zukbox-runtime`의 명세는 **v0.1 초안**입니다. 이 런타임은 렌더 큐를 만들고 픽셀 렌더링은 `zukbox-player`가 담당합니다. 두 저장소의 현재 역할과 진행 상태는 각 README에서 확인하세요.

## 조직과 문서

| 저장소 | 역할 |
| --- | --- |
| [`shizuku`](https://github.com/zukuapp/shizuku) | 공개 플랫폼 소개와 문서 인덱스 |
| [`zukuapp.github.io`](https://github.com/zukuapp/zukuapp.github.io) | [공식 개발 문서 사이트](https://zukuapp.github.io/docs/)와 제품 소개 페이지의 소스 |
| [`.github`](https://github.com/zukuapp/.github) | [조직 프로필](../profile/README.md), 이 개발자 문서와 공통 기여 안내 |

저장소별 코드·형식·테스트 절차는 해당 저장소가 소유합니다. 이 지도의 링크가 오래되었거나 설명이 어긋나면 [문서 변경을 제안](../CONTRIBUTING.md)해 주세요.
