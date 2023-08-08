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
* Return: address of new node or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *current = &head;
		listint_t *next = current->next;
		while (current->next != '\0')
		{
				if (next->n > number)
				{
						current->n = number;
						current->next = current->next;
						return (current);
				}
				current = current->next;
		}
		return (NULL);
}
