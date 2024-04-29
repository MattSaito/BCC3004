class Food:
    def delivery(self):
        pass

class Cheeseburger(Food):
    def delivery(self):
        print("delivering cheeseburger")

class IceCream(Food):
    def delivery(self):
        print("delivering ice cream")
        
class Sushi(Food):
    def delivery(self):
        print("delivering sushi")

class DeliveryManager:
    def __init__(self, food_map):
        self.food_map = food_map
    
    def delivery(self, choice):
        if choice in self.food_map:
            food = self.food_map[choice]()
            food.delivery()
            return "delivery complete"
        else:
            return "delivery not available, please update the menu."

def main():
    food_map = {
        "cheeseburger": Cheeseburger,
        "sushi": Sushi,
        "ice cream": IceCream
    }
    
    print("What would you like to order?")
    user_choice = input().lower()

    delivery_manager = DeliveryManager(food_map)
    print(delivery_manager.delivery(user_choice))

if __name__ == "__main__":
    main()
