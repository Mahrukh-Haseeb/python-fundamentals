# File I/O” means File Input and Output.

# Input (Read) → You are reading from a file.

# Output (Write) → You are writing something into a file.
# file = open("filename.txt", "mode")

# "r"	Read	
# "w"	Write	
# "a"	Append	
# "x"	Create


# Example 1  Write mode "w"

# Writing text to a file

# file = open("notes.txt", "w") 
# file.write("Hello, world!\n")
# file.write("I love Python\n")
# file.close()
# print("File has been created and written successfully!")


# Example 2  Read mode "r"
# file = open("notes.txt", "r")  
# content = file.read()
# print("File content:")
# print(content)
# file.close()



# with open("example.txt", "w") as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n")



# print("File created and automatically closed!")




# Example 3  Appending to a file
# with open("example.txt", "a") as file:
#     file.write("Adding a new line!\n")

# print("Data appended successfully!")




# Context Manager
# The with statement in Python is something called a context manager.
# with open("notes.txt", "r") as file:
#     data = file.read()



# try:
#     with open("notes.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file you’re trying to read doesn’t exist!")



# try:
#     with open("students.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found! Creating a new one...")
#     with open("students.txt", "w") as file:
#         file.write("This file was just created.\n")



# Simple Notes App

# note = input("Write a note: ")

# with open("mynotes.txt", "a") as file:
#     file.write(note + "\n")

# print("Note saved!")

# print("\nAll saved notes:")
# with open("mynotes.txt", "r") as file:
#     for line in file:
#         print("-", line.strip())




# from datetime import date
# today = date.today()

# note = input("Write a note: ")
# with open("mynotes.txt", "a") as file:
#     file.write(f"{today} - {note}\n")



# Function to search notes
# def search_notes():
#     keyword = input("Enter keyword to search: ").lower()
#     found = False

#     try:
#         with open("mynotes.txt", "r") as file:
#             for line in file:
#                 if keyword in line.lower():
#                     print("Found:", line.strip())
#                     found = True
#         if not found:
#             print("No matching notes found.")
#     except FileNotFoundError:
#         print("Notes file not found. Please add a note first.")

# search_notes()



# -------------------------------------Basic Expense Tracker---------------------------------------


# category = input("Enter expense category (e.g. Food, Rent, Transport): ")
# amount = input("Enter amount: ")

# with open("expenses.txt", "a") as file:
#     file.write(f"{category} - {amount}\n")

# print("Expense recorded successfully!")

# #--------------------------------------------------------------------------------------------------


# with open("expenses.txt", "r") as file:
#     print("\nYour Expenses:")
#     for line in file:
#         print("-", line.strip())


# #---------------------------------------------------------------------------------

# def add_expense():
#     category = input("Enter category (e.g. Food, Rent, Travel): ").title()
#     amount = input("Enter amount (in Rs): ")
#     with open("expenses.txt", "a") as file:
#         file.write(f"{category} - {amount}\n")
#     print(f"Expense added: {category} - Rs.{amount}\n")


# def view_expenses():
#     try:
#         with open("expenses.txt", "r") as file:
#             data = file.readlines()
#             if not data:
#                 print("No expenses recorded yet.\n")
#                 return
#             print("All Expenses:")
#             for line in data:
#                 print("-", line.strip())
#             print()
#     except FileNotFoundError:
#         print("File not found! Please add an expense first.\n")


# def total_expenses():
#     total = 0
#     try:
#         with open("expenses.txt", "r") as file:
#             for line in file:
#                 parts = line.strip().split(" - ")
#                 if len(parts) == 2:
#                     try:
#                         total += float(parts[1])
#                     except ValueError:
#                         pass
#         print(f"Total Expenses: Rs.{total}\n")
#     except FileNotFoundError:
#         print("No expenses found.\n")


# # #--------------------------------------------------------------------------------------------------
# while True:
#     print("========= PERSONAL EXPENSE TRACKER =========")
#     print("1. Add Expense")
#     print("2. View Expenses")
#     print("3. View Total Expenses")
#     print("4. Exit")
#     print("=================================================\n")

#     choice = input("Enter your choice (1-4): ")

#     if choice == "1":
#         add_expense()
#     elif choice == "2":
#         view_expenses()
#     elif choice == "3":
#         total_expenses()
#     elif choice == "4":
#         print("Goodbye! Your expenses are saved.")
#         break
#     else:
#         print("Invalid choice! Please select between 1 and 4.\n")




#-------------------------------------Quiz---------------------------------------

# What is the correct way to define a function in Python?
# a) function greet():
# b) def greet:
# c) def greet():
# d) define greet()


# What keyword is used to handle exceptions in Python?
# a) handle
# b) except
# c) catch
# d) throw


# What does the with open("data.txt", "r") as f: statement do?
# a) Opens the file but doesn’t close it automatically
# b) Opens and ensures the file is closed automatically
# c) Deletes the file after reading
# d) None of the above


# Which of the following statements about functions is incorrect?

# a) Functions can call other functions
# b) Functions can return multiple values
# c) Function names can start with a number
# d) Functions can have default arguments



# Which statement about Python libraries is true?

# a) You must install the math library manually
# b) pandas is built into Python
# c) A module is a single file; a library can contain multiple modules
# d) Libraries cannot be imported using aliases



# What will be printed?
# def test():
#     try:
#         return 1
#     finally:
#         return 2

# print(test())


# a) 1
# b) 2
# c) None
# d) Error




# What is the output of this code?

# def greet(name):
#     print("Hello", name)

# result = greet("Ali")
# print(result)


# a) Hello Ali
# b) None
# c) Hello Ali None
# d) Error








# def greet(name):
#     return f"Hello {name}"

# result = greet("Ali")
# print(result)