# 브랜드·타이포그래피

이 저장소의 시각 기준은 [Trecillo 현행 사이트](https://trecillo.crevision.kr/)입니다. 공식 영문 표기는 **Trecillo**입니다.

## 현행 로고

- 원본: [`game-ci.png` (`20260919`)](https://trecillo.crevision.kr/assets/brand/game-ci.png?v=20260919)
- 저장소 사본: [`profile/assets/brand/trecillo-game-ci-20260919.png`](../profile/assets/brand/trecillo-game-ci-20260919.png)
- SHA-256: `59132493bcf9dbeba0a6df0f8c64a03555ab0d0307ea86992ea47561b4d71e6a`

로고의 분홍 심볼과 흰색 `trecillo` 워드마크는 원본 이미지에 함께 들어 있습니다. 배경은 투명이 아닌 `#0B0C10`입니다. 로고의 분홍 `#FF2D7A`와 사이트 UI 분홍 `#E91E63`은 서로 다른 용도로 유지합니다. 다크·라이트 모드에 같은 검정 타일을 사용하면 원본 대비와 비율이 보존됩니다.

## 서체와 색상

[현행 브랜드 CSS](https://trecillo.crevision.kr/assets/brand.css?v=20260917team)는 본문에 **Pretendard 1.3.9**를 먼저 적용하고 Inter, Noto Sans KR을 불러옵니다. 영문 전시 문구와 숫자에는 Inter를 사용합니다. [색상 토큰](https://trecillo.crevision.kr/assets/family-tokens.css)의 본문색은 `#14171F`, 연한 바탕은 `#F4F5F8`, 경계선은 `#D9DCE5`입니다.

조직 프로필의 [개발자 배너](../profile/assets/developer-hero.png)는 현행 로고 원본을 그대로 배치하고, 한글 문구는 Pretendard Bold·Medium, 영문 레이블은 Inter Bold 4.1의 **글자 윤곽선**으로 저장했습니다. GitHub README는 외부 CSS와 웹폰트를 적용하지 못하므로, 배너 안의 글꼴만 고정됩니다. README 본문은 GitHub가 제공하는 글꼴을 사용하며 제목, 표, 링크를 텍스트로 유지해 검색과 접근성을 살립니다.

## 배너 갱신

배너의 편집 가능한 [SVG 원본](../profile/assets/developer-hero.svg)과 [생성 스크립트](../profile/assets/generate_hero.py)가 함께 있습니다. 스크립트는 위 로고 사본과 버전이 고정된 Pretendard·[Inter](https://github.com/rsms/inter/tree/v4.1) WOFF2를 사용하고, `developer-hero.svg`와 README에 쓰이는 `developer-hero.png`를 생성합니다. Python `fonttools`와 `rsvg-convert`가 필요합니다.

```bash
python3 profile/assets/generate_hero.py
```

로고가 사이트에서 바뀌면 먼저 원본을 다시 확인하고 사본·해시·배너를 함께 갱신하세요. 문구만 바꿀 때는 생성 스크립트의 텍스트를 수정한 뒤 두 자산을 다시 만듭니다. 이미지에는 의미를 전달하는 대체 텍스트를 남깁니다.
