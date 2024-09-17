#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: Double pointer to the head of the list.
 * @n: The integer to be added.
 * Return: Address of the new element, or NULL if it failed.
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new_node, *temp;

    new_node = malloc(sizeof(listint_t));
    if (!new_node)
        return (NULL);

    new_node->n = n;
    new_node->next = NULL;

    if (!*head)
    {
        *head = new_node;
        return (new_node);
    }

    temp = *head;
    while (temp->next)
        temp = temp->next;

    temp->next = new_node;
    return (new_node);
}

/**
 * print_listint - Prints all the elements of a listint_t list.
 * @h: Pointer to the head of the list.
 * Return: The number of nodes.
 */
size_t print_listint(const listint_t *h)
{
    size_t count = 0;

    while (h)
    {
        printf("%d\n", h->n);
        h = h->next;
        count++;
    }
    return (count);
}

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the list to be freed.
 */
void free_listint(listint_t *head)
{
    listint_t *temp;

    while (head)
    {
        temp = head->next;
        free(head);
        head = temp;
    }
}
