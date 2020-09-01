# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# sampleDict.pop("name")
# sampleDict.pop("salary")
# print(sampleDict)
# my_list = []

# for i in [2, 3, 4]:
#     for j in [100, 200, 300]:
#         my_list.append(i*j)

# print(my_list)

# >> [200, 400, 600, 300, 600, 900, 400, 800, 1200]
my_list = [i*j for j in [100, 200, 300] for i in [2, 3, 4]]
print(my_list)
