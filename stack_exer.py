# Python program to evaluate value of a postfix expression

# Class to convert the expression


class Evaluate:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # Stack array
        self.array = []

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[-1]
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # The main function that converts given infix expression
    # to postfix expression
    def evaluatePostfix(self, exp):
        # Iterate over the expression for conversion
        for i in exp:
            # If the scanned character is an operand
            # (number here) push it to the stack
            if i.isdigit():
                self.push(i)
                # If the scanned character is an operator,
                # pop two elements from stack and apply it.
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val1 + i + val2)))
        return int(self.pop())


# Driver program to test above function
exp = "231*+9-4555+3"
obj = Evaluate(len(exp))

print("The postfix evaluation is: %d" % obj.evaluatePostfix(exp))


# Sort values in a stack

# Python program to sort a
# stack using auxiliary stack.
def sortStack(stack):
    tempStack = createStack()
    while isEmpty(stack) == False:
        temp = top(stack)
        pop(stack)
        while isEmpty(tempStack) == False and int(top(tempStack)) > int(temp):
            push(stack, tempStack)
            pop(tempStack)
        push(tempStack, temp)
    return tempStack


def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)


def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow ")
        exit(1)


def top(stack):
    p = len(stack)
    return stack[p - 1]


def printStack(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()


# Driver Code
stack = createStack()
push(stack, str(34))
push(stack, str(3))
push(stack, str(31))
push(stack, str(98))
push(stack, str(92))
push(stack, str(23))

print("Sorted numbers are: ")
sortedNumb = sortStack(stack)
print(sortedNumb)

# Stack parentheses balance check
from stacking import Stack


def is_match(picked, actual):
    # a lazy approach=> return True if picked + actual in ['()', '[]', '{}'] else False
    if picked == "(" and actual == ")":
        return True
    elif picked == "{" and actual == "}":
        return True
    elif picked == "[" and actual == "]":
        return True
    else:
        return False


def is_paren_balance(paren_string):
    stacked = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        parentheses = paren_string[index]
        if parentheses in "{([":
            stacked.push(parentheses)
        else:
            if stacked.is_empty():
                is_balanced = False
            else:
                top = stacked.pop()
                if not is_match(top, parentheses):
                    is_balanced = False
                index += 1
    if stacked.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balance("(])"))



