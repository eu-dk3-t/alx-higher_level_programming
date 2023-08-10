# * 0x02-python-import_modules

## - Scripts

### + 0-add.py
Imports the function add(a, b) from the file [`add_0.py`](https://github.com/eu-dk3-t/alx-higher_level_programming/blob/main/0x02-python-import_modules/add_0.py)
and prints the result.
### + 1-calculation.py
Imports functions from the file [`calculator_1.py`](https://github.com/eu-dk3-t/alx-higher_level_programming/blob/main/0x02-python-import_modules/calculator_1.py)
and performs some elementary arithmetic.
### + 2-args.py
Prints the number of and the list of its arguments
### + 3-infinite_add.py
Prints the result of the addition of all arguments
### + 4-hidden_discovery.py
Prints all the names defined by the compiled module [`hidden_4.pyc`](https://github.com/eu-dk3-t/alx-higher_level_programming/blob/main/0x02-python-import_modules/hidden_4.pyc)
### + 5-variable_load.py
Imports the variable `a` from the file 
[`variable_load_5.py`](https://github.com/eu-dk3-t/blob/main/alx-higher_level_programming/blob/main/0x02-python-import_modules/variable_load_5.py) and prints its value.
### + 100-my_calculator.py
Imports functions from [`calculator_1.py`](https://github.com/eu-dk3-t/alx-higher_level_programming/blob/main/0x02-python-import_modules/calculator_1.py) and performs all elementary operations.
### + 101-easy_print.py
Prints #pythoniscoll using the OS module and its methods
### + 102-magic_calculation.py
Matches the following bytecode:
#### Bytecode
	  3           0 LOAD_CONST               1 (0)
	              3 LOAD_CONST               2 (('add', 'sub'))
        	      6 IMPORT_NAME              0 (magic_calculation_102)
	              9 IMPORT_FROM              1 (add)
	             12 STORE_FAST               2 (add)
	             15 IMPORT_FROM              2 (sub)
	             18 STORE_FAST               3 (sub)
	             21 POP_TOP

	  4          22 LOAD_FAST                0 (a)
	             25 LOAD_FAST                1 (b)
	             28 COMPARE_OP               0 (<)
	             31 POP_JUMP_IF_FALSE       94

	  5          34 LOAD_FAST                2 (add)
	             37 LOAD_FAST                0 (a)
	             40 LOAD_FAST                1 (b)
	             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             46 STORE_FAST               4 (c)
	
	  6          49 SETUP_LOOP              38 (to 90)
	             52 LOAD_GLOBAL              3 (range)
	             55 LOAD_CONST               3 (4)
	             58 LOAD_CONST               4 (6)
	             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             64 GET_ITER
        	>>   65 FOR_ITER                21 (to 89)
	             68 STORE_FAST               5 (i)
	
	  7          71 LOAD_FAST                2 (add)
	             74 LOAD_FAST                4 (c)
	             77 LOAD_FAST                5 (i)
	             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	             83 STORE_FAST               4 (c)
        	     86 JUMP_ABSOLUTE           65
	        >>   89 POP_BLOCK
	
	  8     >>   90 LOAD_FAST                4 (c)
	             93 RETURN_VALUE
	
	 10     >>   94 LOAD_FAST                3 (sub)
	             97 LOAD_FAST                0 (a)
	            100 LOAD_FAST                1 (b)
	            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
	            106 RETURN_VALUE
	            107 LOAD_CONST               0 (None)
	            110 RETURN_VALUE

### + 103-fast_alphabet.py
Prints the alphabet in uppercase, by importing them from a module

