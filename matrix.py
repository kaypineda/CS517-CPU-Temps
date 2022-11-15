# Handles all matrix operations: creating, multiplying, solving

def transpose(original):
    transposed = [[]]

    for i,z in enumerate(original[0]):
        for j,y in enumerate(original):
            transposed[i][j] = original[j][i]

    return transposed


def multiply(lhs, rhs):
    result = []

    for i,z in enumerate(result):
        for j,y in enumerate(result[0]):
            for k,x in enumerate(lhs[0]):
                result[i][j] += lhs[i][k] * rhs[k][j]

    return result
