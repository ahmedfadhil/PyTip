import sys

# Find the second minimum element of an array
def main():
    """Finding the second smallest number"""
    numbers = [2, 112, 3, 55, 44, 33, 65, 23, 1]
    print("The array: ", numbers)

    first = sys.maxsize
    second = sys.maxsize

    for number in numbers:
        if number < first:
            second = first
            first = number
    print("First smallest number: ", first)
    print("Second smallest number: ", second)

    # # OR
    # print("first smallest", sorted(number)[0])
    # print("second smallest", sorted(number)[1])

main()

# First non-repeating integers in an array
some_string = "sadadad ddd lll seee ss nnn dd x"

print("The string is: ",some_string)

dict = {}

for st in some_string:
    if st.isalpha():
        if st in dict:
            dict[st]+=1
        else:
            dict[st]=1

first = next((x for x in dict if dict[x] == 1))
print("The first non repeating string:", first)
