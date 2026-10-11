`timescale 1ns/1ps
module sample_tb;
  reg [3:0] a,b; wire [7:0] m; mult_4bit u(a,b,m);
  reg [3:0] ten,one; wire [6:0] bin; wire valid; bcd_conv v(one,ten,bin,valid);
  task mul(input [3:0] x,y); begin a=x;b=y;#1; $display("MUL %0d x %0d = %0d (0x%02h)",x,y,m,m); end endtask
  task cv(input [3:0] t,o); begin ten=t;one=o;#1; $display("BCD ten=%0d one=%0d -> bin=%0d (0b%07b) valid=%0b",t,o,bin,bin,valid); end endtask
  initial begin
    mul(0,0); mul(3,5); mul(15,1); mul(15,15); mul(8,8);
    cv(0,0); cv(1,2); cv(4,7); cv(9,9); cv(10,0); cv(0,10); cv(15,15);
  end
endmodule
