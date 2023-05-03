

from operator import le
from this import s


def function_power(f, n):
    def helper(f, v, n):
        if n == 1:
            return f(v)
        return f(helper(f, v, n-1))

    def wrapper(val):
        return helper(f, val, n)
    return wrapper


# def f(x): return 2*x


# g = function_power(f, 3)
# print(g(10))
d = {"yes": "oui", "good": "bien", "night": "nuit", "you": "toi"}


def language_language(t, d):
    inverse_d = {v: k for k, v in d.items()}
    len_t = len(t)
    en_count = 0
    fr_count = 0
    for item in t:
        if d.get(item):
            en_count += 1
        if inverse_d.get(item):
            fr_count += 1
    if en_count / len_t >= 0.7:
        return "ENGLISH"
    if fr_count / len_t >= 0.7:
        return "FRENCH"
    return "UNKNOWN"


def shrink(ls):
    new_ls = []
    curr_sum = 0
    current_sign = None
    for item in ls:
        if not current_sign:
            current_sign = 1 if item > 0 else -1
        if current_sign == 1 and item < 0:
            current_sign = -1
            new_ls.append(curr_sum)
            curr_sum = item
            continue
        if current_sign == -1 and item > 0:
            current_sign = 1
            new_ls.append(curr_sum)
            curr_sum = item
            continue
        curr_sum += item
    if curr_sum:
        new_ls.append(curr_sum)
    return new_ls


# print(shrink([2, 5, -3, -1, -1, 3, -2, -2]))
def set_power_helper(s, n, curr, arr):
    if len(curr) == n:
        arr.append(curr[:])
        return
    for x in s:
        curr.append(x)
        set_power_helper(s, n, curr, arr)
        curr.pop()


def set_power(s, n):
    arr = []
    set_power_helper(s, n, [], arr)
    return arr


class Residue_class:
    def __init__(self, deviser, reminder):
        self.__deviser = deviser
        self.__reminder = reminder
        self.__curr = 0

    def contains(self, x):
        if self.__deviser == 0:
            return False
        return (x % self.__deviser) == self.__reminder

    def __str__(self):
        return self.get_text_representation()

    def get_text_representation(self):
        arr = []
        curr = 1
        while len(arr) < 3:
            if self.contains(curr):
                arr.append(str(curr))
            curr += 1
        return f"{', '.join(arr)} ..."

    def __iter__(self):
        self.__curr += 1
        while True:
            if self.contains(self.__curr):
                yield self.__curr
            self.__curr += 1


odd = Residue_class(2, 1)
print(odd.contains(3))
print(odd)
c = 0
for i in odd:
    print(i)
    c += 1
    if c == 50:
        break
