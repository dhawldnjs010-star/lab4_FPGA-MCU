# lab4 FPGA - BCD to 이진수 변환 (bcd_conv)

STM32_0 주차 FPGA 개별 실습 2. 최상위 모듈 `bcd_conv(one[3:0], ten[3:0], bin[6:0], valid)`, bin = 10 x ten + one,
ten, one 이 모두 9 이하일 때만 valid = 1. 조합회로, 클록 없음. 템플릿: Glaysia/fpga-lab-template (커밋 0b3318e466e9d77f7d3880df09c827788f361913).

| 경로 | 내용 |
|---|---|
| src/bcd_design.v | 설계 (수업 제공 설계 사용, bcd_to_binary + bcd_conv) |
| sim/bcd_tb.sv | 수업 제공 자기검사 TB. 파형 저장용 `$dumpfile/$dumpvars` 한 줄만 추가 |
| constraints/pins.xdc | 핀 제약 (lab1 XDC에서 옮긴 사전 작성본, 보드 확인 전) |
| simulation.json | 템플릿 실행 설정 |
| evidence/pre/ | 사전 시뮬레이션 로그·파형, 오류 주입 결과 |

실행: FPGA.code-workspace 를 열고 Run Task 01, 02, 03. 터미널: `python tools/fpga_lab.py simulate`

핀 배정 (최상위 비트부터): ten = Y1 W3 U2 T1 (DIP), one = W4 W1 V4 U4 (DIP), bin = M4 M2 N7 M7 M3 M1 N5 (LED), valid = L4 (LED), LVCMOS33.
주의: bcd_conv 의 포트 순서는 (one, ten, ...) 이고 하위 모듈은 (ten, one, ...) 이다. 핀 연결 시 두 입력이 뒤바뀌지 않게 한다.

사전 검증 결과 (Icarus Verilog 12.0): 유효 100개·무효 156개 입력 PASS. 오류 주입((ten<=9) -> (ten<=10))에서 FATAL.
Vivado 합성·보드 시연은 아직 수행하지 않았다.
