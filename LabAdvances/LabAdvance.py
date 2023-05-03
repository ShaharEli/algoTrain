from math import sqrt


def get_y(a, b, x):
    return a*x+b


def geom_prob(x1, y1, x2, y2, a, b):
    start = get_y(a, b, x1)
    end = get_y(a, b, x2)
    if start == y1 or end == y2:
        return True
    if a > 0 and start > y2:
        return False
    if a < 0 and start < y1:
        return False
    if a > 0 and end < y1:
        return False
    if a < 0 and end > y1:
        return False
    if a == 0:
        return b == x1 or b == x2
    return True


def create_arr_from_idexs(letters, idexs):
    return [letters[idexs[i-1]:idexs[i]] for i in range(1, len(idexs))] + [letters[idexs[-1]:]]


def all_the_to_cut(letters, num_words):
    if num_words == 1:
        return [letters]
    arr = []
    starting_indexes = [i for i in range(num_words)]
    curr_idex = starting_indexes[:]
    while curr_idex[-1] < len(letters):
        arr.append(create_arr_from_idexs(letters, curr_idex))
        for i in list(range(1, len(starting_indexes)-1))[::-1]:
            while curr_idex[i] < curr_idex[i+1]-1:
                curr_idex[i] += 1
                arr.append(create_arr_from_idexs(letters, curr_idex))
                for j in list(range(1, i))[::-1]:
                    if i == j:
                        continue
                    while curr_idex[j] < curr_idex[j+1]-1:
                        curr_idex[j] += 1
                        arr.append(create_arr_from_idexs(
                            letters, curr_idex))
                    curr_idex[j] = starting_indexes[j]
            curr_idex[i] = starting_indexes[i]
        curr_idex[-1] += 1
    return arr


# count_sp_ways(x,n,starter):

# def all_ways_to_cut(x,n):
#     arr = []
#     root = int(sqrt(x))
#     count +=

#     return count
def count_sp_ways_helper(start, x, n):
    if x < 0:
        return 0
    if start == 0:
        if x:
            return 0
        return 1
    return count_sp_ways_helper(start-1, x, n) + count_sp_ways_helper(start-1, x-(start**n), n)


def count_sp_ways(x, n):
    root = int(sqrt(x))
    return count_sp_ways_helper(root, x, n)


print(
    count_sp_ways(2, 2))


def num_different_permutations_helper(word, curr, all_word):
    s = 0
    if len(curr) == len(all_word):
        s += 1
    for lett in word:
        if curr.count(lett) < all_word.count(lett):
            curr += lett
            s += num_different_permutations_helper(word, curr, all_word)
            curr = curr[:-1]
    return s


def num_different_permutations(word):
    return num_different_permutations_helper("".join(set(word)), "", word)
