<p align="center">
  <img src="assets/hero-dark.svg#gh-dark-mode-only" alt="ZUKU — Create what moves next. 보고, 넘기고, 직접 뛰어드세요." width="960">
  <img src="assets/hero-light.svg#gh-light-mode-only" alt="ZUKU — Create what moves next. 보고, 넘기고, 직접 뛰어드세요." width="960">
</p>

<p align="center">
  <a href="https://zuzunza.com"><img src="assets/cta-play.svg" alt="Play on zuzunza.com" height="40"></a>
  <a href="https://github.com/zukuapp"><img src="assets/cta-org.svg" alt="github.com/zukuapp" height="40"></a>
  <a href="https://zukuapp.github.io/"><img src="assets/cta-site.svg" alt="Company site" height="40"></a>
  <a href="mailto:contact@zuzunza.com"><img src="assets/cta-mail.svg" alt="contact@zuzunza.com" height="40"></a>
</p>

<p align="center">
  <img src="assets/ripple-rule.svg" alt="" width="960">
</p>

**ZUKU (즈쿠)** 는 Tresillo(트레실로)가 만드는 인터랙티브 UGC 미디어 플랫폼입니다.  
관객으로 머물지 말고, 아래 표면 중 하나를 눌러 들어가세요.

## 표면을 고르세요

카테고리 이름은 로케일과 상관없이 **Thread / Hype / Swipe / Jump / Vive / Vine** 입니다. Aist는 생성 전용 웹 스튜디오입니다.

<p align="center">
  <a href="https://www.zuzunza.com"><img src="assets/card-thread.svg" alt="Thread — 이야기. www.zuzunza.com" height="168"></a>
  <a href="https://hype.zuzunza.com"><img src="assets/card-hype.svg" alt="Hype — 창작. hype.zuzunza.com" height="168"></a>
  <a href="https://swipe.zuzunza.com"><img src="assets/card-swipe.svg" alt="Swipe — 넘김. swipe.zuzunza.com" height="168"></a>
  <a href="https://jump.zuzunza.com"><img src="assets/card-jump.svg" alt="Jump — 플레이. jump.zuzunza.com" height="168"></a>
</p>
<p align="center">
  <a href="https://vive.zuzunza.com"><img src="assets/card-vive.svg" alt="Vive — 문학. vive.zuzunza.com" height="168"></a>
  <a href="https://vine.zuzunza.com"><img src="assets/card-vine.svg" alt="Vine — 사운드. vine.zuzunza.com" height="168"></a>
  <a href="https://aist.zuzunza.com"><img src="assets/card-aist.svg" alt="Aist — 생성. aist.zuzunza.com" height="168"></a>
</p>

하단 탭은 Thread · Hype · Swipe · Jump 입니다. Vive와 Vine은 탐색·딥링크로 들어가는 2차 입구입니다.

## 어떻게 들어오시겠어요?

원하는 문을 열어 보세요. 각 경로가 바로 다음 행동을 안내합니다.

<details>
<summary><strong>플레이어</strong> — 보고, 넘기고, 바로 뛰어들기</summary>
<br/>

- [Thread](https://www.zuzunza.com)에서 이야기를 읽고, 다른 표면의 미리보기(≤30초)를 만납니다.
- [Hype](https://hype.zuzunza.com) · [Swipe](https://swipe.zuzunza.com)에서 창작 피드를 따라갑니다.
- 게임은 [Jump](https://jump.zuzunza.com)에서만 풀 플레이됩니다. Thread에는 미리보기와 딥링크만 있습니다.

</details>

<details>
<summary><strong>크리에이터</strong> — 형식에 맞춰 올리기</summary>
<br/>

| 만들고 싶은 것 | 가는 곳 |
|---|---|
| 인터랙티브 · 가로 영상 · 사진 | [Hype](https://hype.zuzunza.com) |
| 세로 숏폼 | [Swipe](https://swipe.zuzunza.com) (스튜디오 없음, Swipe→Hype 배급 불가) |
| 글 · 문학 | [Vive](https://vive.zuzunza.com) (Thread 붐업은 작성자 선택) |
| 음악 · 보이스 · UTAU | [Vine](https://vine.zuzunza.com) |
| AI로 게임 초안 | [Aist](https://aist.zuzunza.com) → Jump Studio draft |

</details>

<details>
<summary><strong>게임 메이커</strong> — Jump에 올리기</summary>
<br/>

브라우저에서 바로 실행되는 WASM · HTML5 · ZWF 작품을 만듭니다.

1. 엔진·패키지 계약은 [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)
2. 검증·패키징은 [`zuku-cli`](https://github.com/zukuapp/zuku-cli)
3. API 계약은 [`zuku-api`](https://github.com/zukuapp/zuku-api)
4. 저작 툴은 [`zukbox`](https://github.com/zukuapp/zukbox) · 플레이어 [`zukbox-player`](https://github.com/zukuapp/zukbox-player)

공개는 [Jump Studio](https://jump.zuzunza.com)에서, 플레이는 Jump 허브에서.

</details>

<details>
<summary><strong>오픈소스 기여자</strong> — 엔진·툴·계약에 손대기</summary>
<br/>

공개 작업대는 아래 칩을 누르세요. 이슈를 열거나 PR을 보내는 것이 기여의 시작입니다.

- 조직 이슈 검색: [open issues in zukuapp](https://github.com/search?q=org%3Azukuapp+is%3Aissue+is%3Aopen&type=issues)
- 브랜드 표기: **ZUKU / zuku / 즈쿠**. “시즈쿠”는 쓰지 않습니다.
- 격리 핵심(syscall 필터 · 메모리 카운팅 내부)은 공개하지 않습니다. 문서에는 경계·한도·인터페이스만 적습니다.

</details>

<details>
<summary><strong>회사 · 파트너</strong> — Tresillo와 이야기하기</summary>
<br/>

- 기업 사이트: [zukuapp.github.io](https://zukuapp.github.io/)
- 서비스: [zuzunza.com](https://zuzunza.com)
- 메일: [contact@zuzunza.com](mailto:contact@zuzunza.com)
- Seoul, Korea

</details>

<p align="center">
  <img src="assets/ripple-rule.svg" alt="" width="960">
</p>

## 공개 작업대

클릭하면 해당 저장소로 이동합니다.

<p align="center">
  <a href="https://github.com/zukuapp/zuku-engine-next2d"><img src="assets/chip-engine.svg" alt="zuku-engine-next2d" height="56"></a>
  <a href="https://github.com/zukuapp/zuku-cli"><img src="assets/chip-cli.svg" alt="zuku-cli" height="56"></a>
  <a href="https://github.com/zukuapp/zuku-api"><img src="assets/chip-api.svg" alt="zuku-api" height="56"></a>
  <a href="https://github.com/zukuapp/zukbox"><img src="assets/chip-zukbox.svg" alt="zukbox" height="56"></a>
</p>
<p align="center">
  <a href="https://github.com/zukuapp/zukbox-player"><img src="assets/chip-player.svg" alt="zukbox-player" height="56"></a>
  <a href="https://github.com/zukuapp/zukbox-runtime"><img src="assets/chip-runtime.svg" alt="zukbox-runtime" height="56"></a>
  <a href="https://github.com/zukuapp/shizuku"><img src="assets/chip-home.svg" alt="shizuku" height="56"></a>
  <a href="https://github.com/zukuapp/zukuapp.github.io"><img src="assets/chip-site.svg" alt="zukuapp.github.io" height="56"></a>
</p>

## 우리가 지키는 경계

인터랙티브 워크로드는 **권한 없는 격리 경계**와 계약된 CPU · 메모리 · PID · FD 한도 안에서만 실행됩니다.

- **Unprivileged by design** — 샌드박스 밖에서 플레이하지 않습니다.
- **Explicit contracts** — 의존성 · API 버전 · 스키마를 문서 계약으로 고정합니다.
- **Resource-aware** — 한도는 창작물과 플랫폼을 함께 지킵니다.
- **Standards first** — Next.js · WebAssembly · Rust · PostgreSQL · Redis · nginx · Cloudflare.

보안 계약과 공개 표준은 투명하게, 격리 핵심 구현은 사유 영역으로 둡니다.

<p align="center">
  <img src="assets/ripple-rule.svg" alt="" width="960">
</p>

<p align="center">
  <strong>Tresillo</strong> · Seoul, Korea · <a href="mailto:contact@zuzunza.com">contact@zuzunza.com</a><br>
  © 2026 Tresillo. All rights reserved.
</p>
