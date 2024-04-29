class Sword:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f"{self.name} is attacking!")

class Katana(Sword):
    def __init__(self, name, magic_power):
        super().__init__(name)
        self.magic_power = magic_power

    def attack(self):
        print(f"{self.name} is attacking with magic power {self.magic_power}!")

class Nodachi (Sword):
    def __init__(self, name, extended_range):
        super().__init__(name)
        self.extended_range = extended_range

    def attack(self):
        print(f"{self.name} is attacking with more range {self.extended_range}!")


def battle(sword):
    sword.attack()
    

sword = Sword("Excalibur")
magic_sword = Katana("Yamato", 5000)
long_sword = Nodachi("Muramasa", 10)

battle(sword)
battle(magic_sword)
battle(long_sword)