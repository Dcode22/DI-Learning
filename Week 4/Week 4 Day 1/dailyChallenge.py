user_string = input("enter a string of at least 10 characters: ")
print("first character is: ", user_string[0])
print("last character is: ", user_string[-1])
for x in range(len(user_string)):
    print(user_string[0:x+1])

user_string = list(user_string)
print(user_string)
temp = user_string[0]
user_string[0] = user_string [5]
user_string[5] = temp
temp = user_string[8]
user_string[8] = user_string [3]
user_string[3] = temp
temp = user_string[6]
user_string[6] = user_string[2]
user_string[2] = temp
temp = user_string[9]
user_string[9] = user_string[1]
user_string[1] = temp
temp = user_string[9]
user_string[9] = user_string[7]
user_string[7] = temp
print("New scrambled string:", ''.join(user_string))
