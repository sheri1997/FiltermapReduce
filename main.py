'''Here We Are Using The Filter Method To find the
    number of even numbers in the list inputted by the user'''


def filter_func(values):
    data = filter(lambda x: x % 2 == 0, values)
    return list(data)


sequence = filter_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sequence)
