users = [
(0, "Bob", "password"),
(1, "Rolf", "bob123"),
(2, "Jose", "longpassword"),
(3, "usernmae", "1234"),

]

usernmae_mapping = {user[1]: user for user in users}

print(usernmae_mapping["Bob"])

# this is very complicated
for user in users:
    if user[1] == "Bob":
        print(user)

#  this is prompting the user
usernmae_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = usernmae_mapping[usernmae_input]

if password_input == password:
    print("your details are correct!")

else:
    print("Inccorect username or password.")