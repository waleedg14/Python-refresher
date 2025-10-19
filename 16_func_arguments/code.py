# parametr
def add(x,y):
    result = x+y
    print(result)

# argument
add(5,3)

# ---------------------------------
# parametr
def say_hello(name, surname):
    print(f"Hello!, {name} {surname}")

# argument
say_hello(surname="Bob", name="Smith")

# ---------------------------------
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("You fool!")

divide(dividend= 15, divisor=0)