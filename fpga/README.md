# FPGA 개별 실습 (STM32_0 주차)

| 폴더 | 최상위 모듈 | 내용 |
|---|---|---|
| mult_4bit | mult_4bit | 4비트 x 4비트 곱셈기 (m = a*b, 8비트) |
| bcd_conv  | bcd_conv  | BCD(ten, one) -> 이진수 bin[6:0], valid |

각 폴더: src/ 설계, sim/ 수업 제공 테스트벤치(tb, $fatal 자기검사), constraints/pins.xdc 핀 제약.
XDC 핀은 lab1 실습의 XDC에서 옮긴 값이다.

시뮬레이션: cd mult_4bit && iverilog -g2012 -o m.vvp src/*.v sim/*.sv && vvp m.vvp

## 실험 후 (2026-10-12)

각 폴더의 `evidence/post/`에 Vivado XSim 파형, 실행 상태, 보드 시연 영상과 프레임이 있고, `reports/post.md`에 보드 실측 표가 있다. Vivado Tcl 콘솔 전체는 `../evidence/post/fpga/vivado_tcl_console.txt`.
XDC 핀은 보드에서 그대로 동작했다(LED1이 최상위 출력 비트, LED8이 최하위).
