# 실험 후 레포트: STM32_0 FPGA 실습 2 · BCD를 이진수로 변환

작성자 상혁(2025440084) / 실험일 2026-10-12 / 구현 도구 Vivado 2026.1 / part xc7s75fgga484-1 / top `bcd_conv`(구현), `tb`(시뮬레이션) / XDC `constraints/pins.xdc`

## Vivado 시뮬레이션

RTL `src/bcd_design.v`, TB `sim/bcd_tb.sv`, XDC를 등록했다. `PASS BCD: 100 valid and 156 invalid inputs`, `$finish` 256 ns. Icarus 사전 시뮬레이션과 같다. 파형: `evidence/post/xsim_wave.png`.

## 합성·구현·비트스트림

`synth_design Complete!`, `write_bitstream Complete!` (`evidence/post/vivado_runs.png`). 첫 `open_hw_target`은 `No devices detected`로 실패했고, 다시 연결한 뒤 `program_hw_devices`가 완료됐다.

## 실제 보드 기록·실측

출력은 LED1 = `valid`, LED2~LED8 = `bin[6:0]`.

| 영상 시각 | LED1~8 | valid | bin | 입력 (ten, one) | 판정 |
|---|---|---|---|---|---|
| 5 s | 10000000 | 1 | 0 | (0, 0) | 예상과 같음 |
| 17 s | 10101111 | 1 | 47 | (4, 7) | 사전 예상표와 같음 |
| 25 s | 11011011 | 1 | 91 | (9, 1) | 예상과 같음 |
| 33 s | 01100100 | 0 | 100 | (10, 0) | 무효 입력, 사전 예상표와 같음 |
| 37 s | 00010011 | 0 | 19 | (14, 7): 147 mod 128 | 무효 입력, 7비트 잘림과 일치 |

입력은 시연 때 DIP 스위치로 넣은 값이다.

## 비교·결론

유효 입력 세 경우는 bin이 10 × ten + one과 같고, 무효 입력 두 경우는 valid가 0이며 bin은 사전 보고서에서 예상한 대로 하위 7비트만 남았다.

## 제출 링크

영상 `evidence/post/board_demo.mp4`, 프레임 `evidence/post/frame_t*.jpg`, 파형 `evidence/post/xsim_wave.png`.
