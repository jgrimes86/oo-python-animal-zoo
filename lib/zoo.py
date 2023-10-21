from lib.animal import Animal

class Zoo:
    all = []
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    def animals(self):
        return[animal for animal in Animal.all if animal.zoo == self]
    
    def animals_species(self):
        species_list = []
        for animal in self.animals():
            if animal.species not in species_list:
                species_list.append(animal.species)
        return species_list
    
    def find_by_species(self, s):
        return[animal for animal in self.animals() if animal.species == s]
    
    def animal_nicknames(self):
        return[animal.nickname for animal in self.animals()]
    
    @classmethod
    def find_by_location(cls, location):
        return[zoo for zoo in cls.all if zoo.location == location]
