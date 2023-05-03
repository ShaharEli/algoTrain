



def check(item, sett):
    if not isinstance(item, list):
        return
    if id(item) not in sett:
        sett.add(id(item))
        for i in item:
            check(i, sett)
