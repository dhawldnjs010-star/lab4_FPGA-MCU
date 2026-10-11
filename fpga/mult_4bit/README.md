# lab4 FPGA - 4비트 곱셈기 (mult_4bit)

STM32_0 주차 FPGA 개별 실습 1. 최상위 모듈 `mult_4bit(a[3:0], b[3:0], m[7:0])`, m = a x b (무부호, 0~225).
조합회로라 클록·리셋이 없다. 템플릿: Glaysia/fpga-lab-template (커밋 0b3318e466e9d77f7d3880df09c827788f361913).

| 경로 | 내용 |
|---|---|
| src/mult_design.v | 설계 (수업 제공 설계 사용, multiply_unsigned + mult_4bit) |
| sim/mult_tb.sv | 수업 제공 자기검사 TB. 파형 저장용 `$dumpfile/$dumpvars` 한 줄만 추가 |
| constraints/pins.xdc | 핀 제약 (lab1 XDC에서 옮긴 사전 작성본, 보드 확인 전) |
| simulation.json | 템플릿 실행 설정 (sources / testbench / simulation_top = tb) |
| evidence/pre/ | 사전 시뮬레이션 로그·파형, 오류 주입 결과 |

실행: VS Code에서 FPGA.code-workspace를 열고 Terminal > Run Task 의 01 Check tools, 02 Simulate, 03 Open waveform.
터미널: `python tools/fpga_lab.py simulate`

핀 배정 (최상위 비트부터): a = Y1 W3 U2 T1 (DIP), b = W4 W1 V4 U4 (DIP), m = L4 M4 M2 N7 M7 M3 M1 N5 (LED), LVCMOS33.

사전 검증 결과 (Icarus Verilog 12.0): 256개 조합 PASS (evidence/pre/simulation_log.txt). SIMULATED는 실행 완료를
뜻하며 정답 판정은 TB의 $fatal 자기검사가 한다. 오류 주입(a*b -> a+b)에서는 FATAL이 났다 (fault_injection_log.txt).
Vivado 합성·보드 시연은 아직 수행하지 않았다. 로그는 저장소의 .gitignore 때문에 .txt 이름으로 보관한다.
