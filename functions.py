# A function is a block of code that only runs when it is called. in python we use indentation and not curly bracket

# returns a value

def addNum(num1, num2):
    total = num1 + num2
    return total
print(addNum(20, 8))

def subNum(num1, num2):
    difference = num1 - num2
    return difference
print(subNum(80, 30))

def sayhelloworld(name= 'abdul'):
    print(f'hello {name}')

print(sayhelloworld('abdul'))

#lamda function is a small and anonymous function. it can check any number of argument but can only have in the expression. very similiar to the javascript arrow function

addNum = lambda num1, num2: num1 +num2
print(addNum(30, 40))






    