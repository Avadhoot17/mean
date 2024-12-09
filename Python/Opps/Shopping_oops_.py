class Product:
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

class CartItem:
    def _init_(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def _init_(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if product.reduce_stock(quantity):
            self.items.append(CartItem(product, quantity))
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def remove_from_cart(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                item.product.stock += item.quantity  # Restore stock
                self.items.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"{product_name} is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nItems in your cart:")
        total_price = 0
        for item in self.items:
            print(f"{item.product.name} - {item.quantity} x {item.product.price} = {item.quantity * item.product.price}")
            total_price += item.quantity * item.product.price
        print(f"Total Price: {total_price}\n")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add items before checking out.")
            return
        total_price = sum(item.quantity * item.product.price for item in self.items)
        print(f"Checkout successful! Total price to pay: {total_price}")
        self.items = []  # Empty the cart after checkout

class User:
    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

# Example Usage
if _name_ == "_main_":
    # Create some products
    product1 = Product("Laptop", 50000, 10)
    product2 = Product("Smartphone", 20000, 5)
    product3 = Product("Headphones", 2000, 20)

    # Create a user
    user = User("john_doe", "password123")

    # User actions
    user.cart.add_to_cart(product1, 1)
    user.cart.add_to_cart(product2, 3)
    user.cart.add_to_cart(product3, 10)
    user.cart.view_cart()
    user.cart.remove_from_cart("Smartphone")
    user.cart.view_cart()
    user.cart.checkout()