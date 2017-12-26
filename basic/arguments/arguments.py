"""
Basic arguments examples
"""
def positional_arguments():
    # Add two numbers
    def add(a, b):
        return a + b
    return add(1, 2)


def with_keyword_arguments():
    def calculator(a, b, op='add', raise_err=True):
        # Select operator
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

    added = calculator(1, 2)
    subtracted = calculator(1, 2, op='sub')
    muliplied = calculator(1, 2, 'mul')
    undefeind = calculator(1, 2, raise_err=False, op='undefeind')
    return added, subtracted, muliplied, undefeind


"""
Variadic arguments examples
"""
def variadic_positional_arguments():
    # Use variadic positional arguments for accepting arbitrary numbers of values as list
    def add(*args):
        sum_of_nums = 0
        for num in args:
            sum_of_nums += num
        return sum_of_nums
    return add(1, 2, 3, 4, 5, 6)


def variadic_keyword_arguments():
    # Use variadic keyword arguments for accepting arbitrary numbers of values as dict
    def mean_calculator(**kwargs):
        subject_list = []
        sum_scores = 0
        for subject, score in kwargs.items():
            subject_list.append(subject)
            sum_scores += score
        mean = sum_scores / len(kwargs)
        print('The mean of subjects ({0}) is {1}'.format(', '.join(subject_list), mean))
        return mean

    mean = mean_calculator(
        math=100,
        english=90,
        history=95,
        chemistry=80,
        physics=85,
    )
    return mean


"""
Keyword only arguments examples
"""
def keyword_only_arguments():
    # An adder for adding three numbers has a keyword only argument
    def add(a, b, *, c=0):
        return a + b + c
    return add(1, 2, c=3)


if __name__ == '__main__':
    print(positional_arguments())
    print(with_keyword_arguments())
    print(variadic_positional_arguments())
    print(variadic_keyword_arguments())
    print(keyword_only_arguments())
