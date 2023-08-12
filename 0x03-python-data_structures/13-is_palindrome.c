/**
 * File name:
 * 	13-is_palindrome.c
 * Description:
 * 	Determines if a linked list
 * 	contains a palindrome
 * Author:
 * 	eu-dk3-t
 */

#include "lists.h"

/**
 * Function name:
 * 	head_and_tails
 * Description:
 * 	Recursively checks if the head amd tail
 * 	are the same
 * NTK:
 * 	@head : Double pointer to head
 * 	@tail : Pointer to center of 
 * 	singly linked list
 * Return:
 * 	1 - Palindrome
 * 	0 - Not
 */
int head_and_tails(listint_t **head, listint_t *tail)
{
	if (tail->next)
	{
		if (head_and_tails(head, tail->next) == 0)
			return (0);
	}
	if ((*head)->n != tail->n)
		return (0);
	else
	{
		*head = (*head)->next;
		return (1);
	}
}
/**
 * Function name:
 * 	is_palindrome
 * Description:
 * 	Determines if a list is a
 * 	palindrome
 * NTK:
 * 	@head : Double pointer to the 
 * 	head of a linked list
 * Return:
 * 	1 -  Palindrome
 * 	0 - Not
 */

int is_palindrome(listint_t **head)
{
	listint_t *top_stack;

	if (head == NULL || *head == NULL)
		return (1);

	top_stack = *head;
	return (head_and_tails(&top_stack, *head));
}

