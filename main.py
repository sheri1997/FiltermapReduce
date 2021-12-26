'''Here We Are Using The reduce Method To find the
    sum and product of all the elements in the list'''
import functools
import operator


def reduce_func():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("sum of elements of the list : ")
    sum_values = (functools.reduce(operator.add, values))
    print(sum_values)
    print("Product of elements of the list : ")
    product_values = (functools.reduce(operator.mul, values))
    print(product_values)


sequence = reduce_func()
print(sequence)
