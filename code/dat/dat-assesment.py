# decode txt
# read text.txt file
# each line in txt file contains a number and string, place these into a tuple pair
# construct a pyramid based on the number and
# return word matched to last value in pyramid
# pyramid is based on incrementing each row by 1
def decode(input_file):
    nums_set = set()
    words_list = []

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                num, word = line.split()
                words_list.append((int(num), word))

    words_list.sort(key=lambda x: x[0], reverse=True)

    bottom = len(words_list) - 1
    i = 0
    # start from the bottom and add numbers to set
    # i will represent the iteration and bottom will be the highest number in a row
    while bottom >= 0:
        current_num = words_list[bottom][0]
        nums_set.add(int(current_num))
        i += 1
        bottom -= (
            i + 1
        )  # Need to substract i + 1 because we are moving up the pyramid from the bottom

    return_str = " ".join([word for num, word in words_list[::-1] if num in nums_set])
    return return_str


print(decode("./small.txt"))
# print(decode("./text.txt"))
