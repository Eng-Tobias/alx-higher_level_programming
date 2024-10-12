#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    const char *str = PyUnicode_AsUTF8(p);
    Py_ssize_t length = PyUnicode_GetLength(p);

    if (length < 0) {
        printf("[ERROR] Invalid String Length\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %zd\n", length);
    printf("  value: %s\n", str);
}
