/**
 * File name:
 *	13-insert_number.c
 * Description:
 * 	Inserts a number into sorted singly linked list
 * Author:
 * 	eu-dk3-t
 */

#include "lists.h"

/**
* Function name:
* 	insert_node 
* Description:
* 	Inserts a number into a sorted singly linked list
* @head: pointer to head node
* @number: value to be inserted
*
* Return: Address of new node 
* 	or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
