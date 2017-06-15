# Arguments

This section covers **arguments** of Python. Python has special types of argument compared to other languages and there are new concepts of **packing** and **unpacking**.

Before, deep dive into such special arguments, let's look at basic arguments first.

<br>

## Basic arguments

Most of you may know this basic concept if you are a Python programmer. It is very basic, more detail explains are not needed I think.

```python
# We want to make a adder for two numbers
def add(a, b):
    return a + b

added = add(1, 2)
# 3
```

You can just declare the arguments in definition of a function. This kinds of arguments are called **positional arguments**.

Also, Python has another type of argument which is called **keyword arguments**. You may have seen these arguments in many projects or your source code.

With keyword arguments, you can set **default** value of a argument.

Let's look at keyword arguments.

```python
# This is a simple calculator
def calculator(a, b, op='add', raise_err=True):
    if op == 'add':
        return a + b
    if op == 'sub':
        return a - b
    if op == 'mul':
        return a * b
    if op == 'div':
        return a / b
   	if raise_err:
    	raise ValueError('Not supported errors')
        
# The function use default value if we do not pass the keyword argument
added = calculator(1, 2)
# 3

# If you want to use 'subtract' operator
subtracted = calculator(1, 2, op='sub')
# -1

# The basic keyword arguments can be treated as position arguments corresponding to their positions
muliplied = calculator(1, 2, 'mul')
# 2

# The keyword arguments do not care about their positions. But if you change the keyword arguments, you can not omit the keyword keys
undefeind = calculator(1, 2, raise_err=False, op='undefeind')
# None
```

The keyword argument is a very useful feature of Python. With this, you can use the arguments dynaimcally. 

*You have to keep in mind that the keyword arguments must be located after positional arguments.*

<br>

## Variadic arguments

Python also supports the **variadic argument** which does not have fixed length. We often need variadic arguments (or parameters) for some functions. For example, we need it if we don’t know number of passing arguments or when we should process something with arbitrary passing arguments for some reasons.

Imagine that we should make an adder to sum the passed numbers. (Of course, Python provides the **sum** function for this job, but, in here, we will implement that function ourselves)

```python
# An adder for adding two numbers
def add(a, b):
    return a + b

# An adder for adding three numbers
def add(a, b, c)
	return a + b + c

# And so on ... But how do we handle the 4, 5 and 6 numbers?
# An adder for adding arbitrary numbers of numberss
def add(*args):
    sum_of_nums = 0
    for num in args:
        sum_of_nums += num
    return sum_of_nums

# Pass the artitrary numbers of numbers
sum_of_nums = add(1, 2, 3, 4, 5, 6)
# 21
```

In above, the `*args` can accept the arbitrary numbers of values. In here, the `*args` is called **packing**. The arguments passed as positional are stored in a *list* called `args`

Like packing for list, there is also packing for dict for variadic keyword arguments.

```python
# A score mean calculator
def mean_calculator(**kwargs):
    subject_list = []
    sum_scores = 0
    for subject, score in kwargs.items():
        subject_list.append(subject)
        sum_scores += score
    mean = sum_scores / len(kwargs)
    print('The mean of subjects ({0}) is {1}'.format(', '.join(subject_list), mean))
    return mean

# Pass the arbitrary numbers of key-value entries
mean = mean_calculator(
    math=100,
    english=90,
    history=95,
    chemistry=80,
    physics=85,
)
# The mean of subjects (chemistry, history, physics, math, english) is 90
```

You can also use the both positional and keyword arguments at once. But, as refered before, the keyword arguments can not be declared before positional arguments, so following code would raises exceptions.

```python
# Allowed
def some_function(*args, **kwargs):
    pass

# Allowed
def some_function(pos, *args, kv=None, **kwargs):
	pass

# Not allowed
def some_function(**kwargs, *args):
	pass
```

The **variadic argument** is very often used feature, it could be seen on many open source projects. Usually, many open sources use typically used argument names such as `*args` or `**kwargs` as variadic arguments name. But, of course, you can also use the own name for it like `*required` or `**optional`. (However, if your project is open source and there is no special meaning at variadic arguments, it is good to follow conventions of using `*args` and `**kwarg`)

<br>

## Keyword only arguments

In above, we noticed that the keyword arguments can be acted as positional arguments. But, if we want to allow to use those as keyword only arguments, how achieve it? Just like this.

```python
# An adder for adding three numbers
def add(a, b, *, c=0):
    return a + b + c

# Correct usage
added = add(1, 2, c=3)
# 6

# This raises an exception
added = add(1, 2, 3)
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 2 positional arguments but 3 were given
"""
```

