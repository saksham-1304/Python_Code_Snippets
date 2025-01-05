# Genrator Function


def count_up_to(n):
    """
    Generates numbers up to n
    """
    i = 0
    while i < n:
        yield i
        i += 1


# Using a generator function
counter = count_up_to(5)
for num in counter:
    print(num)
