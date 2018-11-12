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

print("The string is: ", some_string)

dict = {}

for st in some_string:
    if st.isalpha():
        if st in dict:
            dict[st] += 1
        else:
            dict[st] = 1

first = next((x for x in dict if dict[x] == 1))
print("The first non repeating string:", first)


# Merge two sorted arrays
class Solution:
    def mergeSortedArray(self, A, B):
        result = []
        indexA, indexB = 0, 0
        while indexA < len(A) and indexB < len(B):
            if A[indexA] < B[indexB]:
                result.append(A[indexA])
                indexA += 1
            else:
                result.append(B[indexB])
                indexB += 1

        #         Perhaps this part is not necessary
        if indexA < len(A):
            remaining = A[indexA]
        else:
            remaining = B[indexB]
        result.extend(remaining)

        return result


A = [1, 2, 3, 4, 5, 6]
B = [1, 2, 3, 4, 5, 6]
sorting = Solution()
sorting.mergeSortedArray(A, B)


# Python program to put positive numbers at even indexes (0, // 2, 4,..) and
# negative numbers at odd indexes (1, 3, 5, ..)

# The main function that rearranges elements of given array.
# It puts positive elements at even indexes (0, 2, ..) and
# negative numbers at odd indexes (1, 3, ..).
def rearrange(arr, n):
    # The following few lines are similar to partition process
    # of QuickSort. The idea is to consider 0 as pivot and
    # divide the array around it.
    i = -1
    for j in range(n):
        if (arr[j] < 0):
            i += 1
            # swapping of arr
            arr[i], arr[j] = arr[j], arr[i]

        # Now all positive numbers are at end and negative numbers
    # at the beginning of array. Initialize indexes for starting
    # point of positive and negative numbers to be swapped
    pos, neg = i + 1, 0

    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next
    # positive number
    while (pos < n and neg < pos and arr[neg] < 0):
        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2


# A utility function to print an array
def printArray(arr, n):
    for i in range(n):
        print(arr[i])

    # Driver program to test above functions


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)
printArray(arr, n)

# Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i

import array as a
import numpy as np


def rearranging(arr, n):
    # total even positions
    evenPos = int(n / 2)
    # total odd positions
    oddPos = n - evenPos

    # intialising empty array in python
    tempArr = np.empty(n, dtype=object)
    #     copy original array
    for i in range(0, n):
        tempArr[i] = arr[i]
    #       sort the auxiliary array
    tempArr.sort()
    j = oddPos - 1
    # fill up even positions in original
    # array
    for i in range(1, n, 2):
        arr[i] = tempArr[j]
        j = j + 1
        # display array

    for i in range(0, n):
        print(arr[i], end=' ')


# Driver code
arr = a.array('i', [1, 2, 3, 4, 5, 6, 7])
rearranging(arr, 7)


