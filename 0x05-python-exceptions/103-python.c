#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        if (PyBytes_Check(item)) {
            printf("bytes\n");
            print_python_bytes(item);
        } else if (PyFloat_Check(item)) {
            printf("float\n");
            print_python_float(item);
        } else {
            printf("Unknown\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }
    Py_ssize_t size = PyBytes_Size(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %zd bytes: ", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < (size < 10 ? size : 10); i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] Invalid Float Object\n");
        return;
    }
    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
