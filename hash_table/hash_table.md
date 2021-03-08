# Hash Tables


The Hash table data structure stores elements in key-value pairs where

`Key` - unique integer that is used for indexing the values

`Value` - data that are associated with keys.



## Hashing (Hash Function)

In a hash table, a new index is processed using the keys. And, the element corresponding to that key is stored in the index. This process is called hashing.

Let `k` be a key and `h(x)` be a hash function.

Here, `h(k)` will give us a new index to store the element linked with `k`.



## Hash Collision

When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.

We can resolve the hash collision using one of the following techniques.


* Collision resolution by chaining
* Open Addressing: Linear/Quadratic Probing and Double Hashing


### Collision resolution by chaining

In chaining, if a hash function produces the same index for multiple elements, these elements are stored in the same index by using a doubly-linked list.

If `j` is the slot for multiple elements, it contains a pointer to the head of the list of elements. If no element is present, `j` contains `NIL`.


Pseudocode for operations

```
chainedHashSearch(T, k)
  return T[h(k)]
chainedHashInsert(T, x)
  T[h(x.key)] = x //insert at the head
chainedHashDelete(T, x)
  T[h(x.key)] = NIL
```

### Open Addressing

Unlike chaining, open addressing doesn't store multiple elements into the same slot. Here, each slot is either filled with a single key or left `NIL`.

Different techniques used in open addressing are:
### Linear Probing

In linear probing, collision is resolved by checking the next slot.

`h(k, i) = (h′(k) + i) mod m`

where

`i = {0, 1, ….}`
`h'(k)` is a new hash function

If a collision occurs at `h(k, 0)`, then `h(k, 1)` is checked. In this way, the value of `i` is incremented linearly.

The problem with linear probing is that a cluster of adjacent slots is filled. When inserting a new element, the entire cluster must be traversed. This adds to the time required to perform operations on the hash table.

### Quadratic Probing

It works similar to linear probing but the spacing between the slots is increased (greater than one) by using the following relation.

$h(k, i) = (h^′(k) + c_1i + c_2i^2) \mod m$

where,

`c1` and `c2` are positive auxiliary constants,
$i = {0, 1, ….}$

### Double hashing

If a collision occurs after applying a hash function h(k), then another hash function is calculated for finding the next slot.

$h(k, i) = (h_1(k) + ih_2(k)) \mod m$



## Ways to Create a good hash functions



A good hash function may not prevent the collisions completely however it can reduce the number of collisions.

Here, we will look into different methods to find a good hash function



### Division Method

If `k` is a key and `m` is the size of the hash table, the hash function `h()` is calculated as:

$h(k) = k \mod m$

For example, If the size of a hash table is `10` and `k = 112` then `h(k) = 112 mod 10 = 2`. The value of `m` must not be the powers of `2`. This is because the powers of `2` in binary format are `10, 100, 1000, ….` When we find `k mod m`, we will always get the lower order `p-bits`.


Generally, this approach is quite good for just about any value of M. However, in certain situations some extra care is needed in the selection of a suitable value for `m`.
For example, it is often convenient to make `m`an even number. But this means that h(x) is even if x is even; and `h(x)` is odd if `x` is odd. If all possible keys are equiprobable, 
then this is not a problem. However if, say, even keys are more likely than odd keys, the function tex2html_wrap_inline62256 will not spread the hashed values of those keys evenly.


For these reasons `M` is often chosen to be a prime number.
For example, suppose there is a bias in the way the keys are created that makes it more likely for a key to be a multiple of some small constant, say two or three. 
Then making `M` a prime increases the likelihood that those keys are spread out evenly. Also, if `M` is a prime number, the division of `x` by that prime number depends on all the bits of x, not just the bottom k bits, for some small constant `k`. 

```
if m = 22, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 01
if m = 23, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 001
if m = 24, k = 17, then h(k) = 17 mod 22 = 10001 mod 100 = 0001
if m = 2p, then h(k) = p lower bits of m
```


### Multiplication Method

$h(k) = ⌊m(kA  \mod 1 )⌋$

where,

`kA mod 1` gives the fractional part `kA`,
`⌊ ⌋` gives the floor value
 `A` is any constant. The value of `A` lies between `0` and `1`. But, an optimal choice will `be ≈ (√5-1)/2` suggested by Knuth.


### Universal Hashing


In Universal hashing, the hash function is chosen at random independent of keys.





