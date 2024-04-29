class IceCream:
    def __init__(self, flavor="", toppings=""):
        self.flavor = flavor
        self.toppings = toppings
        
    def get_icecream(self):
        return f"Flavor: {self.flavor}, Toppings: {self.toppings}"

    def request_and_calculate_price(self):
        flavors = input("choose a flavor:")
        toppings = input("choose a topping:")
        self.flavor = flavors
        self.toppings = toppings
        
        prices = {
            "Vanilla": 1,
            "Chocolate": 2,
            "Strawberry": 3,
            "Chocolate Chips": 2,
            "Sprinkles": 1,
            "Caramel": 3
        }

        flavor_price = prices.get(self.flavor)
        toppings_price = prices.get(self.toppings)

        if not flavor_price:
            raise ValueError(f"Flavor {self.flavor} is not available")
        if not toppings_price:
            raise ValueError(f"Topping {self.toppings} is not available")

        total_price = flavor_price + toppings_price
        print(f"Total price: {total_price}")
        return total_price

    def send_notification(self):
        print("Your order is ready to pick up")

if __name__ == "__main__":
    
    ice_cream = IceCream()

    print(ice_cream.get_icecream())
    ice_cream.request_and_calculate_price()
    ice_cream.send_notification()
    print(ice_cream.get_icecream())

