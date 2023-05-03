class Range2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __iter__(self):
        return (coord for coord in [(x, y) for x in range(self.__x) for y in range(self.__y)])


# hi = Range2D(3, 2)
# for x in hi:
#     print(x, end=" ")
# print()
# for x in hi:
#     print(x, end=" ")
# print()
# for x in hi:
#     print(x, end=" ")


def gen(n):
    curr = 1
    while curr != n+1:
        yield curr
        curr += 1


