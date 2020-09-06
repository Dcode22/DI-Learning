class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}
    def add_animal(self, animal, quantity=1):
        if animal not in self.animals:
            self.animals[animal] = quantity
        elif animal in self.animals:
            self.animals[animal] += quantity
    def get_info(self):
        print("McDonald's farm") 
        for i in self.animals:
            print(i, "      :", self.animals[i])
        print("E-I-E-I-O!")
    def get_animal_types(self):
        self.animal_types = []
        for i in self.animals:
            self.animal_types.append(i)
        self.animal_types.sort()
        return self.animal_types
    def get_short_info(self):
        print(f"McDonald's farm has {self.get_animal_types()}.")