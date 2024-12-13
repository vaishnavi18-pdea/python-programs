class STACK:
    def __init__(self):
        self.stack = []
    def push(self, char):
        self.stack.append(char)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0
    def reverse(self):
        reversed_string = ""
        while not self.is_empty():
            reversed_string += self.pop()
        return reversed_string
    
def preprocess_string(input_string):
    processed_string = ''.join(char.lower() for char in input_string if char.isalnum())
    return processed_string

def is_palindrome(input_string):
    stack = STACK()
    processed_string = preprocess_string(input_string)
    for char in processed_string:
        stack.push(char)
    reversed_string = stack.reverse()
    return processed_string == reversed_string

def main():
    input_string = input("Enter a string to check if it is a palindrome: ")
    
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
main()