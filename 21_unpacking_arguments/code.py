# multiplication pt 1
def multiply(*args):
    print(args)
    total =1
    for arg in args:
        total = total * arg
    return total 


print(multiply(1, 3, 5))

# addition pt1
def add(x, y):
    return x + y

nums = [3,5]
# passing the * makes 5 go into y without it you get an error
print(add(*nums)) 

# addition pt2
def add(x, y):
    return x + y

nums = {"x": 15,"y":25}
print(add(**nums)) 


# multiplication pt 2
def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))
# print(apply(1, 3, 5, "+"))  # Error