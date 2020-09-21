# exercise 1

import json

# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payble":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# myDict = json.loads(sampleJson)
# salary_value = myDict["company"]["employee"]["payble"]["salary"]
# print(salary_value)

# exercise 2

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
sampleJson = list(sampleJson)
sampleJson.sort()
print(sampleJson)
sampleJson = json.dumps(sampleJson)
print(sampleJson)

with open('sampleJson.txt', 'w') as f:
    f.write(sampleJson)