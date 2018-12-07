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

**Lecture5_Memory**

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
**Lecture8_python_basic**

 - Just main(troubled in that)
 ````
def main():
    print("hello, world")

if __name__ == "__main__":
    main()
````

 - -   -   `get_char`
        
    -   `get_float`
        
    -   `get_int`
        
    -   `get_string`
        
    -   …​
        
    
-   And there are even more types and features built into Python, like:
    
    -   `complex`
        
        -   complex numbers from mathematics
            
        
    -   `dict`
        
        -   a dictionary, like a hash table
            
        
    -   `list`
        
        -   like an array that automatically grows and shrinks
            
        
    -   `range`
        
    -   `set`
        
        -   a list with unique items, with operations like those of sets in mathematics
            
        
    -   `tuple`
        
        -   like structs, but without any specifications, like `(x, y)` to store two numbers
            
        
    -   …​
  - Python also doesn’t have a `do while` loop, so instead we use `while True`, and `break`

**Lecture9_p2**
 - @app.route` to indicate what the route, or URL, should trigger the function we define below.
  
  **Lecture10_SQL**
 - A **cookie** (in this context) is a small piece of information unique to our login that a web server gives to our browser, that our browser can send back in the future, to verify who we are. We can think of it like a digital handstamp.
 
 - `session` is the key for the cookie, like a variable name, and `value` will be our unique handstamp, which might be a large random number that’s hard for others to guess.
 - **Database**
 - SQL, Structured Query Language, is a programming language that we use to talk to a database, a program that stores data and responds to requests for data, like a web server.
 
 - In SQL, we’ll use a few basic operations:

 -   `CREATE …​`
    
    -   `INSERT …​`
    
     -   `SELECT …​`
    
    -   `UPDATE …​`
    
    -   `DELETE …​`
    
     -   `…​`
     **Some Statement**
 - `CREATE TABLE 'registrants' ('id' INTEGER PRIMARY KEY, 'name' TEXT, 'dorm' TEXT)`
 - `INSERT INTO "registrants" ("id", "name", "dorm") VALUES(1, 'David', 'Matthews')`
 - `SELECT * FROM "registrants"`
 - `UPDATE "registrants" SET "name" = 'David Malan' where id = 1`
 - `DELETE FROM "registrants" WHERE id = 1` 
**Data Types**

 - -   `BLOB` stands for "binary large object", or binary data.
    
-   `INTEGER`
    
-   `NULL` is something we can use to specify that there is no value for a particular column, like in C.
    
-   `REAL` is a real number, or floating-point value.
    
-   `TEXT`
    
-   `DATETIME` stores dates and times.
    
-   `NUMERIC` stores numbers, whether they are integers or floating-point.

**Attributes**

-   `PRIMARY KEY`, where this column will be used to uniquely identify rows.
    
-   `UNIQUE` means that the field will be unique for every row, but not used to identify rows in joins.
    
-   `INDEX` means that we want the database to store the field in some index to speed up searches in the future, if we anticipate searching on that field frequently.
    
-   `NOT NULL` means that the field has to have some value, and can’t be blank.
    
-   `FOREIGN KEY` we’ll come back to again later, but means that it is referring to a row in some other table.

**lecture11_JavaScript Basic**

```
for (let value of array)
{
    ...
}

for (let key in object)
{
    ...
}
```

-    DOM, Document Object Model
- JSON, JavaScript Object Notation, is a format for storing data in a hierarchy
-  The technology that a browser uses to make requests dynamically is called **Ajax,** and it allows our browser to make additional special HTTP requests, after the initial one, to get more data from a server
- https://developers.google.com/maps/documentation/javascript/tutorial

