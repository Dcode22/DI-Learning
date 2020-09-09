user_string = input("enter a string of at least 10 characters: ")
print("first character is: ", user_string[0])
print("last character is: ", user_string[-1])
for x in range(len(user_string)):
    print(user_string[0:x+1])

#this way to swap character is correct but there are lots of duplication and we dont like to do that. for solving in you can use the random module.
# Below the jonathan solutions
#Method1
# new_text += text[::-2]
# new_text += text[::2]
#Method2
# from random import randint
# for i in range(10):
# 	new_text += text[randint(0,10)]
# print(new_text)

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
