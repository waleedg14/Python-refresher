# -------
# numbers = [1, 3, 5]
# doubled = [num * for num in numbers]

# for num in numbers:
#     doubled.append(num * 2)

# -------
friends = ["Sam", "Samantha", "shdjd"]
starts_s = [friend for friend in friends if friend.lower().startswith("s")]

print(friends)
print(starts_s)
print(friends[0] is starts_s[0])
print("friends: ", id(friends), "starts_s:", id(starts_s))