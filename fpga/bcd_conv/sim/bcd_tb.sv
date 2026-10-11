`timescale 1ns/1ps
module tb;
    // 파형 저장 (템플릿 요구): 수업 제공 TB에 이 한 블록만 추가했다.
    initial begin $dumpfile("wave.vcd"); $dumpvars(0, tb); end
    reg [3:0] ten, one;
    wire [6:0] bin;
    wire valid;
    bcd_conv dut(one, ten, bin, valid);
    integer t, o;
    initial begin
        for(t=0;t<16;t=t+1)
            for(o=0;o<16;o=o+1) begin
                ten=t; one=o; #1;
                if(valid !== ((t<10)&&(o<10))) $fatal(1,"BCD valid");
                if(t<10 && o<10 && bin !== t*10+o) $fatal(1,"BCD value");
            end
        $display("PASS BCD: 100 valid and 156 invalid inputs"); $finish;
    end
    initial begin #1000; $fatal(1,"timeout"); end
endmodule

