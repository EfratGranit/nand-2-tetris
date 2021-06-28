// Run tests inside the Guy game
//
// It compares a value of a static variable:
//   11111 - failure
//   22222 - success
//
// The static variable address is:
//   30 - VM files of the OS are copied in the Guy directory (used in CI)
//   17 - the Guy directory has only its own VM files and VME uses built-ins

load ,
output-file Guy.out,
compare-to Guy.cmp,
output-list RAM[30]%D1.6.1;

// Load menu
repeat 1000000 {
    vmstep;
}

// Enter test menu and run all tests
set RAM[24576] 84;  // Press `T`
repeat 1000000 {
    vmstep;
}
set RAM[24576] 0;   // Release `T`

repeat 1000000 {
    vmstep;
}

set RAM[24576] 65;  // Press `A`
repeat 1000000 {
    vmstep;
}
set RAM[24576] 0;   // Release `A`

// Running tests here
repeat 1000000 {
    vmstep;
}

// Exit to main menu
set RAM[24576] 69;  // Press `E`
repeat 1000000 {
    vmstep;
}
set RAM[24576] 0;   // Release `E`

repeat 1000000 {
    vmstep;
}

output;
