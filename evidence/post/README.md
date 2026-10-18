# lab4 실험 후 자료 (2026-10-12 실습)

실험 후 보고서의 근거 자료다. 영상은 원본(1080p HEVC)을 720p H.264로 줄이고 소리를 뺀 사본이다.

## STM32 (NUCLEO-G474RE) · `stm32/`

| 파일 | 내용 |
|---|---|
| `task1_PA5_demo.mp4` | 과제1 시연: 내장 LED(PA5), 버튼(PC13)으로 간격 변경, 스톱워치와 함께 촬영 |
| `task2_PB0_demo.mp4` | 과제2 시연: PB0 외부 LED, 시리얼 모니터 `Hello, World!` |
| `task1_PA5_frame.jpg`, `task2_PB0_frame.jpg` | 위 영상의 대표 프레임 |
| `led_trace.py` | 영상에서 LED 켜짐/꺼짐 구간을 읽는 스크립트 (10 fps, 분해능 0.1 s) |
| `led_trace_task*.csv`, `led_segments_task*.txt` | 스크립트 출력 (프레임별 화소 수, ON/OFF 구간 길이) |
| `led_board_timeline.png` | 위 구간을 그린 그림 (보고서 그림) |
| `build_pb0_final.txt` | 과제2 최종 빌드 출력 (오류·경고 없음) |
| `build_pb0_redefined_warning.txt` | 과제2 첫 수정 때의 재정의 경고 (문제 해결 기록) |
| `debug_download.txt` | ST-LINK 다운로드 기록 발췌 |

최종 소스: `Core/Src/ece2_474_routine.c` (과제2 PB0 버전). 과제1은 `BLINK_LED_*` 두 줄의 오른쪽 값을 `LED_ece2_Pin`, `LED_ece2_GPIO_Port`로 두면 된다(커밋 3351085의 상태).

## FPGA (Combo II-DLD, xc7s75fgga484-1, Vivado 2026.1) · `fpga/`

| 파일 | 내용 |
|---|---|
| `fpga/vivado_tcl_console.txt` | 두 프로젝트의 Vivado Tcl 콘솔 전체 (시뮬레이션 PASS, 합성·구현·비트스트림, 프로그래밍) |
| `../../fpga/mult_4bit/evidence/post/` | 곱셈기: XSim 파형, 실행 상태, 보드 시연 영상과 프레임 |
| `../../fpga/bcd_conv/evidence/post/` | BCD 변환: XSim 파형, 실행 상태, 보드 시연 영상과 프레임 |

프레임 파일 이름의 `tNNs`는 시연 영상의 시각(초)이다.
