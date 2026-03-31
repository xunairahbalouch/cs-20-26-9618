class Stack:
    """Task 2.1 & 2.2: Stack implementation using a fixed-size array"""
    
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1
    
    def IsEmpty(self):
        """Task 2.1: Check if stack is empty"""
        return self.top == -1
    
    def IsFull(self):
        """Task 2.1: Check if stack is full"""
        return self.top == self.max_size - 1
    
    def Push(self, item):
        """Task 2.2: Push item onto stack"""
        if self.IsFull():
            print("Stack is full. Cannot push.")
            return False
        self.top += 1
        self.stack[self.top] = item
        return True
    
    def Pop(self):
        """Task 2.2: Remove and return top item"""
        if self.IsEmpty():
            print("Stack is empty. Cannot pop.")
            return None, False
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item, True
    
    def Peek(self):
        """Task 2.2: Return top item without removing"""
        if self.IsEmpty():
            return None
        return self.stack[self.top]
    
    def Display(self):
        """Task 2.2: Display all items in stack"""
        if self.IsEmpty():
            print("Stack is empty.")
            return
        print("Stack contents (top to bottom):")
        for i in range(self.top, -1, -1):
            print(f"  {self.stack[i]}")


def ValidateExpression(expression):
    """Task 2.3: Validate if brackets are balanced using stack"""
    stack = Stack(len(expression))
    opening = "([{"
    closing = ")]}"
    matching = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in opening:
            stack.Push(char)
        elif char in closing:
            if stack.IsEmpty():
                return False
            top, _ = stack.Pop()
            if top != matching[char]:
                return False
    
    return stack.IsEmpty()


def ReverseString(text):
    """Task 2.4: Reverse a string using stack"""
    stack = Stack(len(text))
    result = ""
    
    for char in text:
        stack.Push(char)
    
    while not stack.IsEmpty():
        char, success = stack.Pop()
        if success:
            result += char
    
    return result


def DecimalToBinary(decimal_num):
    """Task 2.5: Convert decimal to binary using stack"""
    if decimal_num == 0:
        return "0"
    
    stack = Stack(32)
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.Push(str(remainder))
        decimal_num //= 2
    
    binary = ""
    while not stack.IsEmpty():
        digit, _ = stack.Pop()
        binary += digit
    
    return binary


def EvaluatePostfix(expression):
    """Task 2.5: Evaluate postfix expression using stack"""
    stack = Stack(len(expression))
    operators = "+-*/"
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():
            stack.Push(int(token))
        elif token in operators:
            if stack.IsEmpty():
                return None
            b, _ = stack.Pop()
            if stack.IsEmpty():
                return None
            a, _ = stack.Pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    print("Division by zero")
                    return None
                result = a // b
            
            stack.Push(result)
        else:
            print(f"Unknown token: {token}")
            return None
    
    if stack.IsEmpty():
        return None
    result, _ = stack.Pop()
    return result


if __name__ == "__main__":
    print("=" * 80)
    print("Task 2.1 & 2.2: Stack Implementation")
    print("=" * 80)
    my_stack = Stack(10)
    
    print(f"Is empty: {my_stack.IsEmpty()}")
    print(f"Is full: {my_stack.IsFull()}")
    
    my_stack.Push(10)
    my_stack.Push(20)
    my_stack.Push(30)
    my_stack.Display()
    
    item, success = my_stack.Pop()
    print(f"Popped: {item}")
    my_stack.Display()
    
    print("\n" + "=" * 80)
    print("Task 2.3: Validate Brackets")
    print("=" * 80)
    test_expressions = [
        "(a + b)",
        "(a + b] * {c - d}",
        "((a + b) * (c - d))",
        "((a + b) * (c - d)",
    ]
    
    for expr in test_expressions:
        print(f"'{expr}' is balanced: {ValidateExpression(expr)}")
    
    print("\n" + "=" * 80)
    print("Task 2.4: Reverse String")
    print("=" * 80)
    test_strings = ["Hello", "Python", "Stack"]
    for s in test_strings:
        print(f"'{s}' reversed: {ReverseString(s)}")
    
    print("\n" + "=" * 80)
    print("Task 2.5: Decimal to Binary")
    print("=" * 80)
    test_numbers = [10, 15, 42, 255]
    for num in test_numbers:
        print(f"{num} in binary: {DecimalToBinary(num)}")
    
    print("\n" + "=" * 80)
    print("Task 2.5: Postfix Evaluation")
    print("=" * 80)
    postfix_expressions = [
        "3 4 +",
        "10 5 -",
        "3 4 * 2 +",
        "5 1 2 + 4 * + 3 -",
    ]
    
    for expr in postfix_expressions:
        result = EvaluatePostfix(expr)
        print(f"'{expr}' = {result}")
