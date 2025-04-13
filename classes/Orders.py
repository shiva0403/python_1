class Orders:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
        else:
            print(f"{item} not found in cart")

    def __str__(self):
        return f"Cart: {', '.join(self.cart)}"

    def __len__(self):
        return len(self.cart)

order = Orders()
order.add_to_cart("green apple")
order.add_to_cart("red apple")
print(order)
print(len(order))
