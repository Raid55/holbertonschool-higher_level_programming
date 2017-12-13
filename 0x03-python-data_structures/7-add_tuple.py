def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = tuple_a + (0, 0)
    tup2 = tuple_b + (0, 0)
    tup1 = tup1[0:2]
    tup2 = tup2[0:2]
    return tuple(map(sum, zip(tup1, tup2)))
