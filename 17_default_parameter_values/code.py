def add(x,y):
    print(x+y)

add(5, 5)

# ----------------------------------------------------------------
default_y = 3

def add(x, y=default_y):
    sum = x + y 
    print(sum)

add(2)

# won't be modified since it's already there
default_y = 4

add(2)