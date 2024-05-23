even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

# for i in even:
#     print(f"{i} | 1 = {i | 1}")
#     print(f"{i} & 1 = {i & 1}")

# print('\n')
# for i in odd:
#     print(f"{i} | 1 = {i | 1}")
#     print(f"{i} & 1 = {i & 1}")

dict2 = {"a": 1, "b": 2, "c": 2}
dict3 = {"a": 1, "b": 5}

print("dict1 | dict2\nUnion", (dict2 | dict3), sep=": ")
# print("dict1 & dict2\nIntersection: ", (dict2 & dict2), sep=": ")
