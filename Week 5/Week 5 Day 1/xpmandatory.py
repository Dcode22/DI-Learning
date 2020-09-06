# # exercise 1
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        

# def oldest_cat(*cats):
#     oldestCat = cats[0]
#     for i in range(len(cats)):
#         if cats[i].age > oldestCat.age:
#             oldestCat = cats[i]
#     print(f"the oldest cat is", oldestCat.name, ", she is", oldestCat.age, "years old." )


# def main():
#     cat1 = Cat("Minerva", 74)
#     cat2 = Cat("Mrs. Norris", 5)
#     cat3 = Cat("Crookshanks", 15)
#     oldest_cat(cat1, cat2, cat3)


# main()


# # exercise 2
# class Dog:
#     def __init__(self, nameDog, heightDog):
#         self.name = nameDog
#         self.height = heightDog
    

#     def talk(self):
#         print("woof!")

    
#     def jump(self):
#         height = self.height*2
#         print(height)


#     def info(self):
#         print(self.name, self.height)


# def biggest_Dog(*dogs):
#     biggest_Dog = dogs[0]
#     for i in range(len(dogs)):
#         if dogs[i].height > biggest_Dog.height:
#             biggest_Dog = dogs[i]
#     print(f"the biggest dog is", biggest_Dog.name, ", he is", biggest_Dog.height, "cm tall." )



# def main():
#     davids_Dog = Dog("Rex", 50)
#     sarahs_Dog = Dog("Teacup", 20)
#     davids_Dog.info()
#     sarahs_Dog.info()
#     biggest_Dog(davids_Dog, sarahs_Dog)

# main()


# # exercise 3

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
    

#     def sing_me_a_song(self):
#         for i in self.lyrics:
#             print(i)


# def main():
#     sailing = Song(["In my heart a storm was swirling", "a passion to be soaring.", "So i fastened up my sail", "hoping to catch that golden gale."])
#     sailing.sing_me_a_song()


# main()


# exercise 4

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    

    def get_animals(self):
        print(self.animals)
    

    def sell_animal(self, animal_name):
        print(f"Goodbye Mr. {animal_name}!")
        self.animals.remove(animal_name)

    
    def sort_animals(self):
        self.animals_dict = {}
        animal_letters = []
        for i in range(len(self.animals)):
            if self.animals[i][0] not in animal_letters:
                animal_letters.append(self.animals[i][0])
                self.animals_dict[self.animals[i][0]] = [self.animals[i]] 
            else:
                self.animals_dict[self.animals[i][0]].append(self.animals[i])


    def get_pen(self):
        print(self.animals_dict)    

def main():
    ramatGanZoo = Zoo("ramatGanZoo")
    ramatGanZoo.add_animal("pig")
    ramatGanZoo.add_animal("peacock")
    ramatGanZoo.add_animal("leopard")
    ramatGanZoo.add_animal("lion")
    ramatGanZoo.add_animal("bat")
    ramatGanZoo.add_animal("monkey")
    ramatGanZoo.add_animal("martin")
    ramatGanZoo.add_animal("bear")
    ramatGanZoo.get_animals()
    ramatGanZoo.sell_animal("lion")
    ramatGanZoo.get_animals()
    ramatGanZoo.sort_animals()
    ramatGanZoo.get_pen()
main()
