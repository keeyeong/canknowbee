def calculate(source, target):
    # return recursive(source, len(source), target, len(target))
    return matrix(source, len(source), target, len(target))[0]


def recursive(source, source_size, target, target_size):
    if source_size == 0:
        return target_size
    if target_size == 0:
        return source_size
    if source[source_size - 1] == target[target_size - 1]:
        cost = 0
    else:
        cost = 1
    return min(recursive(source, source_size - 1, target, target_size) + 1,
               recursive(source, source_size, target, target_size - 1) + 1,
               recursive(source, source_size - 1, target, target_size - 1) + cost)


def matrix(source, source_size, target, target_size):
    result = [[0 for x in range(target_size + 1)] for y in range(source_size + 1)]

    for x in range(1, source_size + 1):
        result[x][0] = x

    for y in range(1, target_size + 1):
        result[0][y] = y

    for x in range(1, source_size + 1):
        for y in range(1, target_size + 1):
            if source[x - 1] == target[y - 1]:
                cost = 0
            else:
                cost = 1
            result[x][y] = min(result[x - 1][y] + 1,
                               result[x][y - 1] + 1,
                               result[x - 1][y - 1] + cost)

    return result[source_size][target_size], result
