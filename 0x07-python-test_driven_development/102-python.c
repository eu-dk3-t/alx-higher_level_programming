#include "Python.h"


/**
 * Function name:
 * 	print_python_string
 * Description:
 * 	Prints a python obj as a string and the first 10 bytes in hex
 * NTK:
 * 	@p: Pointer to a Python object.
 * Return:
 * 	Void.
 */
void print_python_string(PyObject *p)
{
	char *str;
	Py_ssize_t p_len;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		p_len = PyUnicode_GET_LENGTH(p);
		str = PyBytes_AsString(PyUnicode_AsUTF8String(p));
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n  value: %s\n", p_len, str);
	}
	else
		printf("  [ERROR] Invalid String Object\n");
	fflush(stdout);
}
