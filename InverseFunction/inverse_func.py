def inverse_func(f, n):
    d = {f(i): i for i in range(n)}

    def wrapper(k):
        return d[k]

    return wrapper


def f(x): return (x+1) % 7


g = inverse_func(f, 7)
print(g(3))
