mixed_array = ["a", 10, "b", "hello", 122, 15]


def same_type_array(array, type):
    if not isinstance(array, list):
        raise TypeError("Variable must be an array!")

    filtered_items = [item for item in array if isinstance(item, type)]

    return filtered_items
