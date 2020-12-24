def eval(expression):
    index = 0
    op = '+'
    while index < len(expression):
        char = expression[index]
        if char is ('+' or '-'):
            op = char
        index += 1

#Driver function
print(eval('- (3 + (2 - 1))'))