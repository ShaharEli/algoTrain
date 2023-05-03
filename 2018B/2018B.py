
def merge_helper(word1, word2, length, idx):
    if len(word1) == length:
        print("".join(word1))
        return
    curr = word2.pop(0)
    for i in range(idx, len(word1)+1):
        word1.insert(i, curr)
        merge_helper(word1, word2, length, i + 1)
        word1.pop(i)
    word2.insert(0, curr)


def merge(word1, word2):
    merge_helper(list(word1), list(word2), len(word2)+len(word1), 0)


# merge("abc", "12")

def check_pwds(req_list, pwd_list):
    lst = []
    for pwd in pwd_list:
        valid = True
        for req in req_list:
            valid2 = False
            for i in req:
                if i in pwd:
                    valid2 = True
                    break
            if not valid2:
                valid = False
                break

        if valid:
            lst.append(pwd)
    return lst


# print(check_pwds(["123", "abc", "$*%"], ["3a@*c", "a@*b%c", "1a$", "%%12"]))


def is_prime(i):
    if i == 2:
        return True
    if i < 2 or i % 2 == 0:
        return False
    for j in range(3, int(i**0.5) + 1, 2):
        if i % j == 0:
            return False
    return True


def get_next_prime(old_prime):
    i = old_prime+1
    while not is_prime(i):
        i += 1
    return i


def prime_components(n):
    if n == 1:
        return
    prime = 2
    while (n % prime) != 0:
        prime = get_next_prime(prime)
    yield prime
    yield from prime_components(n/prime)


# for i in prime_components(40):
    # print(i)

def find_pairs_helper(lst, start, end):
    mid = (start+end)//2
    if lst[mid] == "(" and lst[mid+1] == ")":
        return mid
    if lst[mid] == "(" and lst[mid+1] == "(":
        return find_pairs_helper(lst, mid+1, end)
    if lst[mid] == ")" and lst[mid+1] == ")":
        return find_pairs_helper(lst, start, mid-1)


def find_pairs(lst):
    return find_pairs_helper(lst, 0, len(lst)-1)


# print(find_pairs(["(", "(", ")", ")"]))
class Rect:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2


a = Rect([0, 0.5], [2, 2])
b = Rect([3, 1], [1, 3])
a.overlap_rect(b)
