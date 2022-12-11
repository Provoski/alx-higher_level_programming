#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;
	int i;
	int x;
	listint_t *node_addr[MAX_NODES];

	temp = list;
	i = 0;
	while (temp != NULL)
	{
		node_addr[i] = temp;
		temp = temp->next;
		for (x = 0; x < i && x >= 0; x++)
		{
			if (temp == node_addr[x])
				return (1);
		}
		i++;
	}
	return (0);
}
