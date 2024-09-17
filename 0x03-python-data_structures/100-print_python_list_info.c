#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: Python object (should be a list)
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;
    
    if (!PyList_Check(p))
    {
        PyErr_SetString(PyExc_TypeError, "Expected a list");
        return;
    }

    size = PyList_Size(p);
    allocated = PyList_GET_SIZE(p);  /* Size of the list */

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
