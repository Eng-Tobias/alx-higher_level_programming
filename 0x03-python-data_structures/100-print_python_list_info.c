#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    Py_ssize_t size, allocated, i;
    PyObject *item;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyObject\n");
        return;
    }

    size = PyList_Size(p);
    allocated = Py_SIZE(p);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

