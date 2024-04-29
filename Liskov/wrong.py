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
        if self.magic_power < 1000: #breaking lsp
            print(f"{self.name} cannot attack due to insufficient magic power!")
        else:
            print(f"{self.name} is attacking with magic power {self.magic_power}!")

class Shieldedblade(Sword):
    def __init__(self, name, shield_power):
        super().__init__(name)
        self.shield_power = shield_power

    def defend(self): #lacking the attack method
        print(f"{self.name} is defending with shield power {self.shield_power}!")

def battle(sword):
    sword.attack()

sword = Sword("Excalibur")
magic_sword = Katana("Yamato", 500)
Shieldedsword = Shieldedblade("Aegis", 1000)

battle(sword)
battle(magic_sword)
battle(Shieldedsword)