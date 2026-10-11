# STM32_0 pre-lab evidence

- logs/    build and simulation logs (build logs are from the cloud environment, GNU Arm 13.2.1)
- sim/     testbench copies with VCD dump, fault-injected designs, VCDs, sample-vector testbench
- fw/      host mock harness for polling_routine() (mock.h, harness.c, wrap.c)
- fig/     figures used in the report and figs.py that draws them from the VCD and fw_log.txt

Reproduce (from the repo root):
    cd fpga/mult_4bit && iverilog -g2012 -o m.vvp src/*.v sim/*.sv && vvp m.vvp
    gcc -Wall -Wextra -o h evidence/pre/fw/harness.c && ./h
