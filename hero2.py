class SuperHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchprace):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchprace = catchprace


Hero = SuperHero("Maxim", "Max", "Teleportation", 10, "Hello, world!")
print(Hero.name)
Hero.health_points = Hero.health_points*2
print(Hero.nickname, Hero.superpower, Hero.health_points)
print(len(Hero.catchprace))

class AirHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchprace, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchprace = catchprace
        self.damage = damage
        self.fly = False

Hero2 = AirHero("James", "Jack", "Teleportation", 10, "Air must be saved!", 0)

class SpaceHero:
    people = "people"

    def __init__(self, name, nickname, superpower, health_points, catchprace, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchprace = catchprace
        self.damage = damage
        self.fly = False

Hero3 = SpaceHero("Alexander", "Alex", "Invisibility", 10, "The world will be safe!", 0)

Hero2.health_points = Hero2.health_points**2
print(Hero2.health_points)
Hero3.health_points = Hero3.health_points**2
print(Hero3.health_points)
Hero2.fly = True
Hero3.fly = True
print(Hero2.fly, Hero3.fly)

class Villain:
    people = "monster"

    def __init__(self, name, nickname, superpower, health_points, catchprace, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchprace = catchprace
        self.damage = damage
        self.fly = False

Villain1 = Villain("Thomas", "Tom", "Invisibility", 10, "The world will be destroyed!", 5)

gen_x = ()
crit = Villain1.damage**2
print(crit)
crit = Hero2.damage**2
print(crit)
