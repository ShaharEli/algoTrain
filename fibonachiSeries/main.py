
# def fib_finder():


def fib_series(n):
    if n == 0 or n == 1:
        return 1
    return fib_series(n-1) + fib_series(n-2)
