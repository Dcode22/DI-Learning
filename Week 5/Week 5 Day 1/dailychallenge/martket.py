def main():
    from farm import Farm
    mcDonald = Farm("McDonald")
    mcDonald.add_animal("cow", 5)
    mcDonald.add_animal("sheep")
    mcDonald.add_animal("sheep")
    mcDonald.add_animal("goat", 12)
    
    mcDonald.get_info()
    print(mcDonald.get_animal_types())
    mcDonald.get_short_info()

main()
