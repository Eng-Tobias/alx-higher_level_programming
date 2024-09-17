#include "lists.h"

/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the list.
 * Return: Pointer to the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
    listint_t *prev = NULL, *next = NULL;

    while (head)
    {
        next = head->next;
        head->next = prev;
        prev = head;
        head = next;
    }
    return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 * Return: 1 if it's a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *rev, *tmp;

    if (!*head || !(*head)->next)
        return (1);

    while (fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    rev = reverse_list(slow);
    tmp = rev;

    while (tmp)
    {
        if ((*head)->n != tmp->n)
        {
            reverse_list(rev);
            return (0);
        }
        *head = (*head)->next;
        tmp = tmp->next;
    }
    reverse_list(rev);
    return (1);
}
