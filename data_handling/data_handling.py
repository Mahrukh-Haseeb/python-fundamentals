# Working with External Data (CSV & JSON in Python)
# Using Virtual Environments & Installing Packages with pip

#=================================================================================================


#Reading CSV

# import csv

# with open("orders.csv", mode="r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(f"{row['name']} ordered a {row['size']} {row['drink']} for Rs. {row['price']}")


#writing to CSV File:


# data = [
#     {"name": "Amna", "drink": "Tea", "size": "Medium", "price": 1000},
#     {"name": "Ayesha", "drink": "Coffee", "size": "Small", "price": 500},
# ]

# with open("new_orders.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "drink", "size", "price"])
#     writer.writeheader()
#     writer.writerows(data)

#=================================================================================================

# Working with JSON

#-----------------Reading JSON-------------------------


# import json

# with open("orders.json", "r") as file:
#     data = json.load(file)

# for order in data:
#     print(f"{order['name']} ordered {order['drink']} for Rs. {order['price']}")


# ------------------Writing to JSON------------------------


# orders = [
#     {"name": "Ali", "drink": "Latte", "size": "Medium", "price": 1000},
#     {"name": "Ayesha", "drink": "Espresso", "size": "Small", "price": 500},
# ]

# with open("saved_orders.json", "w") as file:
#     json.dump(orders, file, indent = 4)

# print("Orders saved to saved_orders.json")
