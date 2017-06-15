from math import sqrt
"""
List comprehension examples
"""
def basic_list_comprehension():
    # Make a list with even numbers up to 20
    evens = [x * 2 for x in range(11)]
    return evens


def basic_list_comprehension2():
    # Normalize the elements in a list and add a constant to those
    vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
    amount = sum(vals)
    norm_and_move = [(x / amount) + 1 for x in vals]
    return norm_and_move


def list_comprehension_with_conditions():
    # Find non-sqaure numbers up to 100
    non_squars = [x for x in range(101) if sqrt(x)**2 != x]
    return non_squars


def nested_list_comprehension():
    # Find all combinations of two lists
    epithets = ['sweet', 'annoying', 'cool', 'grey-eyed']
    names = ['john', 'alice', 'james']
    epithet_names = [(e, n) for e in epithets for n in names]
    return epithet_names


def find_pythagorean_solutions():
    # Find the solutions of Pythagorean triple positive integers
    # Where a^2 + b^2 = c^2 (a < b < c)
    solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
    return solutions


def remove_vowels_from_a_word():
    # Remove the vowels from a word
    word = 'mathematics'
    without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
    return without_vowels


def flatten_a_matrix():
    # Flatten a matrix
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    flatten = [e for r in matrix for e in r]
    return flatten


"""
Set comprehension examples
"""
def basic_set_comprehension():
    # Obtain the non-prime numbers without duplicate
    no_primes = {j for i in range(2, 9) for j in range(i * 2, 50, i)}
    return no_primes


"""
Dict comprehension examples
"""
def combine_two_list_to_dict():
    # Combine the two list to dict, where former is as key, and other is as value
    subjects = ['math', 'history', 'english', 'computer engineering']
    scores = [90, 80, 95, 100]
    score_dict = {key: value for key, value in zip(subjects, scores)}
    return score_dict


def transform_tuple_list_to_dict():
    # Transform the tuple list to dict form
    score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100)]
    score_dict = {t[0]: t[1] for t in score_tuples}
    return score_dict


"""
Generator expression examples
"""
def generate_square_numbers():
    # Make a generator to generate the square numbers
    gen = (x**2 for x in range(10))
    return gen


if __name__ == '__main__':
    # List comprehensions
    print(basic_list_comprehension())
    print(basic_list_comprehension2())
    print(list_comprehension_with_conditions())
    print(nested_list_comprehension())
    print(find_pythagorean_solutions())
    print(remove_vowels_from_a_word())
    print(flatten_a_matrix())

    # Set comprehensions
    print(basic_set_comprehension())

    # Dict comprehensions
    print(combine_two_list_to_dict())
    print(transform_tuple_list_to_dict())

    # Generator expressions
    gen = generate_square_numbers()
    print(gen)
    print(next(gen))
    print(next(gen))
    print(sum(gen))
