# Comprehension

The **comprehension** is an elegant way to define and create interable object in Python.

There are four kinds of comprehensions: **list**, **dict**, **set**, **generator**.

Let's look at each comprehension.

<br>

## List comprehension

**List comprehension** is a way to create list easily. This is a commonly used feature in Python. With this, you can create a list in a line with some conditions. 

First, let's see the basic example.

```python
# We want to make a list with even numbers up to 20
# We can create with this way
evens = [x * 2 for x in range(11)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# We want to normalize the elements in a list and add a constant to those
vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)
norm_and_move = [(x / amount) + 1 for x in vals]
# [1.0587155963302752, 1.0220183486238532, 1.1761467889908257, 1.0770642201834861, 1.0587155963302752, 1.1706422018348623, 1.0568807339449542, 1.0422018348623854, 1.1192660550458715, 1.0788990825688074, 1.1394495412844037]
```

More complex example. (conditions and nested one)

```python
# With conditions : Find non-sqaure numbers up to 100
from math import sqrt
non_squars = [x for x in range(101) if sqrt(x)**2 != x]
# [2, 3, 5, 6, 7, 8, 10, 12, 13, 15, 18, 19, 20, 23, 24, 26, 28, 29, 31, 32, 37, 38, 40, 43, 45, 48, 50, 51, 52, 58, 59, 60, 61, 63, 65, 66, 72, 73, 75, 76, 77, 78, 80, 82, 87, 89, 92, 94, 95, 96, 97]

# Nested list comprehension : Find all combinations of two lists
epithets = ['sweet', 'annoying', 'cool', 'grey-eyed']
names = ['john', 'alice', 'james']
epithet_names = [(e, n) for e in epithets for n in names]
# [('sweet', 'john'), ('sweet', 'alice'), ('sweet', 'james'), ('annoying', 'john'), ('annoying', 'alice'), ('annoying', 'james'), ('cool', 'john'), ('cool', 'alice'), ('cool', 'james'), ('grey-eyed', 'john'), ('grey-eyed', 'alice'), ('grey-eyed', 'james')]
```

More practical examples.

```python
# We want to find the solutions of Pythagorean triple positive integers
# That is, to find the solutions of a^2 + b^2 = c^2 (a < b < c)
solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
# [(3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15), (10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

# Remove the vowels from a word
word = 'mathematics'
without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
# 'mthmtcs'

# Flatten a matrix
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
flatten = [e for r in matrix for e in r]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

<br>

## Set comprehension

**Set comprehension** is exact same to list comprehension. But it create a set, not list.

Just do like this.

```python
# This list comprehension has duplicated elements
no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49, 16, 24, 32, 40, 48]

# With set comprehension, we can obtain the non-prime numbers without duplicate
no_primes = {j for i in range(2, 9) for j in range(i * 2, 50, i)}
# {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}
```

<br>

## Dict comprehension

**Dict comprehension** is also just like to list comprehension. But it create a dict, not list nor set.

Basic examples.

```python
# We want to combine the two list to dict, where former is as key, and other is as value
subjects = ['math', 'history', 'english', 'computer engineering']
scores = [90, 80, 95, 100]
score_dict = {key: value for key, value in zip(subjects, scores)}
# {'math': 90, 'history': 80, 'english': 95, 'computer engineering': 100}

# We also want to transform the tuple list to dict form.
score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100)]
score_dict = {t[0]: t[1] for t in score_tuples}
# {'math': 90, 'history': 80, 'english': 95, 'computer engineering': 100}
```

<br>

## Generator expression

**Generator expression** is a special comprehension form rather than above ones. This generates the **generator** which is an iterator returns a single value at a time, not returns all elements at once.

I will introducte the details of **generator** on other section, so I just focus on "expression" in here.

Generator expression is easy to use, which is same to other comprehensions.

```python
# This is a generator to yield square numbers
gen = (x**2 for x in range(10))
print(gen)
# <generator object <genexpr> at 0x105bde5c8>
print(next(gen)) # call 1
# 0
print(next(gen)) # call 2
# 1
# repeat the 'next' call up to 10 times
print(next(gen)) # call 10
# 81
print(next(gen)) # call 11
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""

# Yes, it is an just generator. You can sum the yielding values.
gen = (x**2 for x in range(10))
sum_of_squares = sum(gen)
# 285
```

