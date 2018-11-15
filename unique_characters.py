

def is_unique(s):
    the_set = set(s)

    if len(s) == len(the_set):
        return True
    return False


s1 = "unqiue"
s2 = "bearing"

print(is_unique(s1))
print(is_unique(s2))