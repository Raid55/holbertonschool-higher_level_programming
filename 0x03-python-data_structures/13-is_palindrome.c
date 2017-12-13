#include "lists.h"
/**
 * is_palindrome - checks if linked list is palindrone
 * @head: head of list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *start;
	int *holder;
	int i = 0, len = 0;
	
	start = *head;

	while (start != NULL)
		len++, start = start->next;

	holder = malloc(sizeof(int) * (len));
	if (holder == NULL)
		return (0);

	i = 0, start = *head;
	while (start != NULL)
		holder[i++] = start->n, start = start->next;

	/* i = 0; */
	/* while (holder[i]) */
		/* printf("%d", holder[i++]->n); */
	i = 0, len--;
	while (holder[i] == holder[len])
	{
		if (i == len || i > len)
		{
			free(holder);
			return (1);
		}
		i++, len--;
	}
	free(holder);
	return (0);
}
