def calculate(source, target):
    return recursive(source, len(source), target, len(target))


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
