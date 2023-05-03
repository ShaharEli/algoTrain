def most_common(lst):
    entries = {}
    entreis = {k: entries.get(k, 0)+1 for k in lst}
    maxx = 0
    val = ""
    for k, v in entreis.items():
        if v > maxx:
            maxx = v
            val = k
    return val
