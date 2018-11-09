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
def isEmpty(stack):
    pass


def pop(stack):
    pass


def top(stack):
    pass


def push(stack, param):
    pass


def sortStack(stack):
    tempStack = createStack()
    while isEmpty(stack) == False:
        temp = top(stack)
        pop(stack)
        while isEmpty(tempStack) == False and int(top(tempStack)) > int(temp):
            push(stack, top(tempStack))
            pop(tempStack)


def createStack():
    stack = []
    return stack
