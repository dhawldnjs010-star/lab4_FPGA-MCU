`timescale 1ns/1ps
module tb;
    // 파형 저장 (템플릿 요구): 수업 제공 TB에 이 한 블록만 추가했다.
    initial begin $dumpfile("wave.vcd"); $dumpvars(0, tb); end
    reg [3:0] a, b;
    wire [7:0] m;
    mult_4bit dut(a, b, m);
    integer x, y;
    initial begin
        for (x=0; x<16; x=x+1)
            for (y=0; y<16; y=y+1) begin
                a=x; b=y; #1;
                if (m !== x*y) $fatal(1, "multiply a=%0d b=%0d m=%0d", x,y,m);
            end
        $display("PASS multiplier: 256 input pairs"); $finish;
    end
    initial begin #1000; $fatal(1, "timeout"); end
endmodule

