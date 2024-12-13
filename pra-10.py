class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):                                 
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

def is_operator(ch):
    return ch in ['+', '-', '*', '/', '^']

def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    for ch in expression:
        if ch.isalnum():  
            postfix.append(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()  
        elif is_operator(ch):
            while (not stack.is_empty() and precedence(ch) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(ch)

    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def evaluate_postfix(expression):
    stack = Stack()
    for ch in expression:
        if ch.isdigit():  
            stack.push(int(ch))
        elif is_operator(ch):
            op2 = stack.pop()
            op1 = stack.pop()
            if ch == '+':
                stack.push(op1 + op2)
            elif ch == '-':
                stack.push(op1 - op2)
            elif ch == '*':
                stack.push(op1 * op2)
            elif ch == '/':
                stack.push(op1 / op2)
            elif ch == '^':
                stack.push(op1 ** op2)
    return stack.pop()

infix_expr = "3+(2*4)^2-5"  
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix Expression:", postfix_expr)
result = evaluate_postfix(postfix_expr)
print("Evaluation Result:", result)