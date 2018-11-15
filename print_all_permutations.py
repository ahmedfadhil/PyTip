def toString(Lists):
    return "".join(Lists)


def permute(astring, starting, ending):
    if starting == ending:
        print(toString(astring))
    else:
        for i in range(1, ending + 1):
            astring[starting], astring[i] = astring[i], astring[starting]
            permute(astring, starting + 1, ending)
            astring[starting], astring[i] = astring[i], astring[starting]


# Driver code
string = "ABCD"
length = len(string)
astring = list(string)
permute(astring, 0, length - 1)
