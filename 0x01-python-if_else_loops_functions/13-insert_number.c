#include "lists.h"

/**
 * insert_node - inserts node in sorted list
 * @head: head node
 * @number: number to be inserted
 * Return: new head node
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;
	listint_t *tmp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	tmp = *head;
	while (tmp != NULL)
	{
		if (tmp->n <= number && (tmp->next == NULL || tmp->next->n >= number))
			break;
		tmp = tmp->next;
		i++;
	}
	tmp = *head;
	while (i != 0)
		tmp = tmp->next, i--;
	
	new->n = number, new->next = tmp ? tmp->next : NULL;
	if (*head == NULL)
		*head = new;
	else
		tmp->next = new;
	return (*head);
}
