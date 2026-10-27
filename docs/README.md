<!-- BEGIN ZUKU OFFICIAL BRAND -->
<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://docs.zuzunza.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)"
        srcset="../docs/branding/zuku-logo-dark.png">
      <img src="../docs/branding/zuku-logo-light.png"
        alt="ZUKU" width="320">
    </picture>
  </a>
</p>
<p align="center">ZUKU - 내가 불러 일으키는 새로운 창작.</p>
<!-- markdownlint-enable MD033 MD041 -->
<!-- END ZUKU OFFICIAL BRAND -->

# ZUKU 개발자 문서

이 문서는 ZUKU의 공개 도구와 계약 문서 목차입니다. 같은 안내를 브라우저에서는 [공식 개발자 사이트](https://zukuapp.github.io/docs/)로, GitHub에서는 [조직 프로필](../profile/README.md)로 제공합니다. 각 도구의 사용법과 형식 세부 사항은 해당 저장소의 문서를 기준으로 합니다.

## 작업별 문서

| 하려는 일 | 읽을 문서 |
| --- | --- |
| HTML5 게임 ZIP을 로컬에서 ZWF2로 컴파일하고 검사하기 | [시작하기](getting-started.md) |
| 공개 저장소 중 맞는 도구와 계약 찾기 | [저장소 지도](repository-map.md) |
| 실제 ZUKU 서비스 API 연동하기 | [ZUKU API 가이드](https://docs.zuzunza.com/) |
| ZWF2와 이전 ZWF 바이너리 형식, 실행 경계 이해하기 | [공개 아키텍처](architecture.md) |
| ZUKU 공식 로고와 문서 글꼴 원칙 확인하기 | [브랜드·타이포그래피](brand.md) |
| 버그 수정이나 문서 변경 제안하기 | [기여 안내](../CONTRIBUTING.md) |
| 취약점 제보 또는 사용 문의하기 | [보안 정책](../SECURITY.md) · [지원 안내](../SUPPORT.md) |

## 세 가지 출발점

1. HTML5 게임 패키지 — [`zwf`](https://github.com/zukuapp/zwf)의 [ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md)와 로컬 컴파일러를 사용합니다. [입문 절차](getting-started.md#zwf2-패키지를-로컬에서-만들기)는 샘플 파일로 패키지를 만듭니다.
2. Jump·API 계약 — [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)의 [매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json)와 [`zuku-api`](https://github.com/zukuapp/zuku-api)의 [OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)를 기준으로 합니다. CLI 소스 명령과 릴리스별 검증 범위는 [`zukujs-cli`](https://github.com/zukuapp/zukujs-cli)에 있습니다.
3. ZUKBOX 저작·재생 — [`zukbox`](https://github.com/zukuapp/zukbox), [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime), [`zukbox-player`](https://github.com/zukuapp/zukbox-player)가 에디터·바이너리 파싱·렌더링을 나눠 맡습니다. 이 경로의 `.zwf`는 [ZWF2 HTML5 패키지](https://github.com/zukuapp/zwf/blob/main/SPEC.md)와 형식이 다릅니다.

> 문서 범위: 이 저장소는 공개 도구와 계약을 설명합니다. 실제 서비스 API 연동은 [ZUKU API 가이드](https://docs.zuzunza.com/)와 사용 중인 릴리스의 응답을 기준으로 합니다. 공개 `zuku-api` OpenAPI·SDK 초안은 별도 프로젝트입니다.

## 저장소 상태

| 상태 | 저장소 | 의미 |
| --- | --- | --- |
| 실행 가능 | [`zwf`](https://github.com/zukuapp/zwf) | 소스에서 설치해 로컬 ZIP을 컴파일·검사함 |
| 계약·어댑터 | [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d) | 매니페스트 검증과 공개 어댑터·런타임 계약을 제공함 |
| 계약 초안 | [`zuku-api`](https://github.com/zukuapp/zuku-api) | OpenAPI 초안을 제공함; SDK 골격과 운영 API 제공은 별개 |
| 소스 구현·릴리스별 검증 | [`zukujs-cli`](https://github.com/zukuapp/zukujs-cli) | 두 별칭이 같은 Core를 사용하며, 플랫폼별 GUI·서비스 호출은 별도 증거를 따름 |
