# 공개 아키텍처와 실행 경계

ZUKU의 공개 저장소는 게임 **형식과 인터페이스**를 나누어 설명합니다. 이 페이지는 공개 명세에서 확인되는 경계를 연결한 지도이며, 비공개 구현이나 운영 환경의 상태를 설명하지 않습니다.

## HTML5 ZIP → ZWF2

```text
HTML5 게임 파일 → ZIP → zwf 컴파일러 → ZWF2 .zwf
                                      └→ 검사기(inspect)
ZWF2 .zwf → 호환 플레이어의 검증 → 격리된 iframe에서 실행
```

[`zwf` 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md)는 **16바이트 `ZWF2` 헤더 + JSON 매니페스트 + ZIP**을 정의합니다. 매니페스트는 `version: 2`, `profile: "html5-sandbox/2"`, 진입점, 파일별 SHA-256 등을 담습니다. 해시는 파일 손상을 찾아내는 수단이며 제작자 신원을 증명하는 서명은 아닙니다.

호환 플레이어는 사용 전에 컨테이너와 파일 경로·크기·해시를 검사해야 합니다. 명세의 필수 실행 경계에는 불투명 출처의 `iframe`, `sandbox="allow-scripts allow-pointer-lock"`, 응답 헤더의 CSP, 민감한 브라우저 권한 거부가 포함됩니다. 게임 코드를 서버에서 실행하거나 부모 문서·계정 자격 증명을 게임에 전달하는 방식은 명세에 맞지 않습니다.

이 경계는 플랫폼 데이터와 브라우저 권한을 분리하기 위한 것입니다. **CPU·GPU·메모리 사용량의 결정적 제한이나 운영체제 수준의 샌드박스를 제공한다는 뜻은 아닙니다.** 브라우저 CSP만으로 모든 외부 네트워크 동작과 iframe 자체 탐색을 완전히 막을 수도 없습니다. 자세한 요구사항과 한계는 [ZWF2 명세의 Mandatory player behavior](https://github.com/zukuapp/zwf/blob/main/SPEC.md#mandatory-player-behavior)를 따르세요.

## ZUKBOX의 이전 ZWF 바이너리

```text
ZUKBOX 저작물 → ZWF1 바이너리 → zukbox-runtime (WASM 파싱·타임라인)
                                           → zukbox-player (렌더링)
```

[`zukbox-runtime`의 v0.1 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md)은 `ZWF1` 헤더와 청크 기반 바이너리 포맷을 정의합니다. 런타임은 파일 검증·타임라인 평가·렌더 큐 생성을 맡고, [`zukbox-player`](https://github.com/zukuapp/zukbox-player)는 렌더링을 맡습니다. 런타임 README는 스크립트 실행을 호스트의 별도 경계로 설명합니다.

**ZWF1과 ZWF2는 확장자 `.zwf`를 공유하지만 서로 다른 파일 형식입니다.** ZWF2 컴파일러는 ZWF2를 출력합니다. ZUKBOX의 ZWF1 형식은 별도 명세와 파서를 기준으로 다루세요. 형식별 상태와 호환 범위는 각 저장소의 최신 명세에서 확인합니다.

## 계약을 찾는 순서

| 확인할 것 | 단일 기준 문서 |
| --- | --- |
| HTML5 ZIP의 ZWF2 파일 구조와 플레이어 경계 | [`zwf/SPEC.md`](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| ZUKBOX 바이너리 파일 구조 | [`zukbox-runtime` 형식 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md) |
| Jump 패키지 메타데이터 | [`zuku-engine-next2d` 매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json) |
| 공개 API의 경로와 데이터 모델 | [`zuku-api` OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml) |

더 넓은 저장소 목록은 [저장소 지도](repository-map.md)에, 직접 만들어 보는 절차는 [시작하기](getting-started.md)에 있습니다.
