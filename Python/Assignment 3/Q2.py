class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Stock: {self.stock})"


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append(CartItem(product, quantity))
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Insufficient stock for {product.name}. Available: {product.stock}")

    def remove_product(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                item.product.stock += item.quantity  # Restock the product
                self.items.remove(item)
                print(f"Removed {product_name} from cart.")
                return
        print(f"{product_name} not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        
        total = 0
        print("Items in your cart:")
        for item in self.items:
            print(f"- {item.product.name}: {item.quantity} x ${item.product.price:.2f} = ${item.total_price():.2f}")
            total += item.total_price()
        print(f"Total: ${total:.2f}")

    def checkout(self):
        total = sum(item.total_price() for item in self.items)
        self.items.clear()  # Clear the cart after checkout
        print(f"Checked out successfully! Total amount: ${total:.2f}")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product_name):
        self.cart.remove_product(product_name)

    def view_cart(self):
        self.cart.view_cart()

    def checkout(self):
        self.cart.checkout()


# Example usage:
if __name__ == "__main__":
    # Creating products
    product1 = Product("Laptop", 999.99, 10)
    product2 = Product("Smartphone", 499.99, 5)
    product3 = Product("Headphones", 199.99, 20)

    # Creating a user
    user = User("alice", "password123")

    # Adding products to the user's cart
    user.add_to_cart(product1, 1)
    user.add_to_cart(product2, 2)

    # Viewing the cart
    user.view_cart()

    # Removing a product from the cart
    user.remove_from_cart("Smartphone")

    # Checking out
    user.checkout()

    # Attempt to add more items than available stock
    user.add_to_cart(product3, 25)
