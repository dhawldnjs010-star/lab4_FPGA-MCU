# STM32_0 FPGA 실습 1 - 4비트 곱셈기 (최상위: mult_4bit)
# 핀 출처: lab1_03_adder4 / lab1_07_demux1to8 의 pins.xdc (같은 보드, 같은 DIP 스위치·LED)
# 보드 확인 전 사전 작성본. 수업에서 핀맵과 대조 후 수정한다.
# a, b 입력: DIP 스위치 (최상위 비트가 [3])
set_property PACKAGE_PIN Y1 [get_ports {a[3]}]
set_property PACKAGE_PIN W3 [get_ports {a[2]}]
set_property PACKAGE_PIN U2 [get_ports {a[1]}]
set_property PACKAGE_PIN T1 [get_ports {a[0]}]
set_property PACKAGE_PIN W4 [get_ports {b[3]}]
set_property PACKAGE_PIN W1 [get_ports {b[2]}]
set_property PACKAGE_PIN V4 [get_ports {b[1]}]
set_property PACKAGE_PIN U4 [get_ports {b[0]}]
# m 출력: LED 8개 (최상위 비트가 [7])
set_property PACKAGE_PIN L4 [get_ports {m[7]}]
set_property PACKAGE_PIN M4 [get_ports {m[6]}]
set_property PACKAGE_PIN M2 [get_ports {m[5]}]
set_property PACKAGE_PIN N7 [get_ports {m[4]}]
set_property PACKAGE_PIN M7 [get_ports {m[3]}]
set_property PACKAGE_PIN M3 [get_ports {m[2]}]
set_property PACKAGE_PIN M1 [get_ports {m[1]}]
set_property PACKAGE_PIN N5 [get_ports {m[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a[*] b[*] m[*]}]
