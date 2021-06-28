// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Pixel's starting address = 8191 + SCREEN = 512 * 256 - 1 + 16384
(INIT)
    @24575
    D=A
    @address
    M=D   
// Detects a pressed key  
(WATEKEY)  
    // Init pixel value to white
    @pixel
    M=0     
    @KBD
    D=M
    // Change pixel to black in case of pressed key
    @BLACK
    D;JNE
//changes the color of screen   
(LOOPPAINTSCREEN)
    @pixel
    D=M
    @address
    A=M
    M=D     // Memory[address] = pixel
    @address
    M=M-1   // address = address - 1
    D=M
    @SCREEN
    D=D-A   // Memory[address] - 16384
    @INIT
    D; JLT
    @LOOPPAINTSCREEN
    0; JMP    
(BLACK)
// Init pixel value to black
    @pixel
    M=-1     
    @LOOPPAINTSCREEN
    0; JMP
    
    
    