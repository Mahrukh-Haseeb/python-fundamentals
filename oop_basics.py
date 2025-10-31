# #============================QUIZ==============================

# #-----------------------------1--------------------------------

# # word = "python"
# # print(word[::-2])
# # What is printed?

# # a) ‘pto’ b) ‘nhy’ c) ‘nht’ d) ‘ntr’

# #------------------------------2-------------------------------

# # What is the output?

# # x = 0
# # for i in range(3):
# #     x += i 
# # print(x)

# # a) 3 b) 6 c) 2 d) None

# #-------------------------------3------------------------------

# # What’s the difference between is and ==?
# # a) is compares identity, == compares values.
# # b) They are identical.
# # c) is checks data type, == checks equality.
# # d) None of the above.

# #-------------------------------4------------------------------

# # Which built-in function returns the number of items in a list or tuple?
# # a) length() b) count() c) len() d) size()

# #--------------------------------5-----------------------------

# # What is the result of:
# # print("hello" * 3)


# # a) hellohellohello
# # b) ['hello', 'hello', 'hello']
# # c) ['h', 'e', 'l', 'l', 'o', 'h', ...]
# # d) Error

# #--------------------------------6-----------------------------

# # What will be printed?
# # x = [1, 2, 3]
# # print(x * 2)


# # a) [2, 4, 6]
# # b) [1, 2, 3, 1, 2, 3]
# # c) [[1, 2, 3], [1, 2, 3]]
# # d) Error

# #-------------------------------7------------------------------

# # Which statement is true about the finally block?

# # a) It runs only if there is no error.
# # b) It runs only if there is an error.
# # c) It always runs, whether there’s an error or not.
# # d) It never runs.

# #-------------------------------8-------------------------------

# # What is the output of this comprehension?
# # nums = [1, 2, 3, 4]
# # squares = [x**2 for x in nums if x % 2 == 0]
# # print(squares)


# # a) [1, 9]
# # b) [2, 4]
# # c) [4, 16]
# # d) [1, 4, 9, 16]

# #---------------------------------9------------------------------------

# # What does this print?
# # x = 5
# # def func():
# #     x = 10
# #     print(x)
# # func()
# # print(x)

# # a) 10 10
# # b) 5 10
# # c) 10 5
# # d) Error

# #---------------------------------10------------------------------------

# # What error will this cause?
# # for i in range(5)
# #     print(i)

# # a) SyntaxError
# # b) IndentationError
# # c) NameError
# # d) TypeError

# #----------------------------------------------------------------------



# # What is Object-Oriented Programming?

# # Definition:
# # OOP is a programming paradigm that organizes code into objects,
# # bundles of data (attributes) and behavior (methods) that work together.

# ---Proceedural Code---            |     ---OOP---
# # Code = functions + variables	|     Code = classes + objects
# # Functions act on data	        |     Objects carry their own data and methods
# # Harder to scale	                |     Easier to maintain and extend.



#-----Proceedural Code Example-----
# # Managing one customer order:
# # name1 = "Ali"
# # drink1 = "Latte"
# # size1 = "Medium"
# # price1 = 1000

# # # Managing another order:
# # name2 = "Ayesha"
# # drink2 = "Espresso"
# # size2 = "Small"
# # price2 = 500

#--------------------------------------------------------------------------------------------

# # Concept                 |           Description	
# # Class	                |           A blueprint or template	
# # Object (Instance)	    |           A thing created from that template	
# # Attributes	            |           Data stored in the object	
# # Methods	                |           Actions the object can perform

# #=======================================Example=============================================

# class CoffeeOrder:
#     def __init__(self, name, drink, size, price):
#         self.name = name
#         self.drink = drink
#         self.size = size
#         self.price = price

#     def show_order(self):
#         print(f"{self.name} ordered a {self.size} {self.drink} for Rs. {self.price}")

# order1 = CoffeeOrder("Ali", "Latte", "Medium", 1000)
# order2 = CoffeeOrder("Ayesha", "Espresso", "Small", 500)

# order1.show_order()
# order2.show_order()


# #============================================================================================


# # ----------OOP'S four pillars----------:
# # 1. Encapsulation: 
# # Encapsulation means bundling data (attributes) and behavior (methods)
# # together inside one class, keeping them as a single logical unit.



# #=========================================================================================

# # 2. Abstracion:
# # Abstraction means hiding unnecessary internal details and exposing only
# # what’s important to the outside world.

# #=========================================================================================

# # 3. Inheritance:
# # Inheritance allows us to create new classes that reuse and extend attributes
# # and methods from an existing class.

# class ColdDrink(CoffeeOrder):
#     def serve(self):
#         print(f"Serving {self.drink} (Cold Drink)")


# class HotDrink(CoffeeOrder):
#     def serve(self):
#         print(f"Serving {self.drink} (Hot Drink)")

# order1 = ColdDrink("Ali", "7up", "Medium", 300)
# order2 = HotDrink("Ayesha", "Chocolate Milk", "Small", 600)

# # order1.show_order()
# # order1.serve()
# # order2.show_order()
# # order2.serve()


# #=========================================================================================

# # 4. Polymorphism
# # Polymorphism means “many forms.”
# # It allows different classes to use the same method name,
# # but each one behaves differently depending on the class.

# orders = [order1, order2]
# for order in orders:
#     order.show_order()
#     order.serve()
