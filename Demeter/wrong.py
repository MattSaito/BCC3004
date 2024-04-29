from random import randint

class River:
    def __init__(self, water, animal):
        self.water = water
        self.animal = animal
    
    def get_animals(self):
        return self.animal

class Fisher:
    def __init__(self, name, baits, river):
        self.name = name
        self.baits = baits
        self.caught_fish = 0
        self.river = river  # Fisher holds a reference to the River instance
    
    def get_fish(self):
        random = randint(0, 10)
        if random >= 5:
            self.caught_fish += 1
            print(f"{self.name} caught a fish")
            return True
        return False

    def fishing(self):
        if self.river.water == "clean":  # Directly accessing the water attribute of the River instance
            while self.baits > 0:
                self.get_fish()
                self.baits -= 1



def main():
    name = input("Enter the fisher's name: ")
    baits = int(input("Enter the number of baits: "))
    water_state = input("Enter the state of the river (clean or dirty): ")
    fish_type = input("Enter the type of fish you want to go fishing for: ")

    river = River(water_state, fish_type)
    fisher = Fisher(name, baits,river)

    
    if fisher.river.water == "clean":
        fisher.fishing()
    else:
        print("The river is dirty. Fishing is not allowed. Therefore:")

    print(f"{fisher.name} has caught {fisher.caught_fish} {fish_type}")

if __name__ == "__main__":
    main()
