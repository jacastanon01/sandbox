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

# Defining the allergies
allergies = [
    "eggs",
    "peanuts",
    "shellfish",
    "strawberries",
    "tomatoes",
    "chocolate",
    "pollen",
    "cats",
]


class Allergies:
    def __init__(self, score) -> None:
        self.allergies = [
            allergin
            for i, allergin in enumerate(allergies)  # loop through allergies with index
            if score & (1 << i)  # shift 1 left i times and compare each bit to score
            # if any bit has a 1 in its place, it will be true and the allergy and
            # allergies[i] matches the new number derived from bitwise &
        ]

    def allergic_to(self, item) -> bool:
        return item in self.allergies

    @property
    def lst(self) -> list[str]:
        return self.allergies
