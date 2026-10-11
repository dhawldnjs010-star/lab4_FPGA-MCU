# STM32_0 FPGA 실습 2 - BCD -> 이진수 변환 (최상위: bcd_conv)
# 핀 출처: lab1_03_adder4 / lab1_07_demux1to8 의 pins.xdc (같은 보드, 같은 DIP 스위치·LED)
# 보드 확인 전 사전 작성본. 수업에서 핀맵과 대조 후 수정한다.
# ten: DIP 스위치 4개, one: DIP 스위치 4개 (최상위 비트가 [3])
set_property PACKAGE_PIN Y1 [get_ports {ten[3]}]
set_property PACKAGE_PIN W3 [get_ports {ten[2]}]
set_property PACKAGE_PIN U2 [get_ports {ten[1]}]
set_property PACKAGE_PIN T1 [get_ports {ten[0]}]
set_property PACKAGE_PIN W4 [get_ports {one[3]}]
set_property PACKAGE_PIN W1 [get_ports {one[2]}]
set_property PACKAGE_PIN V4 [get_ports {one[1]}]
set_property PACKAGE_PIN U4 [get_ports {one[0]}]
# bin 출력: LED 7개, valid: 맨 왼쪽 LED
set_property PACKAGE_PIN M4 [get_ports {bin[6]}]
set_property PACKAGE_PIN M2 [get_ports {bin[5]}]
set_property PACKAGE_PIN N7 [get_ports {bin[4]}]
set_property PACKAGE_PIN M7 [get_ports {bin[3]}]
set_property PACKAGE_PIN M3 [get_ports {bin[2]}]
set_property PACKAGE_PIN M1 [get_ports {bin[1]}]
set_property PACKAGE_PIN N5 [get_ports {bin[0]}]
set_property PACKAGE_PIN L4 [get_ports valid]
set_property IOSTANDARD LVCMOS33 [get_ports {ten[*] one[*] bin[*] valid}]
