def reverse_array(items):
    items_len = len(items) // 2
    print("Len: ", items_len)
    for i in range(items_len):
        print("Loop ", items[i], items[len(items) - i - 1])
        items[i], items[len(items) - i - 1] = items[len(items) - i - 1], items[i]
    return items

reverse_array([1,2,3,4])