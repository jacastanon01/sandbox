def summation(*args):
    # print(args)
    return sum(args)


tuple_n = summation(1, 2, 3)
# list_n = summation([1, 2, 3])


def items(**kwargs):
    print(kwargs)
    result = ""
    for values in kwargs:
        result += values
    return result


list1 = {"A": 1, "B": 2, "C": 3}
list2 = {"D": 4, "E": 5, "F": 6}
l = [1, 2, 3]
s = [2, 3, 4]


print({**l, **s})

# print(items(a=1, b=2, c=3))
# print(dict(y.items()), {"D": 4})


def is_prime(n):
    if n == 0 or n == 1:
        return False

    abs_n = abs(n)
    for i in range(abs_n // 2, n + 1):
        if abs_n % i == 0:
            return False
    return True


print(is_prime(9))
print(is_prime(-4))
print(is_prime(8))
