

def check(f):
    s = {"initialized": False, "maxxes": [], "count": 0}

    def wrapper(n):
        if not s["initialized"]:
            s["args"] = n
            s["initialized"] = True

        def helper():
            s["count"] += 1
            return f(n)
        hi = helper()
        s["maxxes"].append(s["count"])
        s["count"] = 0
        maxx = max(s["maxxes"])
        if s["args"] == n:
            s["args"] = 0
            s["maxxes"] = []
            s["count"] = 0
            s["initialized"] = False
            return hi,  maxx
        return hi
    return wrapper


@ check
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)


# print(
#     fib(7)


# )


# print(
#     fib(3)

# )

def decode_helper(codebook, cipher, subs, curr, start, end, arr):
    if start == end:
        subs_str = "".join(subs)
        if subs_str in codebook:
            curr += [codebook[subs_str]]
            subs = []
        if subs:
            return
        arr.append(" ".join(curr))
        return
    tail = cipher[start]
    subs_str = "".join(subs)
    if subs_str in codebook:
        decode_helper(codebook, cipher, [tail], curr +
                      [codebook[subs_str]], start+1, end, arr)
    subs.append(tail)
    decode_helper(codebook, cipher, subs, curr, start+1, end, arr)
    subs.pop()


def decode(codebook, cipher):
    arr = []
    decode_helper(codebook, cipher, [], [], 0, len(cipher), arr)
    return arr


cipher = "abcdefghij"
codebook = {"hij": "lied", "ab": "hide", "cdef": "your", "efg": "secrets", "abcd": "old",
            "xyz": "submarine", "efghij": "spies", "ghij": "messages", "abz": "rocket"}
print(
    decode(codebook, cipher)
)
