/**
 * File name:
 * 	10-check_cycle.c
 * Description:
 * 	Checks of a linked list 
 * 	contains a cycle
 * Author:
 * 	eu-dk3-t
 */

#include "lists.h"

/**
 * Function name:
 * 	check_cycle
 * Description:
 * 	Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 - If there is no cycle
 *         1- If there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current_i, *next_i;

	if (list == NULL || list->next == NULL)
		return (0);

	current_i = list->next;
	next_i = list->next->next;

	while (current_i && next_i && next_i->next)
	{
		if (current_i == next_i)
			return (1);

		current_i = current_i->next;
		next_i = next_i->next->next;
	}

	return (0);
}
