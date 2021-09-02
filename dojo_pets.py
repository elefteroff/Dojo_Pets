class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.pets_health = 75
        self.pets_energy = 25

    def sleep(self):
        self.pets_energy = + 25
        return self

    def eat(self):
        self.pets_energy += 5
        self.pets_health += 10
        return self

    def play(self):
        self.pets_health += 5
        return self

    def noise(self):
        print("Whoof")
        return self

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = None
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self, treats, pet_food):
        self.pet.eat()
        return self
    
    def bathe(self):
        self.pet.noise()
        return self

kentaro = Ninja("Nakagawa", "Kentaro", "Doggy Biscuits", "Raw Steak", "Dog")
animal = Pet("Gravity", "Dog", "Rollover")

kentaro.pet = Pet("Gravity", "Dog", "Rollover")

kentaro.walk()
print(kentaro.pet.pets_health)

kentaro.feed("Doggy Buscuits", "Raw Steak")
print(kentaro.pet.pets_health)
print(kentaro.pet.pets_energy)

kentaro.bathe()