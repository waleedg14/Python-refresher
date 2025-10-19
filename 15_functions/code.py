def hello():
    print("hello!")

hello()

# -- Defining vs. calling --
# It's still all sequential!

# ---2
def user_age_in_seconds():
    user_age = int(raw_input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")

# ---2 this sin't what you want
def print():
    print("Hello world!")