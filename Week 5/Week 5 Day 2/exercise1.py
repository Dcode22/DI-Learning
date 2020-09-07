# ex 1
class Family:

    def __init__(self, lastname, members):
        self.members = members
        self.lastname = lastname
    def born(self, **memberinfo):
        self.members.append(memberinfo)
    def is_18(self, name):
        self.name = name
        for i in range(len(self.members)):
            if self.members[i]["name"] == self.name:
                if self.members[i]["age"] >= 18:
                    return True
                else:
                    return False
    def __repr__(self):
        output = [self.lastname]
        for member in self.members:
            output.append(f"name: {member['name']}, age: {member['age']}, gender: {member['gender']}")
        return "\n".join(output)
    # def __repr__(self):
    #     print(f"{self.lastname} family members include:")
    #     for i in range(len(self.members)):
    #         print(f"{self.members[i]['name']} who is a {self.members[i]['age']} year old {self.members[i]['gender']},")

def main():            
    levinemembers = [{'name':'Michael','age':15,'gender':'Male','is_child':False}, {'name':'Sarah','age':32,'gender':'Female','is_child':False}] 
    Levine = Family("Levine", levinemembers)
    Levine.born(name = 'Dovid', age = 12, gender = "male", is_child = False)
    print(Levine.members)
    print(Levine.is_18("Dovid"))
    print(Levine.members)
    print(repr(Levine))


if __name__ == "__main__":
    main()

