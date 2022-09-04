from .data_translations import int_list


def surface_area(a):
    [x, y, z] = int_list(a)
    return 2*x*y + 2*x*z + 2*y*z


def area(a):
    res = 1
    for i in int_list(a):
        res = res * i
    return res


def perimeter(a):
    return sum([2*i for i in int_list(a)])


def volume(a):
    [x, y, z] = int_list(a)
    return x*y*z


def manhattan_distance(a, b):
    return abs(a) + abs(b)


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def is_even(i):
    return i % 2 == 0
