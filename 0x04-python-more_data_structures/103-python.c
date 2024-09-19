#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);

        printf("Element %zd: ", i);

        if (PyBytes_Check(item))
        {
            printf("bytes\n");
            print_python_bytes(item);
        }
        else if (PyFloat_Check(item))
        {
            printf("float\n");
        }
        else if (PyLong_Check(item))
        {
            printf("int\n");
        }
        else if (PyTuple_Check(item))
        {
            printf("tuple\n");
        }
        else if (PyList_Check(item))
        {
            printf("list\n");
        }
        else if (PyUnicode_Check(item))
        {
            printf("str\n");
        }
        else
        {
            printf("unknown\n");
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t i;
    Py_ssize_t size;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %zd bytes: ", (size < 10 ? size : 10));

    for (i = 0; i < (size < 10 ? size : 10); i++)
    {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
