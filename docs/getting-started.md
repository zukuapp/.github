# 시작하기: HTML5 ZIP에서 ZWF2까지

[`zwf`](https://github.com/zukuapp/zwf)는 HTML·JavaScript·CSS·WebAssembly와 로컬 자산을 담은 ZIP을 ZWF2 `.zwf` 패키지로 컴파일하고 검사하는 공개 도구입니다.

## 준비

| 항목 | 요구 사항 |
| --- | --- |
| 도구 | Git, Node.js 22 이상, npm, `zip` 명령 |
| 입력 ZIP | 루트 `index.html` 또는 한 단계의 감싸는 디렉터리 아래 `index.html` |
| 자산 | 스크립트·글꼴·이미지 등 필요한 자산을 ZIP 안에 포함하고 상대 경로로 참조 |

입력 규칙은 [`zwf` README](https://github.com/zukuapp/zwf/blob/main/README.md)에 있습니다. `zwf`는 저장소를 복제해 소스에서 실행합니다.

## ZWF2 패키지를 로컬에서 만들기

저장소에 포함된 `examples/hello/index.html`을 ZIP의 루트에 넣는 예제입니다.

```bash
git clone https://github.com/zukuapp/zwf.git
cd zwf
npm ci
npm test
zip -j hello.zip examples/hello/index.html
node src/cli.mjs compile hello.zip -o hello.zwf --title "Hello ZWF"
node src/cli.mjs inspect hello.zwf
```

`inspect` 결과의 매니페스트에는 `version: 2`, `profile: "html5-sandbox/2"`, `entry_point: "index.html"`이 표시됩니다. 컴파일러는 기존 출력 파일을 덮어쓰지 않습니다. 다시 컴파일할 때는 새 출력 파일 이름을 지정합니다. 다른 앱을 패키징할 때는 브라우저용 파일을 먼저 빌드하고, `index.html`과 필요한 자산을 ZIP에 함께 담습니다.

파일 구조, 무결성 검사, 허용되는 자산과 플레이어의 필수 실행 경계는 [`zwf/SPEC.md`](https://github.com/zukuapp/zwf/blob/main/SPEC.md)에 있습니다.

## 다음 단계

| 목표 | 볼 곳 |
| --- | --- |
| Jump 매니페스트의 필수 필드와 형식 확인 | [`zuku-engine-next2d` 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) |
| ZUKU CLI 사용법 확인 | [`zukujs-cli` README](https://github.com/zukuapp/zukujs-cli/blob/main/README.md) |
| 공개 API의 경로·데이터 모델 검토 | [`zuku-api` OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |
| ZUKBOX의 저작·런타임·플레이어 구조 이해 | [저장소 지도](repository-map.md) · [공개 아키텍처](architecture.md) |
| 문서나 도구에 변경 제안 | [기여 안내](../CONTRIBUTING.md) |

브라우저에서 읽는 전체 안내는 [공식 개발 문서](https://zukuapp.github.io/docs/)에 있습니다.
