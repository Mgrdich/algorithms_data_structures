# Linked List

A linked list data structure includes a series of connected nodes. Here, each node store the data and the address of the next node. For example,

You have to start somewhere, so we give the address of the first node a special name called HEAD.

Also, the last node in the linked list can be identified because its next portion points to NULL.

You might have played the game Treasure Hunt, where each clue includes the information about the next clue. That is how the linked list operates.

## Representation of Linked List

Let's see how each node of the linked list is represented. Each node consists:

 A data item
 An address of another node

We wrap both the data item and the next node reference in a struct as:

```c
struct node
{
  int data;
  struct node *next;
};

```
Techincally struct is a crude thing for dictionary

Understanding the structure of a linked list node is the key to having a grasp on it.

Each struct node has a data item and a pointer to another struct node. Let us create a simple Linked List with three items to understand how this works.

```c
/* Initialize nodes */
struct node *head;
struct node *one = NULL;
struct node *two = NULL;
struct node *three = NULL;

/* Allocate memory */
one = malloc(sizeof(struct node));
two = malloc(sizeof(struct node));
three = malloc(sizeof(struct node));

/* Assign data values */
one->data = 1;
two->data = 2;
three->data=3;

/* Connect nodes */
one->next = two;
two->next = three;
three->next = NULL;

/* Save address of first node in head */
head = one
```
The power of a linked list comes from the ability to break the chain and rejoin it. E.g. if you wanted to put an element 4 between 1 and 2, the steps would be:

* Create a new struct node and allocate memory to it.
* Add its data value as 4
* Point its next pointer to the struct node containing 2 as the data value
* Change the next pointer of "1" to the node we just created.

Doing something similar in an array would have required shifting the positions of all the subsequent elements.


### Time Complexity

|  | Worst Case | Average case |
| --| -----------| ------------ |
| Search | `O(n)`| `O(n)` |
| Insert | `O(1)`| `O(1)` |
| Deletion | `O(1)`| `O(1)` |



## Operations

### Traverse a Linked List
Displaying the contents of a linked list is very simple. We keep moving the temp node to the next one and display its contents.
When temp is NULL, we know that we have reached the end of the linked list so we get out of the while loop.

```c
struct node *temp = head;
printf("\n\nList elements are - \n");
while(temp != NULL)
{
     printf("%d --->",temp->data);
     temp = temp->next;
}
```


### Insert and Element

You can add elements to either the beginning, middle or end of the linked list.


#### Insert at the beginning

* Allocate memory for new node
* Store data
* Change next of new node to point to head
* Change head to point to recently created node


#### Insert at the End

* Allocate memory for new node
* Store data
* Traverse to last node
* Change next of last node to recently created node


#### Insert at the Middle

* Allocate memory and store data for new node
* Traverse to node just before the required position of new node
* Change next pointers to include new node in between


### Delete from a Linked List

#### Delete from beginning

* Point head to the second node


#### Delete from end

* Traverse to second last element
* Change its next pointer to null


### Delete from middle

* Traverse to element before the element to be deleted
* Change next pointers to exclude the node from the chain

