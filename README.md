# cs50
## [Algorithms](https://docs.cs50.net/2017/fall/notes/0/lecture0.html#algorithms)

-   Now that we know how to represent inputs and outputs, we can work on algorithms, which is just step-by-step instructions on how to solve a problem.
#lecture1(c programming)
 
   float y = get_float("y: ");

    // Perform division
    printf("%f divided by %f is %f\n", x, y, x / y);
    
#lecture2(C)
  

    1.preprocessing
        In C, preprocessing involves replacing the lines that start with #include with the contents of the actual file.
    2.compiling
      The compiler takes the complete source code and converts it to assembly code, much simpler instructions that look like this:
           main:                               #   @main
              .cfi_startproc
           # BB#0:
               pushq   %rbp
     3.assembling
        Finally, these lines of assembly are converted to 0s and 1s that the CPU can directly understand.
     4.linking
        We also need to combine into our program the binary file for standard I/O library that we call functions from, and this last step does exactly that. Recall that we only included stdio.h, which is just the header file that declares the functions, not the actual code for them

