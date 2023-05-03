class Child:
    def __init__(self, name, mother=None, father=None):
        self.name = name
        self.mother = mother
        self.father = father


def generate_family_tree(a):
    if not a:
        return []
    return [a.name] + generate_family_tree(a.mother)+generate_family_tree(a.father)


def family_tree(a, b):
    a_tree = generate_family_tree(a)
    b_tree = generate_family_tree(b)
    for name in a_tree:
        if name in b_tree:
            return True
    return False


x = Child("Ety")
y = Child("Malka", x)
z = Child("Iosy", y, x)
u = Child("Ely", z)
v = Child("Avi")
print(family_tree(u, x))
print(family_tree(x, x))
print(family_tree(v, x))
