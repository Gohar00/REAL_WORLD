class Animal:
    def __init__(self, name, species, sound=""):
        self.name = name
        self.species = species
        if type(sound) == str:
            self.sound = sound
        else:
            self.sound = ""

    def make_sound(self):
        print(self.sound)

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def eat(self, food):
        return f'{self.name} eating {food}'

    def move(self, direction):
        return f'{self.name} move to {direction}'

