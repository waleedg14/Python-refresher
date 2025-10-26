# part one
def named(**kwargs):
    print(kwargs)
named(name="Waleed", age =27)

# part two
def named(name, age):
    print(name, age)

details = {"name": "Waleed", "age": 27}

named(**details)

# part three
def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Waleed", age = 27)

# part 4 
def both(*args, **kwargs):
    print(args)
    print(args)

both(1, 3, 5, name="Waleed", age=27)