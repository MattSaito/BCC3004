class IceCream:
    def __init__(self, flavor, toppings):
        self.flavor = flavor
        self.toppings = toppings

    def get_icecream(self):
        return f"Flavor: {self.flavor}, Toppings: {self.toppings}"


class PriceCalculator:

    def __init__(self, prices):
        self.prices = prices

    def get_flavor_price(self, flavor):
        flavor_price = self.prices.get(flavor)
        if not flavor_price:
            raise ValueError(f"Flavor {flavor} is not available")
        return flavor_price

    def get_toppings_price(self, toppings):
        toppings_price = self.prices.get(toppings)
        if not toppings_price:
            raise ValueError(f"Topping {toppings} is not available")
        return toppings_price

    def calculate_price(self, flavor, toppings):
        flavor_price = self.get_flavor_price(flavor)
        toppings_price = self.get_toppings_price(toppings)
        total_price = flavor_price + toppings_price
        print(f"Total price: {total_price}")
        return total_price


def get_user_selection():
    flavor = input("Choose a flavor: ")
    toppings = input("Choose toppings: ")
    return flavor, toppings

def send_notification():
    print("Your order is ready to pick up")


if __name__ == "__main__":
    prices = {
        "Vanilla": 1,
        "Chocolate": 2,
        "Strawberry": 3,
        "Chocolate Chips": 2,
        "Sprinkles": 1,
        "Caramel": 3
    }

    flavor, toppings = get_user_selection()
    ice_cream = IceCream(flavor, toppings)

    print(ice_cream.get_icecream())

    price_calculator = PriceCalculator(prices)
    price_calculator.calculate_price(flavor, toppings)

    send_notification()

    print(ice_cream.get_icecream())
