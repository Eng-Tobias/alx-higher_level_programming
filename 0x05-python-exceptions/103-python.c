#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[.] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

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
            print_python_float(item);
        }
        else if (PyLong_Check(item))
        {
            printf("int\n");
        }
        else
        {
            printf("unknown\n");
        }
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[.] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", str ? str : "None");

    if (size > 10)
        size = 10;

    printf("  first %zd bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[.] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
