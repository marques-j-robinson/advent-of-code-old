def leading_zero(n):
    return str(n).zfill(2)


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]
