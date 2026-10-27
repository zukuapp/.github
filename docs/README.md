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
2. Jump·API 계약 — [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)의 [매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json)와 [`zuku-api`](https://github.com/zukuapp/zuku-api)의 [OpenAPI 3.1 초안](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)에 있습니다. CLI 명령은 [`zukujs-cli`](https://github.com/zukuapp/zukujs-cli)에 있습니다.
3. ZUKBOX 저작·재생 — [`zukbox`](https://github.com/zukuapp/zukbox), [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime), [`zukbox-player`](https://github.com/zukuapp/zukbox-player)가 에디터·바이너리 파싱·렌더링을 나눠 맡습니다.
