#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    tmpArr = [[1]]
    for x in range(n - 1):
        tmpArr.append(
            [f + n for f, n in zip(tmpArr[-1] + [0], [0] + tmpArr[-1])]
        )
    return tmpArr
