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
