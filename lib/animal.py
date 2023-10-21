class Animal:
    all = []
    def __init__(self, species, number, nickname, zoo_instance):
        self.species = species
        self.number = number
        self.nickname = nickname
        self.zoo = zoo_instance
        self.weight = number
        Animal.all.append(self)

    def find_by_species(s):
        return[animal for animal in Animal.all if animal.species == s]

    

