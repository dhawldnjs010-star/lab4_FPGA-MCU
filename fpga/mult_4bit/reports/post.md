# 실험 후 레포트: STM32_0 FPGA 실습 1 · 4비트 곱셈기

작성자 상혁(2025440084) / 실험일 2026-10-12 / 구현 도구 Vivado 2026.1 / part xc7s75fgga484-1 / top `mult_4bit`(구현), `tb`(시뮬레이션) / XDC `constraints/pins.xdc`

## Vivado 시뮬레이션

RTL `src/mult_design.v`, TB `sim/mult_tb.sv`, XDC를 등록했다. 시뮬레이션 top을 `mult_4bit`로 둔 첫 실행은 자기검사 출력이 없었고, top을 `tb`로 바꾼 뒤 `PASS multiplier: 256 input pairs`, `$finish` 256 ns를 확인했다. Icarus 사전 시뮬레이션(`evidence/pre/`)과 입력 수·종료 시각·PASS 문구가 같다. 파형: `evidence/post/xsim_wave.png`.

## 합성·구현·비트스트림

`synth_design Complete!`, `write_bitstream Complete!` (`evidence/post/vivado_runs.png`). 조합회로라 타이밍 제약이 없고 timing은 통과 수치로 쓰지 않는다. 이용률·DRC 보고서는 저장하지 않았다.

## 실제 보드 기록·실측

Hardware Manager에서 `xc7s75_0`에 `mult_4bit.bit`를 프로그래밍했다(`program_hw_devices` 완료, 로그 `../../evidence/post/fpga/vivado_tcl_console.txt`). 입력은 DIP 스위치, 출력은 LED1~LED8(LED1 = `m[7]`, LED8 = `m[0]`).

| 영상 시각 | LED1~8 | 출력 m | 입력 a × b | 판정 |
|---|---|---|---|---|
| 1 s | 00000000 | 0 | 0 × 0 | 일치 |
| 29 s | 00001111 | 15 | 3 × 5 등 | 일치 |
| 37 s | 01000000 | 64 | 8 × 8 | 일치 (사전 예상표) |
| 41 s | 10110100 | 180 | 12 × 15 등 | 일치 |
| 43 s | 11100001 | 225 | 15 × 15 | 일치 (사전 예상표) |

입력은 시연 때 DIP 스위치로 넣은 값이다. 15와 180은 같은 곱을 내는 조합이 여럿이라 한 예만 적었다.

## 비교·결론

예상값 → Icarus → Vivado XSim이 모두 일치했고, 보드의 LED 값은 다섯 경우 모두 입력한 두 수의 곱과 같았다.

## 제출 링크

영상 `evidence/post/board_demo.mp4`, 프레임 `evidence/post/frame_t*.jpg`, 파형 `evidence/post/xsim_wave.png`.
