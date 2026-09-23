# 시작하기: HTML5 ZIP에서 ZWF2까지

[`zwf`](https://github.com/zukuapp/zwf)는 HTML·JavaScript·CSS·WebAssembly와 로컬 자산을 담은 ZIP을 ZWF2 `.zwf` 패키지로 컴파일하고 검사하는 공개 도구입니다. 아래 과정은 로컬 파일만 사용합니다. 패키지를 서비스에 게시하거나 API를 호출하지 않습니다.

## 준비

- Git, Node.js **22 이상**, npm, `zip` 명령이 필요합니다.
- 컴파일할 ZIP에는 루트 `index.html` 또는 **한 단계의 감싸는 디렉터리** 아래 `index.html`이 있어야 합니다. 스크립트·글꼴·이미지 등 필요한 자산은 ZIP 안에 넣고 경로는 상대 경로로 빌드하세요. [입력 규칙](https://github.com/zukuapp/zwf/blob/main/README.md)을 확인할 수 있습니다.
- `zwf` 패키지는 현재 npm에 게시되지 않았습니다. 아래에서는 공개 저장소를 복제해 실행합니다.

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

`inspect` 결과의 매니페스트에서 `version: 2`, `profile: "html5-sandbox/2"`, `entry_point: "index.html"`을 확인하세요. 출력 파일은 기존 파일을 덮어쓰지 않습니다. 다시 컴파일하려면 새 출력 파일 이름을 지정합니다. 다른 앱을 패키징할 때는 먼저 브라우저에서 사용할 파일을 빌드한 뒤, `index.html`과 필요한 자산을 ZIP에 함께 담습니다.

파일 구조, 무결성 검사, 허용되는 자산과 플레이어의 필수 실행 경계는 [`zwf/SPEC.md`](https://github.com/zukuapp/zwf/blob/main/SPEC.md)에 있습니다. 여기서 만드는 **ZWF2**는 ZUKBOX의 [이전 `ZWF1` 바이너리 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md)과 다릅니다. 확장자가 같아도 두 파일을 같은 파서의 입력으로 취급하지 마세요.

## 다음 단계

| 목표 | 볼 곳 |
| --- | --- |
| Jump 매니페스트의 필수 필드와 형식 확인 | [`zuku-engine-next2d` 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) |
| Jump CLI가 제공하는 명령과 설정 확인 | [`zuku-cli` README](https://github.com/zukuapp/zuku-cli/blob/main/README.md) |
| 공개 API의 경로·데이터 모델 검토 | [`zuku-api` OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |
| ZUKBOX의 저작·런타임·플레이어 구조 이해 | [저장소 지도](repository-map.md) · [공개 아키텍처](architecture.md) |
| 문서나 도구에 변경 제안 | [기여 안내](../CONTRIBUTING.md) |

각 저장소의 README와 명세가 해당 도구의 현재 사용법을 정의합니다. 이 페이지의 ZWF2 예제를 다른 도구의 설치·게시 절차로 해석하지 마세요.
