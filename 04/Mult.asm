// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.
//init the variables: index=1, sum=0
@index
M=1
@sum
M=0
@LOOP
0;JMP
// Loop, adding R0 to sum R1 times
(LOOP)
  // Break if index >= R1
  @index
  D=M
  @R1
  D=D-M
  @BREAK
  D;JGT
  // If if index < R1 , add 1 to index
  @index
  M=M+1
  //Adds R0 to sum
  @R0
  D=M
  @sum
  M=M+D
  @LOOP
  0;JMP
// Break the loop
(BREAK)
  @sum
  D=M
  @R2
  M=D
  @END
(END)
@END
0;JMP