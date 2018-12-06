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

_Running Time_

-   The notation for theoretical running time includes:
    
    -   _O_, worst-case running time, or upper bound
        
    -   Ω, best-case running time, or lower bound
        
    -   Θ, if both of those are the same

_Merge sort_

    on input of n elements
        if n < 2
            return
        else
            sort left half of elements
            sort right half of elements
            merge sorted halves



**Lecture4**
  

 - In C, we call variables that store addresses of other variables **pointers**. 
 (The `*` symbol indicates that a variable is a pointer to some other variable type,
 so we could have `int *` in addition to `char *` and others.)
 - (`*` is also used, confusingly, when declaring a variable that the variable should be a pointer. 
 But in this case, and other cases, it is used to go to some address and read the value there.)
 - `scanf` is a function in C’s standard I/O library, that reads from the user’s keyboard.
 The arguments it takes are like `printf`'s, but instead of printing to the screen it stores values to variables.
 Here, we are telling it to look for something that matches a `%i`, integer, and to store it in `&x`.
 - `&` gets us the address of a variable
 -   The heap, at top, is where memory for `malloc` comes from.
    
-   The stack, in the bottom, is used for functions. In fact, for our C programs, 
the very bottom of the stack contains a chunk of memory for our `main` function, such as any local variables or arguments.
    
-   Then, on top of that, the next function called, such as `swap`, will have its own chunk of memory, called a **stack frame**:
- `x` was copied into `a`, and `y` was copied into `b`, so `swap` was working with its own copy of the variables. And once `swap` returns, that entire frame of memory is marked as free to be used again.
- _Images_

1.The bit `1` to represent black and `0` for white, we can create an image with a grid of bits.
The first three bytes of a JPEG file are `0xff 0xd8 0xff`. `0xff` is 255. `0xd8` is 216.
2.Bitmap files, with the extension BMP, maps bits directly to pixels.



 - a `struct`, we can create a more complicated data type:
  ```

    typedef struct
    {
        string name;
        string dorm;
    }
    student;
 ```

**Memory**

 -  pointers, which is  an address to a location in memory where some data might be stored.
 **Memory  in**
 - The text area contains the binary code of our compiled program.
    
 -   Initialized and uninitialized data refers to global variables for our program
 - **Heap**
	 - The heap has dynamically allocated memory, or memory allocated when the program is running.
	 - can manage manually
	 - `malloc`()
	      - which allocates some fixed amount of memory
	      - calloc()   (call location)
	        -sets the initial values of that memory to 0, so we don’t have garbage values.
	  - `realloc` grows the size of previously allocated memory,
	  - **Heap Overflow**
	       - start allocating so much memory from the heap that we start reaching memory that our stack has grown to.
	        
 **Stack**
 
 -   The stack contains slices, or frames, of memory for functions and their local variables.
 - **stack overflow**
    - the heap is somewhere above it. If we were to call enough functions, and use up enough
    much memory, we could overflow the stack to the point where we start overwriting memory in the heap.
    
   **Environment variables,** which we’ll see in web programming,
   are variables like usernames and passwords that we don’t want to store in the source code of our program,
   but still want access to via different mechanisms.
 
 - Buffer
 A buffer is a chunk of memory that we’ve allocated to store data,
 **Buffer Overflow**
     - writing more data than the size of the buffer,
 
 **Tool for memory**
    - valgrind

**free(x)**
 - we used `malloc` to allocate memory. When we finish using it, it’s best to call `free`

**DATA STRUCTURE**

 - With pointers, we can connect pieces of memory together in any way we want to.
