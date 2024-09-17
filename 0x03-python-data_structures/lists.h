#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/* Definition of the listint_t structure */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Function prototypes */
listint_t *add_nodeint_end(listint_t **head, const int n);
size_t print_listint(const listint_t *h);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);  /* Corrected comment */

#endif /* LISTS_H */
