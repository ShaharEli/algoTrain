

def binary_search(arr, val, start, end):
    if start == end:
        return end
    mid = (end + start)//2
    if (mid-1) >= 0 and arr[mid-1] < val and val <= arr[mid]:
        return mid
    if arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    if arr[mid] <= val:
        return binary_search(arr, val, mid+1, end)


def match(team1, team2):
    count = 0
    prev_idx = 0
    for teamate in team1:
        idx = binary_search(team2, teamate, prev_idx, len(team2))
        count += idx
        prev_idx = idx
    return count


def contains_all_of_helper(items, world, item_idx, world_idx):
    if len(items) == item_idx:
        return True
    if len(world)-1 == world_idx:
        if world[world_idx] == items[item_idx]:
            return contains_all_of_helper(items, world, item_idx+1, 0)
        return False
    if items[item_idx] == world[world_idx]:
        return contains_all_of_helper(items, world, item_idx+1, 0)
    return contains_all_of_helper(items, world, item_idx, world_idx+1)


def contains_all_of(items, world):
    return contains_all_of_helper(items, world, 0, 0)


def brute_search_helper(word, text, num, idx):
    if num == 0:
        return True
    if len(text) < (len(word)+idx):
        return False
    possible_word = text[idx:idx+len(word)]
    if possible_word == word:
        return brute_search_helper(word, text, num-1, idx+len(word))
    return brute_search_helper(word, text, num, idx+1)


def brute_search(word, text, num):
    return brute_search_helper(word, text, num, 0)


def iterable_to_function(iterable):
    def wrapper(n):
        the_iter = iter(iterable)
        for i in range(n-1):
            next(the_iter)
        return next(the_iter)
    return wrapper


# hi = iterable_to_function([1, 2, 3])
# print(hi(3))
class Car:
    licenses = set()

    def __init__(self, license_num):
        if Car.licenses.get(license_num):
            raise ValueError
        self.__license_num = license_num
        self.__original = license_num
        Car.licenses.add(license_num)

    def change(self, num):
        if Car.licenses.get(num):
            raise ValueError
        Car.licenses.add(self.__license_num)
        self.__license_num = license_num
        Car.licenses.add(license_num)

    def revert(self):
        self.change(self.__original)




