#include "lists.h"

/**
 * check_cycle - checks if linked list cycles
 * @list: list to be checked
 * Return: 1 or 0 depending on true or false
 */
int check_cycle(listint_t *list)
{
	listint_t *behind;
	listint_t *ahead;
	
	behind = list;
	ahead = list;	
	while (behind != NULL && ahead != NULL && ahead->next != NULL)
    {
        behind = behind->next, ahead = ahead->next->next;
        
		if (behind == ahead)
            return (1);
    }
	return (0);
}
