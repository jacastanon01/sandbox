# Problem: https://exercism.org/tracks/python/concepts/bitwise-operators

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
