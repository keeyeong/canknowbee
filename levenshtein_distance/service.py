def calculate_distance_with_matrix(source, target):
    return calculate(source, len(source), target, len(target))


def calculate(source, source_size, target, target_size):
    # Initialize "2d matrix" with 0
    # One row/column extra for the length of source and target string (maximum possible distance)
    result = [[0 for x in range(target_size + 1)] for y in range(source_size + 1)]

    # max possible distance for every prefix is its length (replacing every character), up to whole source string length
    for x in range(1, source_size + 1):
        result[x][0] = x

    # max possible distance for every prefix is its length (replacing every character), up to whole target string length
    for y in range(1, target_size + 1):
        result[0][y] = y

    for x in range(1, source_size + 1):
        for y in range(1, target_size + 1):
            if source[x - 1] == target[y - 1]:
                cost = 0
            else:
                cost = 1
            result[x][y] = min(result[x - 1][y] + 1,  # by deleting the source string
                               result[x][y - 1] + 1,  # by inserting to the source string
                               result[x - 1][y - 1] + cost)  # by substitution (or not if same char at position)

    return result[source_size][target_size], result
