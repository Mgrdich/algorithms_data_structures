# Stack Algorithm
A stack is a useful data structure in programming. It is just like a pile of plates kept on top of each other.

It follow LIFO Princiles ( Last In First Out )

### LIFO Principle of Stack
In programming terms, putting an item on top of the stack is called push and removing an item is called pop.


### Basic Operations of a Stack 

* `Push`  Add a new element to the top of the stack
* `Pop`  Remove an element form the top of the stack
* `IsFull`  Check if the stack is full
* `IsEmpty`  Check if the stack is Empty
* `Peek`  Get the value of the top element without removing it

### Data Structure Working principles
1. Before pushing, we check if the stack is already full
2. Before popping, we check if the stack is already empty
3. a pointer to keep track of the top element `pointer`
4. during initializing pointer is assigned to `pointer = -1`
5. On pushing an element, we increase `pointer` and place the new element in the position pointed to `pointer`.
6. On popping an element, we return the element pointed to by TOP and reduce its value.


