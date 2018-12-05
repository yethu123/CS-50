# cs50
## [Algorithms](https://docs.cs50.net/2017/fall/notes/0/lecture0.html#algorithms)

-   Now that we know how to represent inputs and outputs, we can work on algorithms, which is just step-by-step instructions on how to solve a problem.
#lecture1(c programming)
 
   float y = get_float("y: ");

    // Perform division
    printf("%f divided by %f is %f\n", x, y, x / y);
    

#lecture2(C)
1. preprocessing
- In C, preprocessing involves replacing the lines that start with #include with the contents of the actual file.
2. compiling
 - The compiler takes the complete source code and converts it to assembly code, much simpler instructions that look like this:
      

       main: #   @main
          .cfi_startproc
       # BB#0:
           pushq   %rbp

 3. assembling
  -  Finally, these lines of assembly are converted to 0s and 1s that the CPU can directly understand.
  4. linking
 -  We also need to combine into our program the binary file for standard I/O library that we call functions from, and this last step does exactly that. Recall that we only included stdio.h, which is just the header file that declares the functions, not the actual code for them
      - eprintf, to provide information to ourselves when our program is running:
      - Typecasting is casting, or converting, variables from a certain type, like int, to another, like char, or vice versa.
      - can do cryptography


#lecture3(algorithm)
   1.Searching
  **linear search**
     
    for each element in array
        if element you're looking for
            return true
    return false

 **binary search**
 

    look at middle of sorted array
    if element you're looking for
        return true
    else if element is to left
        search left half of array
    else if element is to right
        search right half of array
    else
        return false


2.Sorting
 1. insertion sort
 2. Bubble sort
 3. selection sort
 -    Insertion sort

    for i from 1 to n-1
       call 0'th through i-1'th elements the "sorted side"
       remove i'th element
       insert it into sorted side in order


-   Bubble sort
```
repeat until no swaps
    for i from 0 to n-2
        if i'th and i+1'th elements out of order
            swap them
```
-   Selection sort
```
    for i from 0 to n-1
       find smallest element between i'th and n-1'th
       swap smallest with i'th element
      
   ```

comparing sorting demonstration
https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html 



