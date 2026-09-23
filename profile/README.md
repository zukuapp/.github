<p align="center">
  <a href="https://zukuapp.github.io/docs/"><img src="assets/developer-hero.png" alt="Trecillo · ZUKU 개발자 문서 — 공개 명세에서 첫 실행까지" width="960"></a>
</p>

<p align="center">
  <a href="https://zukuapp.github.io/docs/">공식 개발 문서</a> ·
  <a href="../docs/getting-started.md">시작하기</a> ·
  <a href="../docs/repository-map.md">저장소 지도</a> ·
  <a href="../docs/architecture.md">공개 아키텍처</a> ·
  <a href="../CONTRIBUTING.md">기여 안내</a>
</p>

# ZUKU 개발자 허브

**ZUKU(즈쿠)** 는 **Trecillo(트레실로)** 가 만드는 창작 미디어 플랫폼입니다. [공식 개발자 사이트](https://zukuapp.github.io/)와 이 조직 홈은 ZUKU의 **공개 개발 도구, 파일 형식, API 계약**을 찾는 출발점입니다. 저장소별 최신 사용법은 각 저장소의 README와 명세를 기준으로 합니다.

## 어디서 시작하나요?

| 하고 싶은 일 | 바로 갈 곳 |
| --- | --- |
| HTML5 게임을 ZWF2 패키지로 만들어 로컬에서 검사하기 | [5분 입문](../docs/getting-started.md) · [`zwf` 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| Jump 게임의 패키지 필드와 실행 계약 확인하기 | [Jump 매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) · [런타임 계약](https://github.com/zukuapp/zuku-engine-next2d/blob/main/contracts/jump-runtime.contract.json) |
| 실제 서비스 API 연동하기 | [ZUKU API 가이드](https://docs.zuzunza.com/) |
| 공개 API 설계 초안 살펴보기 | [`zuku-api` OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |
| 에디터·플레이어·언어 도구의 역할 찾기 | [공개 저장소 지도](../docs/repository-map.md) |
| 버그 수정이나 문서 개선 제안하기 | [기여 안내](../CONTRIBUTING.md) · [지원 안내](../SUPPORT.md) |

> 공개 명세는 구현 계약을 설명합니다. 서비스 계정, 배포 상태, API 접근 권한을 보증하지는 않습니다. 설치 명령과 지원 범위는 각 저장소에서 확인해 주세요.

## 공개 개발 경로

| 경로 | 저장소 | 먼저 읽을 계약 |
| --- | --- | --- |
| **HTML5 패키지** | [`zwf`](https://github.com/zukuapp/zwf) | [ZWF2 파일 형식과 플레이어 경계](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| **Jump 게임 계약** | [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | [매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) · [런타임 계약](https://github.com/zukuapp/zuku-engine-next2d/blob/main/contracts/jump-runtime.contract.json) |
| **플랫폼 API 계약** | [`zuku-api`](https://github.com/zukuapp/zuku-api) | [OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |
| **서비스 API 사용법** | [ZUKU API 가이드](https://docs.zuzunza.com/) | [인증·콘텐츠·게임 클라우드 문서](https://docs.zuzunza.com/) |
| **ZUKBOX 저작·재생** | [`zukbox`](https://github.com/zukuapp/zukbox) · [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime) · [`zukbox-player`](https://github.com/zukuapp/zukbox-player) · [`zukbox-lang`](https://github.com/zukuapp/zukbox-lang) | [저장소 지도와 형식 구분](../docs/repository-map.md#zukbox-저작재생) |

`zwf`의 **ZWF2 HTML5 패키지**와 ZUKBOX 런타임의 **이전 ZWF1 바이너리**는 확장자가 같아도 형식이 다릅니다. [공개 아키텍처](../docs/architecture.md)에서 경계를 먼저 확인해 주세요.

`zuku-cli`는 명령 이름만 갖춘 **시제품**으로, 현재 생성·검증·패키징·업로드 작업을 수행하지 않습니다. 공개 `zuku-api` 명세 역시 운영 API나 SDK 배포를 뜻하지 않습니다. 실제 서비스 연동은 [API 가이드](https://docs.zuzunza.com/)를 확인하세요. [저장소별 상태](https://zukuapp.github.io/docs/#repositories)도 함께 읽어 주세요.

## 문서와 기여

- [공식 개발 문서](https://zukuapp.github.io/docs/) · [GitHub 문서 목차](../docs/README.md) — 입문, 저장소 상태, 공개 아키텍처, 브랜드 원칙
- [기여 안내](../CONTRIBUTING.md) — 변경 제안과 검증 결과 작성
- [보안 정책](../SECURITY.md) — 취약점 비공개 신고
- [지원 안내](../SUPPORT.md) — 기술·서비스 문의 경로

<p align="center">
  <a href="https://trecillo.crevision.kr">Trecillo</a> ·
  <a href="https://github.com/zukuapp">GitHub</a> ·
  <a href="https://zuzunza.com">ZUKU</a> ·
  <a href="mailto:contact@crevision.kr">문의</a>
</p>
