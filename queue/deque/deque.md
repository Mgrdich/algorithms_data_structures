# Deque 

Deque or Double Ended Queue is a type of queue in which insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow FIFO rule First In First Out.

Remeber all of this is being done by two pointers

Operations on a Deque

Below is the circular array implementation of deque. In a circular array, if the array is full, we start from the beginning.

But in a linear array implementation, if the array is full, no more elements can be inserted. In each of the operations below, if the array is full, "overflow message" is thrown.

Before performing the following operations, these steps are followed.

Take an array deque of size n.
Set two pointers at the first position and set `front = -1` and `rear = 0`.


### Insert at the Front
* Check the position of the Front
* if `front < 1` , reinitalize `front = n - 1` last index.
* Else , decrease `front` by `1`
* Add the new ket to `array[front]`


### Insert at the Rear
* Check if the array is full.
* if the deque is full reinitalize
* Else , decrease `rear` by `1`
* Add the new ket to `array[rear]`



### Delete from the Front
* Check if the deque is empty
* if the deque is empty i.e. `front = -1` deletting cannot be performed underflow
* if the deque has only one element `front = rear`, set `front = -1` and `rear = -1`
* Else if `front` is at the end `front = n - 1` set go the the front `front = 0`
* Else `front = front + 1`

### Delete from the End
* Check if the deque is empty
* if the deque is empty i.e. `front = -1` deletting cannot be performed underflow
* if the deque has only one element `front = rear`, set `front = -1` and `rear = -1`
* Else if `rear` is at the front `reat = 0` set go the the front `rear = n - 1`
* Else `rear = rear + 1`



### Check Empty
This operation checks if the deque is empty. If `front = -1`, the deque is empty.

### Check Full
This operation checks if the deque is full. If `front = 0` and `rear = n - 1` OR `front = rear + 1`, the deque is full.

