from exercise1 import Family
family_dict=[{
    'name':'Bob',
    'age':40,
    'gender':'Male',
    'power':'SuperHuman Strength',
    'incredible_name':'Mr. Incredible'
},{
    'name':'Helen',
    'age':40,
    'gender':'Female',
    'power':'Elasticity',
    'incredible_name':'Elastigirl'
},{
    'name':'Violet',
    'age':16,
    'gender':'Female',
    'power':'Invisibility',
    'incredible_name':'InvisibleGirl'
},{
    'name':'Dash',
    'age':12,
    'gender':'Male',
    'power':'SuperFastSpeed',
    'incredible_name':'Speedster'
}
]

class TheIncredibles(Family):
    def __init__(self, lastname, members):
        super().__init__(lastname, members)
    
    def use_power(self, name):
        try:
            if self.is_18(name) == True:
                for i in range(len(self.members)):
                    if self.members[i]["name"] == self.name:
                        print(self.members[i]["power"])
            else:
                raise ValueError("Too Young")
        except:
            print("you have no powers here")
    def presentHeroes(self):
        output = [self.lastname]
        for member in self.members:
            output.append(f"name: {member['incredible_name']}, power: {member['power']}")
        print ("\n".join(output))

def main():
    print("hello")
    the_Incredibles = TheIncredibles("Parr", family_dict)
    print(the_Incredibles.members)
    the_Incredibles.use_power("Violet")
    print(repr(the_Incredibles))
    the_Incredibles.presentHeroes()
    the_Incredibles.born(name = 'Baby Jack', age = 1, gender = 'male', power = 'Unknown Power', incredible_name = 'Baby Jack Incredible')
    print(repr(the_Incredibles))
    the_Incredibles.presentHeroes()
main()


