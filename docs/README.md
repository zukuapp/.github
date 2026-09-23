# ZUKU 개발자 문서

ZUKU의 공개 도구와 계약을 찾는 출발점입니다. 브라우저에서 읽으려면 [공식 개발자 사이트](https://zukuapp.github.io/docs/)를, GitHub에서 둘러보려면 [조직 프로필](../profile/README.md)을 이용하세요. 각 도구의 사용법과 형식 세부 사항은 해당 저장소의 문서를 기준으로 합니다.

## 어디서 시작할까요?

| 하려는 일 | 읽을 문서 |
| --- | --- |
| HTML5 게임 ZIP을 로컬에서 ZWF2로 컴파일하고 검사하기 | [시작하기](getting-started.md) |
| 공개 저장소 중 맞는 도구와 계약 찾기 | [저장소 지도](repository-map.md) |
| ZWF2와 이전 ZWF 바이너리 형식, 실행 경계 이해하기 | [공개 아키텍처](architecture.md) |
| Trecillo 로고와 문서 글꼴 원칙 확인하기 | [브랜드·타이포그래피](brand.md) |
| 버그 수정이나 문서 변경 제안하기 | [기여 안내](../CONTRIBUTING.md) |
| 취약점 제보 또는 사용 문의하기 | [보안 정책](../SECURITY.md) · [지원 안내](../SUPPORT.md) |

## 세 가지 출발점

1. **HTML5 게임 패키지** — [`zwf`](https://github.com/zukuapp/zwf)의 [ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md)와 로컬 컴파일러를 사용합니다. [5분 입문](getting-started.md#zwf2-패키지를-로컬에서-만들기)에서 샘플 파일을 만들어 볼 수 있습니다.
2. **Jump·API 계약** — [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)의 [매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json)와 [`zuku-api`](https://github.com/zukuapp/zuku-api)의 [OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)를 확인합니다. [`zuku-cli`](https://github.com/zukuapp/zuku-cli)는 아직 실제 생성·검증·패키징·업로드를 수행하지 않는 시제품입니다.
3. **ZUKBOX 저작·재생** — [`zukbox`](https://github.com/zukuapp/zukbox), [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime), [`zukbox-player`](https://github.com/zukuapp/zukbox-player)가 에디터·바이너리 파싱·렌더링을 나눠 맡습니다. 이 경로의 `.zwf`는 [ZWF2 HTML5 패키지](https://github.com/zukuapp/zwf/blob/main/SPEC.md)와 형식이 다릅니다.

> **문서 범위**  공개 저장소에서 확인할 수 있는 형식, 도구, 인터페이스를 설명합니다. 서비스의 배포 상태나 계정·API 이용 가능 여부는 저장소의 계약 문서만으로 확정하지 않습니다.

## 현재 상태를 읽는 법

| 상태 | 저장소 | 의미 |
| --- | --- | --- |
| 실행 가능 | [`zwf`](https://github.com/zukuapp/zwf) | 소스에서 설치해 로컬 ZIP을 컴파일·검사할 수 있음 |
| 계약·어댑터 | [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | 매니페스트 검증과 공개 어댑터·런타임 계약을 확인할 수 있음 |
| 계약 초안 | [`zuku-api`](https://github.com/zukuapp/zuku-api) | OpenAPI를 읽을 수 있으나 SDK 골격과 운영 API 제공은 구별해야 함 |
| 시제품 | [`zuku-cli`](https://github.com/zukuapp/zuku-cli) | 명령 이름은 있으나 실제 작업은 구현 전 |
