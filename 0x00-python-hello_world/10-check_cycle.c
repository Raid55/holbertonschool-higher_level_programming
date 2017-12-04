#include "lists.h"

/**
 *
 *
 *
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
