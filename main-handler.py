mixed_array = ["a", 10, "b", "hello", 122, 15]


def same_type_array(array, type):
    if not isinstance(array, list):
        raise TypeError("Variable must be an array!")

    filtered_items = [item for item in array if isinstance(item, type)]

    return filtered_items


def largest_number(array):
    maxNum = max(array)
    return maxNum


def alg_handling(array):
    letters_array = same_type_array(array, str)
    numbers_array = same_type_array(array, int)
    max_number = largest_number(numbers_array)

    return [letters_array, numbers_array, max_number]


print(alg_handling(mixed_array))
