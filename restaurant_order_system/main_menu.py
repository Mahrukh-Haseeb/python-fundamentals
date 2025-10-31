import csv
import os

class Menu:

    def __init__(self, filename="menu.csv"):
        self.filename = filename
        self.items = self.load_menu()

    def load_menu(self):
   
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            print(f" {self.filename} not found. Please add it and try again.")
            return []

    def show_menu(self):
     
        print("\n======= Menu =======")
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item['item']} - Rs. {item['price']}")
#========================================================================================

class Order:
 

    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, menu_item, quantity):
    
        item_name = menu_item["item"]
        price = int(menu_item["price"])
        cost = price * quantity
        self.items.append({"item": item_name, "qty": quantity, "cost": cost})
        self.total += cost
        print(f"Added {quantity} x {item_name}. Subtotal: Rs. {self.total}")

    def show_receipt(self):
  
        print("\n======= Order Receipt =======")
        if not self.items:
            print("No items ordered.")
            return
        for order in self.items:
            print(f"{order['item']} x{order['qty']} = Rs. {order['cost']}")
        print("------------------------------")
        print(f"Total: Rs. {self.total}")

    def save_order(self, filename="orders.csv"):
   
        file_exists = os.path.exists(filename)
        with open(filename, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["item", "qty", "cost"])
            if not file_exists:
                writer.writeheader()
            writer.writerows(self.items)
        print("Order saved to 'orders.csv'.")
#========================================================================================

class RestaurantApp:


    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def run(self):
  
        if not self.menu.items:
            return

        self.menu.show_menu()
        while True:
            choice = input("\nEnter item number (or 'done' to finish): ").lower()
            if choice == "done":
                break
            if not choice.isdigit() or not (1 <= int(choice) <= len(self.menu.items)):
                print("Invalid choice.")
                continue
            qty = int(input("Enter quantity: "))
            self.order.add_item(self.menu.items[int(choice) - 1], qty)

        self.order.show_receipt()
        self.order.save_order()

#========================================================================================

if __name__ == "__main__":
    app = RestaurantApp()
    app.run()







