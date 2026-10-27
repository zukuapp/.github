<!-- BEGIN ZUKU OFFICIAL BRAND -->
<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://docs.zuzunza.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)"
        srcset="docs/branding/zuku-logo-dark.png">
      <img src="docs/branding/zuku-logo-light.png"
        alt="ZUKU" width="320">
    </picture>
  </a>
</p>
<p align="center">ZUKU - 내가 불러 일으키는 새로운 창작.</p>
<!-- markdownlint-enable MD033 MD041 -->
<!-- END ZUKU OFFICIAL BRAND -->

![version](https://img.shields.io/badge/version-v27.26102701-informational)

# zukuapp 개발 문서와 공통 안내

이 저장소는 zukuapp 조직 프로필과 조직 공통 커뮤니티 파일을 관리합니다. [`profile/README.md`](profile/README.md)는 [zukuapp 조직 홈](https://github.com/zukuapp)에 표시됩니다.

## 문서 찾기

| 경로 | 내용 |
| --- | --- |
| [조직 프로필](profile/README.md) | 개발자를 위한 첫 화면과 주요 계약 링크 |
| [공식 개발 문서 사이트](https://zukuapp.github.io/docs/) | 브라우저에서 읽는 입문·저장소 목록·공개 명세 |
| [개발 문서 목차](docs/README.md) | 입문, 저장소 지도, 아키텍처, 브랜드 원칙 |
| [ZWF2로 시작하기](docs/getting-started.md) | 공개 도구를 로컬에서 실행하는 검증 가능한 예제 |
| [저장소 지도](docs/repository-map.md) | 공개 저장소별 역할과 기준 문서 |
| [공개 아키텍처](docs/architecture.md) | 파일 형식과 실행 경계 |
| [브랜드·타이포그래피](docs/brand.md) | 승인된 ZUKU 로고 원본과 글꼴 적용 범위 |

## 조직 공통 파일

[`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md), [`SUPPORT.md`](SUPPORT.md), [Issue 양식](.github/ISSUE_TEMPLATE), [Pull Request 양식](.github/PULL_REQUEST_TEMPLATE.md)은 각 저장소에 자체 파일이 없을 때 GitHub가 기본 안내로 사용합니다.

## 이 저장소를 수정할 때

1. 기능과 계약의 사실 관계는 해당 공개 저장소의 README·명세·테스트에서 확인합니다.
   - 입문 경로에는 공개 저장소와 공개 문서만 연결합니다.
2. 조직 홈의 문구와 링크는 [`profile/README.md`](profile/README.md)에서 수정합니다.
   - 웹 문서는 [`zukuapp.github.io/docs/`](https://github.com/zukuapp/zukuapp.github.io/tree/main/docs)에 둡니다.
   - GitHub 문서는 [`docs/`](docs/README.md)에 둡니다.
   - 저장소별 상세 사용법은 소유 저장소로 연결합니다.
3. 로고를 바꿀 때는 [로고 사용 안내](docs/branding/README.md)의 원본 파일과 SHA-256을 따릅니다.
4. 상대 링크, 이미지, 예제 명령을 확인한 뒤 Pull Request에 검증 결과를 적습니다.

## 변경 이력

버전별 변경 사항은 [`CHANGELOG.md`](CHANGELOG.md)에 있습니다.

Trecillo · Crevision · [trecillo.crevision.kr](https://trecillo.crevision.kr) · [contact@crevision.kr](mailto:contact@crevision.kr)
