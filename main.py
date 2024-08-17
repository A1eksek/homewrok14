def flatten(a_list: list, depth: int = 0) -> list:
    count = 0
    while True:
        result = []
        has_list = False
        for element in a_list:
            if type(element) is list:
                result.extend(element)
                has_list = True
            else:
                result.append(element)
        a_list = result
        count += 1
        if not has_list or (0 < depth == count):
            break
    return result
print(flatten([1, 2, [3, 4, [5, 6], 7], 8], 1))