def isValid(s):
    stack = []
    closeToOpen = {"}": "{", "]": "[", ")": "("}

    # loop over string
    for c in s:
        # check hashmap for char
        if c in closeToOpen:
            # see if we have a stack and if so compare last element to first closing bracket
            if stack and stack[-1] == closeToOpen[c]:
                # remove last opening bracket
                stack.pop()
            else:
                # otherwise not a match, return False.
                return False
        else:
            # append opening brackets to stack
            stack.append(c)

    return True if not stack else False


print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([])"))
print(isValid(""))
