'''Here We Are Using The map Method To find the
    double of each number entered by the user'''


def map_func(values):
    data = map(lambda x: x + x, values)
    return list(data)


sequence = map_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sequence)
