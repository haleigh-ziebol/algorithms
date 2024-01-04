def is_match(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')

def isValid(s):
    stack = []

    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack or not is_match(stack.pop(), char):
                return False

    return not stack

# Test string
test_string = "()[]{}"

# Call the isValid function
result = isValid(test_string)

# Print the result
print(f"The string '{test_string}' is valid: {result}")
