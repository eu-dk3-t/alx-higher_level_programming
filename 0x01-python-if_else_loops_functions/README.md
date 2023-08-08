# * 0x01-puthon-if_else_loops_functions

## - Scripts

### Note:
	Programs 0 and 1 are a completion of the following source code:
[Source code](https://github.com/alx-tools/0x01.py/tree/master)
#### * 0-positive_or_negative.py
#### * 1-last_digit.py

### Note:
	Programss 2 and 3 print the ASCII alphabet in lowercase
#### * 2-print_alphabet.py
#### * 3-print_alphabt.py

### * 4-print_hexa.py
	This program prints numbers from 0 to 98 in decimal and in hexadecimal
### * 5-print_comb2.py
	This program prints numbers from 0 to 99.
### * 6-print_comb3.py
	This program prints all possible different combinations of two digits.
### * 7-islower.py
	This function prints a string in lowercase followed by a new line.
### * 8-uppercase.py
	This function that prints a string in uppercase followed by a new line.
### * 9-print_last_digit.py
	This function prints the last digit of a number
### * 10-add.py
	This function adds two integers and returns the result.
### * 11-pow.py
	This function computes a raised to the power of b and returns the value.
### * 12-fizzbuzz.py
	Prints Fizz for multiples of 3 and Buzz for multiples of 5
### * 13-insert_number.c
	Inserts a node in a linked list at a given index
### * 100-print_tebahpla.py
	Prints the ASCII aplhabet in reverse, in uppercase and lowercase 
### * 101-remove_char_at.py
	Removes the character at the specified index
### * 102-magic_calculation.py
	Matches the following bytecode
##### * Bytecode

	  3           0 LOAD_FAST                0 (a)
        	      3 LOAD_FAST                1 (b)
	              6 COMPARE_OP               0 (<)
	              9 POP_JUMP_IF_FALSE       16

	  4          12 LOAD_FAST                2 (c)
	             15 RETURN_VALUE
	
	  5     >>   16 LOAD_FAST                2 (c)
	             19 LOAD_FAST                1 (b)
	             22 COMPARE_OP               4 (>)
	             25 POP_JUMP_IF_FALSE       36
	
	  6          28 LOAD_FAST                0 (a)
	             31 LOAD_FAST                1 (b)
	             34 BINARY_ADD
	             35 RETURN_VALUE

	  7     >>   36 LOAD_FAST                0 (a)
	             39 LOAD_FAST                1 (b)
	             42 BINARY_MULTIPLY
	             43 LOAD_FAST                2 (c)
	             46 BINARY_SUBTRACT
	             47 RETURN_VALUE
	
