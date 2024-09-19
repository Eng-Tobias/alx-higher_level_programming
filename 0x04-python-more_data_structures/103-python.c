#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t i;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            Py_ssize_t j;
            printf("[.] bytes object info\n");
            printf("  size: %zd\n", PyBytes_Size(item));
            printf("  trying string: %.100s\n", PyBytes_AsString(item));
            printf("  first %zd bytes: ", PyBytes_Size(item) > 10 ? 10 : PyBytes_Size(item));
            for (j = 0; j < (PyBytes_Size(item) > 10 ? 10 : PyBytes_Size(item)); j++) {
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            }
            printf("\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %.100s\n", PyBytes_AsString(p));
    printf("  first %zd bytes: ", size > 10 ? 10 : size);
    for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
