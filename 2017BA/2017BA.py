from math import inf
import random  # you may use inf,-inf
BRACKETS = {
    '{': '}',
    '[': ']',
    '(': ')',
}


# def balanced_brackets(string):

# if not len(string):
#     return True
# if len(string) % 2 != 0:
#     return False
# if string[0] in brackets.values() or string[-1] in brackets.keys():
#     return False
# tail = string[0]
# closing_bracket = brackets.get(tail)
# for idx, elm in enumerate(string[1:]):
#     if elm == closing_bracket:
#         if balanced_brackets(
#                 string[1:idx+1]):
#             if balanced_brackets(string[idx+2:]):
#                 return True
# return False

def balanced_brackets(brackets):
    stack = []
    for bracket in brackets:
        if not stack:
            stack.append(bracket)
            continue
        prev = stack[-1]
        closing = BRACKETS[prev]
        if bracket == closing:
            stack.pop()
        else:
            stack.append(bracket)
    return len(stack) == 0


# print(balanced_brackets("([]{})"))
# print(balanced_brackets("([{})"))

class InfiniteSet:
    def __init__(self, f):
        self.f = f

    def __contains__(self, val):
        return self.f(val)

    def __iter__(self):
        i = 1
        while True:

            if self.f(i):
                yield i
            i += 1

    def __or__(self, other):
        return InfiniteSet(lambda x: other(x) or self.f(x))


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n*0.5)+1, 2):
        if n % i == 0:
            return False
    return True


# primes = InfiniteSet(isPrime)
# print(7 in primes)
# print([n for (i, n) in zip(range(5), primes)])
# new = primes | (lambda x: x % 3 == 0)

# print([n for (i, n) in zip(range(10), new)])


def matrix_multiply(m1, m2):
    multiplied = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            multiplied[i][j] = sum([m1[i][k]*m2[k][j]
                                   for k in range(len(m2))])
    return (multiplied)


# matrix_multiply([[1, 2]], [[3], [4]])
matrix_multiply([[3], [4]], [[1, 2]])
matrix_multiply([[1, 0, 0], [0, 1, 0]], [[1, 0], [0, 1], [0, 0]])


def fixed_point(f):
    def wrapper(start):
        prev = start
        curr = f(start)
        while prev != curr:
            prev = curr
            curr = f(curr)
        return curr

    return wrapper


def f(x): return (x-2)*(x-2)


# fp = fixed_point(f)
# print(fp(2))  # prints 4, because: 𝑓
def thresholdgen(threshold):
    while True:
        # An expensive action which returns a random int
        n = random.randint(1, 100)
        yield n, n >= threshold


class Learn:
    def __init__(self, gen):
        self.gen = gen
        self.low = -inf
        self.high = inf
        self.threshold = None

    def evaluate(self, n):
        if self.threshold:
            return n >= self.threshold
        curr = next(self.gen)
        while n > self.low and n < self.high:
            j, is_greater_threshold = curr
            if is_greater_threshold:
                self.high = min(j, self.high)
            else:
                self.low = max(j, self.low)
            curr = next(self.gen)
        if n >= self.high:
            return True
        if n <= self. low:
            return False

    def find_threshold(self):
        if self.threshold:
            return self.threshold
        curr = next(self.gen)
        while self.high != self.low+1:
            n, is_greater_threshold = curr
            if is_greater_threshold:
                self.high = min(n, self.high)
            else:
                self.low = max(n, self.low)
        self.threshold = self.high
        return self.high


gen = thresholdgen(7)
my_learner = Learn(gen)
print(

    my_learner.evaluate(8)
)
print(

    my_learner.evaluate(7))
print(

    my_learner.evaluate(6)
)

print(

    my_learner.find_threshold()
)
