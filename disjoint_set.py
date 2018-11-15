# A Simple python 3 program to check
# if two sets are disjoint

# Returns true if set1[] and set2[] are disjoint, else false
def areDisjoint(set1, set2, m, n):
    # Take every element of set1[] and search it in set2
    for i in range(0, m):
        for j in range(0, n):
            if set1[i] == set2[j]:
                return False
            # If no element of set1 is present in set2
    return True


#         Driver program
set1 = [12, 34, 1, 11, 9, 3]
set2 = [7, 2, 1, 5]

m = len(set1)
n = len(set2)

print("Yup, they're disjoint right..." if areDisjoint(set1, set2, m, n) else "Nop, they're not disjoint...")

if __name__ == '__main__':
    areDisjoint(set1, set2, m, n)

# A shorter version

# Python3 program for isdisjoint() function

set1 = {2, 4, 5, 6}
set2 = {7, 8, 9, 10}
set3 = {1, 2}

# checking of disjoint of two sets
print("set1 and set2 are disjoint?", set1.isdisjoint(set2))

print("set1 and set3 are disjoint?", set1.isdisjoint(set3))


