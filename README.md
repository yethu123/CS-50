# cs50
## [Algorithms](https://docs.cs50.net/2017/fall/notes/0/lecture0.html#algorithms)

-   Now that we know how to represent inputs and outputs, we can work on algorithms, which is just step-by-step instructions on how to solve a problem.
#lecture1(c programming)
 
   float y = get_float("y: ");

    // Perform division
    printf("%f divided by %f is %f\n", x, y, x / y);
    
#lecture2(C)
  

preprocessing

    In C, preprocessing involves replacing the lines that start with #include with the contents of the actual file.

compiling

    The compiler takes the complete source code and converts it to assembly code, much simpler instructions that look like this:

    main:                               #   @main
        .cfi_startproc
    # BB#0:
        pushq   %rbp
    .Ltmp0:
        .cfi_def_cfa_offset 16
    .Ltmp1:
        .cfi_offset %rbp, -16
        movq %rsp, %rbp

