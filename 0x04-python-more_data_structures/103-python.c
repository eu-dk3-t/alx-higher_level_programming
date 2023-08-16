/**
 * File name:
 * 	103-python.c
 * Description:
 * 	Prints some basic info
 * 	about Py list
 * Author:
 * 	eu-dk3-t
 */

#include <Python.h>

/**
 * Function name:
 * 	print_python_list_info
 * Description:
 * 	Prints basic info about Python lists.
 * NTK:
 * 	@p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
/**
 * Function name:
 * 	print_python_bytes 
 * Description:
 * 	Prints basic info about Python byte objects.
 * NTK:
 * 	@p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
