class Cheeseburguer:
    def delivery(self):
        print("delivering cheeseburguer")

class Sushi:
    def delivery(self):
        print("delivering sushi")

class DeliveryManager:
    def __init__(self, choice):
        self.choice = choice
    
    def delivery(self):
        if self.choice == "cheeseburger":
            Cheeseburguer().delivery()
            return "delivery complete"
        elif self.choice == "sushi":
            Sushi().delivery()
            return "delivery complete"
        else:
            return "delivery not available"

def main():
    print("What would you like to order? (Type 'cheeseburger' or 'sushi')")
    user_choice = input().lower()
    
    delivery_manager = DeliveryManager(user_choice)
    print(delivery_manager.delivery())

if __name__ == "__main__":
    main()
