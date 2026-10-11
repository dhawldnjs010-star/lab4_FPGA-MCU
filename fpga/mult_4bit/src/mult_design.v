`timescale 1ns/1ps
module mult_4bit(input wire [3:0] a, b, output wire [7:0] m);
    multiply_unsigned #(.WIDTH(4)) u_multiply(a, b, m);
endmodule


`timescale 1ns/1ps
// 4비트 곱셈: 입력 두 개를 곱해 8비트 결과를 만듭니다.
module multiply_unsigned #(parameter WIDTH = 4)(
    input wire [WIDTH-1:0] a, b,
    output wire [2*WIDTH-1:0] product
);
    assign product = a * b;
endmodule

