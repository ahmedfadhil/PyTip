from queue import Queue


# Python program to generate binary numbers from
# 1 to n

# This function uses queu data structure to print binary numbers

def generatePrintBinary(n):
    queue = Queue()
    queue.put("1")
    while n > 0:
        n -= 1
        s1 = queue.get()
        print(s1)
        s2 = s1
        queue.put(s1 + "0")
        queue.put(s2 + "1")


# Driver program
n = 20

generator = generatePrintBinary(n)

