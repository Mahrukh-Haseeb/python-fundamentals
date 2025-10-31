#===================Best Practices==============================

#------------------Don't Repeat Yourself------------------------


#----Bad Example----

# print("Welcome Ali")
# print("Welcome Zunaira")
# print("Welcome Aimen")


#-----------------------------------------------------

#-----Better-------

# def greet(name):
#     print(f"Welcome, {name}")

# greet("Ali")
# greet("Zunaira")
# greet("Aimen")



# def greet(name):
#      print(f"Welcome, {name}")

# for person in ["Ali", "Zunaira", "Aimen"]:
#      greet(person)

#-------------------Single Responsibility Principle--------------

#---Bad Example---

# def process_order():
#      print("Showing menu")
#      name = input("Enter your name")
#      print("Saving order")


#-------------------------------------------------

#----Better----

# def show_menu():
#      print("Showing menu")

# def take_order():
#     name = input("Enter your name")
#     print("Saving order")



# -------------------Readability Counts---------------

#----Bad Example----

# def f(a,b):
#      return a*b/100

#----Better-------

# def Calculate_discount(price, percent):
#      return price * percent / 100




#--------------------Error Handling-------------------

# file = open("menu1.csv", "r")

#------Better------

# try:

#     file = open("menu1.csv", "r")

# except FileNotFoundError:

#     print("menu1.csv not found, please enter a valid file name.")


# --------------------Modularity---------------------

# Don't put all your code into one giant file.

# Split it into smaller files and fucntions that work together.


#-----------------------------------------------------

import this

# ==================Version Control=======================

# git init

# git add .

# git commit -m "added new file"

# git remote add origin repolink

# git push -u origin main

