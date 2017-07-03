# List

**List** is very powerful and may most used data structure in Python.

When you want to hold the sequential data, should use it for that. In Python, the using of list is very very easy and intuitive. This section covers the following topics for list.

* List basic
* List methods
* List operations
* Nested list
* List comprehension
* Using as stack
* Using as queue

Let's explore the list world.

<br>

## List basic

Quick examples.

```python
# Declare the empty list in two ways
empty = []
empty = list()

# Declare and initialize the list in two ways
numbers = [1, 2, 3]
numbers = list([1, 2, 3])

# Add an element to above lists
empty.append(1)
numbers.append(4)
# empty: [1]
# numbers: [1, 2, 3, 4]

# You can add any type of data to list
empty.append('string')
numbers.append(False)
# empty: [1, 'string']
# numbers: [1, 2, 3, 4, False]
```

<br>

## List methods

There are some useful methods to handle the list easily. Here is a list of methods:

* **append**(object) → None: Append an item to end of a list
* **extend**(iterable) → None: Extend list by appending elements from the iterable
* **clear**() → None : Remove all items in a list
* **count**(value) → integer: Return the number of occurrences of value in a list
* **index**(value, [start, [stop]]) → integer: Return first index of value
* **insert**(index, object): Insert object before index
* **pop**([index]) → item: Remove and return item at index (default: last)
* **remove**(value) → None: Remove first occurrence of value
* **reverse**(): Reverse the list
* **sort**(key=None, reverse=False) → None: Stable sort the list 
* **copy**() → list: Return a shallow copy of a list

<br>

What is difference between `append` abd `extend`?

#### append

```python
numbers = [1, 2, 3]
numbers.append(4)
# numbers: [1, 2, 3, 4]

numbers.append([5, 6])
# numbers: [1, 2, 3, 4, [5, 6]]
```

#### extend

```python
### extend
numbers = [1, 2, 3]
numbers.extend(4)
# numbers: [1, 2, 3, 4]

numbers.extend([5, 6])
# numbers: [1, 2, 3, 4, 5, 6]
```

The `extend` method appends the all values of added list one by one, but `append` just adds the value as one object.

Continue looking remaining methods.

#### clear

```python
numbers = [1, 2, 3]
numbers.clear()
# numbers: []
```

#### count

```python
numbers = [1, 1, 1, 2, 2, 3]
print(numbers.count(2))
# 2
print(numbers.count(4))
# 0
```

#### index

```python
# The 'start' is included, but the 'stop' is excluded
numbers = [1, 2, 1, 2, 3, 4, 2]
print(numbers.index(1)) # on [1, 2, 1, 2, 3, 4, 2]
# 0
print(numbers.index(1, 1)) # on [X, 2, 1, 2, 3, 4, 2]
# 2
print(numbers.index(2, 1)) # on [X, 2, 1, 2, 3, 4, 2]
# 1
print(numbers.index(2, 4, 6)) # on [X, X, X, X, 3, 4, X]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: 2 is not in list
```

#### insert

```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 6)
# numbers: [1, 2, 6, 3, 4, 5]
```

#### pop

```python
numbers = [1, 2, 3, 4, 5]
print(numbers.pop())
# 5
print(numbers.pop(0))
# 1
```

#### remove

```python
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
# numbers: [1, 2, 4, 5]
numbers.remove(6)
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ValueError: list.remove(x): x not in list
```

#### reverse

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
# numbers: [5, 4, 3, 2, 1]
```

#### sort

```python
numbers = [6, 1, 3, 2, 5, 4]
numbers.sort()
# numbers: [1, 2, 3, 4, 5, 6]
numbers.sort(reverse=True)
# numbers: [6, 5, 4, 3, 2, 1]

# Sort by custom order
numbers = [(0, 6), (3, 1), (2, 3), (4, 2), (100, 5), (-1, 4)]
numbers.sort(key=lambda e: e[1]) # sort by value of second element of tuples in the list
# numbers: [(3, 1), (4, 2), (2, 3), (-1, 4), (100, 5), (0, 6)]
numbers.sort(key=lambda e: e[0] + e[1]) # sort by sum of elements of tuples in the list
# numbers: [(-1, 4), (3, 1), (2, 3), (4, 2), (0, 6), (100, 5)]
```

#### copy

```python
numbers = [1, 2, 3]
copied = numbers.copy()
copied.append(4)
# numbers: [1, 2, 3]
# copied: [1, 2, 3, 4]
```

<br>

## List operations

There are some available operations for handling the list.

The **slicing** is to slice the list with an interval and step you want.

```python
# Slicing format: list[first index:last index:step]
# The first index is included, but last index is excluded
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[:])
# [1, 2, 3, 4, 5, 6]
print(numbers[2:])
# [3, 4, 5, 6]
print(numbers[1:4])
# [2, 3, 4]
print(numbers[1:6:2])
# [2, 4, 6]
```

You can also use the **+** and **\*** for list type as following:

```python
# The + operator can be used to 'extend' a list
arr = [1, 2]
arr += [3, 4]
# arr: [1, 2, 3, 4]

# The * operator can extend the list with multiplying as many as times by given number
arr = [1, 2, 3]
arr *= 2
# arr: [1, 2, 3, 1, 2, 3]
```

Here are other operations.

```python
# Make a new sorted list
arr = [4, 1, 3, 2]
sorted_arr = sorted(arr) # 'sorted' has same keyword parameters to 'sort' method

# Find the length of a list
print(len(arr))
# 4

# Convert the string list to a single string with a delimiter
fruits = ', '.join(['apple', 'pear', 'banana', 'kiwi'])
# fruits: 'apple, pear, banana, kiwi'

# Find the maximum or minimum value of a list
max(arr)
# 4
min(arr)
# 1

# Find the sum of values of a list
sum(arr)
# 10

# Remove a specific index or interval in a list
del arr[3]
# arr: [4, 1, 3]
del arr[1:]
# arr: [4]
```

<br>

## Nested list

List can be nested and you can use it to build a dimensional structure like matrix (2-D list)

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
matrix[0]
# [1, 2, 3, 4]
matrix[1][2]
# 7

# Transpose the matrix
for i in range(len(matrix)):
    for j in range(i, len(matrix[i])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# matrix: [
#     [1, 5, 9, 13],
#     [2, 6, 10, 14],
#     [3, 7, 11, 15],
#     [4, 8, 12, 16],
# ]
```

<br>

## List comprehension

See it [here](/basics/comprehension)

<br>

## Using as stack

You can use the list as stack data structure like this simply:

```python
stack = [7, 1, 4, 3]
stack.pop()
# 3
# stack: [7, 1, 4]
stack.pop()
# 4
# stack: [7, 1]
stack.append(5)
# stack: [7, 1, 5]
stack[-1] # Refers to the top of stack
# 5
```

<br>

## Using as queue

You can use the list as queue data structure like this simply:

```python
queue = [1, 6, 4, 3]
queue.append(2)
# queue: [1, 6, 4, 3, 2]
queue.append(7)
# queue: [1, 6, 4, 3, 2, 7]
queue.pop(0)
# 1
# queue: [6, 4, 3, 2, 7]
```



