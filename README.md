# brainfrick
BrainF*ck interpreter, but in python, but in 1 LOC :)

input scripts are stored in ./data/ as .bf files, only the recognized characters (listed in rules) are read in, everything else treated as comments (ie thrown out).

run the 'good' bf interpreter with
```
py ./main.py [filname]
```
1loc script for helloworld (in bf, interpreter by py) can be run with
```
py ./helloworld.py
```


## rules
```
> = increases memory pointer, or moves the pointer to the right 1 block.
< = decreases memory pointer, or moves the pointer to the left 1 block.
+ = increases value stored at the block pointed to by the memory pointer
- = decreases value stored at the block pointed to by the memory pointer
[ = like c while(cur_block_value != 0) loop.
] = if block currently pointed to's value is not zero, jump back to [
, = like c getchar(). input 1 character.
. = like c putchar(). print 1 character to the console
```