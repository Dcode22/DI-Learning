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
        print(f"{self.name}'s farm") 
        for i in self.animals:
            print(i, "      :", self.animals[i])
        print("E-I-E-I-O!")
    def get_animal_types(self):
        animals = list(self.animals.keys())
        animals.sort()
        return animals
    def get_short_info(self):
        print(f"{self.name}'s farm has {self.get_animal_types()}.")