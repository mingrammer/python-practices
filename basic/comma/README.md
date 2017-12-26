# Comma

This section introduces the useful tips of usage of **comma** in Python. Most pythonista may already knows the usages which are I will introduce.

There are three cases for using the comma in Python as followings:

* To use multiple values
* To use single value tuple
* To use as trailing comma

<br>

## Multiple values

This is a very natural feature of not only Python but also other languages as well. We can use multiple assignment and returns with commas.

```python
# Concurrent assignments and initializations
a, b = 1, 2

# Swap
a, b = b, a

# Returns multiple values
def add_and_mul(a, b):
    add = a + b
    mul = a * b
    return add, mul
```

<br>

## Single value tuple

Python has a special type called **tuple** which is immutable list-like container. A single value **list** can be defined with `[1]` form. But, in case of **tuple** , you can not create the single tuple by `(1)`. Because, Python would treat the `(1)` expression as just one integer value. So `(1)` is same to just  `1`.

Therefore, if you want to create single value tuple, you should use comma after the single value like this

```python
>>> type((1))
<class 'int'>
>>> type((1,))
<class 'tuple'>
```

So, where do we use this single vlaue tuple? Actually, there are some methods which take only tuple as their arguments. In some cases, you should pass the single value as tuple not multiple values. For example, the query executor method.

```python
# Throws a type error
execute_query('QUERY_STATEMENT', (1))

# Correct call
execute_query('QUERY_STATEMENT', (1,))
```

<br>

## Trailing comma

Above tips are kinds of just grammar features of Python. But It is more practical tips.

The **trailing comma** is a comma is located at after last value in a list as following.

```python
scores = [
    100,
    93,
    82,
    97,
]
```

In abov,e the comma of `97,` is the trailing comma. But, so, where do we use this trailing comma?

The purpose of this comma is that avoiding the mistakes and managing the source code on VCS (such as Git) easily.

<br>

### Avoiding the mistakes

As side effects, to avoid the human errors.

```python
scores = [
    100,
    93,
    82,
    97
    76
]
```

Imagine that if we want to add an additional score to existing scores list, a someone could make a mistake of forget of adding a comma. But, If you use trailing comma, it could reduce the mistakes. 

<br>

### For ease source code managing on VCS

This is main purpose of using the trailing comma. First, look at a case without trailing comma.

```python
names = [
    'James',
    'Smith',
    'Ming',
    'John'
]
```

And we will add a name to that list.

```python
names = [
    'James',
    'Smith',
    'Ming',
    'John',
    'Torvalds'
]
```

Done. there may no problems. But, see the `git diff` for that file.

```diff
@@ -2,5 +2,6 @@ names = [
     'James',
     'Smith',
     'Ming',
-    'John'
+    'John',
+    'Torvalds'
]
```

We just added an one data, but the diff tells us that there are one deleted data and two added data. Of course, it is not big problem, but it is not useful for tracing the commit history.

So, with trailing comma, we can solve that problems. Let's look at following example.

```python
names = [
    'James',
    'Smith',
    'Ming',
    'John',
]
```

And add a name to that list and see the `git diff` again.

```diff
@@ -3,4 +3,5 @@ mes = [
     'Smith',
     'Ming',
     'John',
+    'Torvalds',
 ]
```

Our intention was reflected to `diff` and we can see the only modified lines.