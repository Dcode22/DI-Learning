# ex1
# my_fav_nums = {22, 33, 9, 97, 47}
# print(my_fav_nums)
# my_fav_nums.add(23)
# my_fav_nums.add(42)
# print(my_fav_nums)
# my_fav_nums.remove(23)
# print(my_fav_nums)
# friend_fav_nums = {14, 18, 73, 99}
# our_fav_nums = friend_fav_nums.union(my_fav_nums)
# print(our_fav_nums)
# ex2
# mi_fav_nums = (22, 33, 9, 97, 47)
# print(mi_fav_nums)
# mi_fav_nums = list(mi_fav_nums)
# mi_fav_nums.append(42)
# mi_fav_nums.append(38)
# print(mi_fav_nums)
# mi_fav_nums.remove(38)
# print(mi_fav_nums)
# friends_fav_nums = (14, 18, 73, 99)
# friends_fav_nums = list(friends_fav_nums)
# ours_fav_nums = (friends_fav_nums.extend(mi_fav_nums))
# print(ours_fav_nums)
# ours_fav_nums = tuple(ours_fav_nums)
# print(ours_fav_nums)

# for the Exercise 2 you didnt say if with tuple its working or not ? but you need to understand that tuple is immutable so after creating a tuple you cannot modify the tuple 

# ex3
# list = [i*0.5 for i in range(3,11)]
# print(list)
# # ex4
# list2 = [i for i in range(1,21)]
# print(list2)
# ex5
# while True:
#     topping = input("enter a pizza topping: ")
#     if topping == "quit":
#         break
#     print("We will add",topping, "to your pizza")
# ex6
# family = ["Mom", "Dad", "Sister", "Brother"]
# ticketsprice = 0
# for i in range(len(family)): 
#     sentence = str("How old are you " + (family[i]) + "?: ") # Try to use f"{var}" instad of + concatenation
#     age = int(input(sentence))
#     if age >= 12:
#         ticket = 15
#     elif age > 3:
#         ticket = 10
#     else: 
#         ticket = 0
#     ticketsprice = ticketsprice + ticket
# print("total price =", ticketsprice)
friends = ("Jack", "Dan", "Carl")
friends_allowed=[]
for i in range(len(friends)): 
    sentence2 = str("How old are you " + (friends[i]) + "?: ") # here also try to use f"{var}"
    age = int(input(sentence2))
    if age >= 16 and age <= 21: # In python you can write if  16 <= age <= 21
        friends_allowed.append(friends[i])
    else:
        continue
    # Here the else: continue is useless you can remove it.
print(friends_allowed, "can come")



        
