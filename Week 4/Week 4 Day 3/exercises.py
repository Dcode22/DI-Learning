# ex1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dictionary1 = zip(keys, values)
# print(dict(dictionary1))
 
# ex2 
# store = {
# "name": 'Zara', 
# "creation_date": 1975, 
# "creator_name": "Amancio Ortega Gaona", 
# "type_of_clothes": ["men", "women", "children", "home"], 
# "international_competitors": ["Gap", "H&M", "Benetton"], 
# "number_stores": 7000, 
# "major_color": {"France": 'blue', "Spain": 'red', "US": ['pink', 'green'] },
# }
# store["number_stores"] = 2

# print("The clients of Zara are", store.get("type_of_clothes"))
# store["country_creation"] = "Spain"

# if "international_competitors" in store:
#     store["international_competitors"] += ["Desigual"]
# store.pop("creation_date")

# print(store)
# print(store["international_competitors"][-1])
# print("The major clothes colors in the United States are", store["major_color"]["US"][0], "and", store["major_color"]["US"][1], ".")
# print(len(store))
# print(store.keys())
# more_on_zara = {
#     'creation_date': 1975, 
#     'number_stores': 10000  
# }
# store.update(more_on_zara)
# print(store)
# print(store["number_stores"])
# ex3
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_users_A = {}
for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)
disney_users_B = {}
for i in range(len(users)):
    disney_users_B[i] = users[i]
print(disney_users_B)
disney_users_C = {}
users.sort()
for i in users:
    disney_users_C[i] = users.index(i)
print(disney_users_C)
disney_users_D = {}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for x in users:
    num = users.index(x)
    if "i" in users[num]:
        if users[num][0] == "M" or users[num][0] == "P":
            disney_users_D[x] = users.index(x)
print(disney_users_D)