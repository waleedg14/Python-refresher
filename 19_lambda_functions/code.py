def add(x, y):
    return x + y

print(add(5, 7))

# Lambda function

add = lambda x, y: x + y 

print(add(5, 7))

# Lambda function pt2

def double(x):
    return x *2

# map simplifies it for you
sequence = [1,4,5,9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)

# map simplifies it for you
sequence = [1,4,5,9]
# this is bad example for lambda
doubled = [(lambda x: x *2) (x) for x in sequence]
# this is how you use lambda
doubled = list(map(lambda x:x *2, sequence))