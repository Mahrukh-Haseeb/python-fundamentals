#  What are Libraries (or Modules)?

# A library or module is a collection of pre-written Python code 
# that you can use to add extra features to your program.

# How to Import Libraries

# There are three main ways to import in Python.

# a) Importing the entire module:

# import math
# print(math.sqrt(25))
# print(math.pi)

# # b) Importing the entire module with an alias:
# import pandas as pd
# import numpy as np
# data = {'col1': [1, 2], 'col2': [3, 4]}
# df = pd.DataFrame(data)
# print(df)

# c) Importing specific items from a module:
# from math import sqrt, pi

# print(sqrt(25))
# print(pi)



# ---------------------------------Pandas--------------------------------

# Pandas is used for data manipulation, cleaning, and analysis, 
# especially when your data looks like a table (rows and columns).





# Create a DataFrame (like an Excel sheet)
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 28],
#     "Salary": [50000, 60000, 55000]
# }

# df = pd.DataFrame(data)
# print(df)


# ----------------What is NumPy-----------------?

# For fast computations on numbers:
# For scientific and mathematical tasks:
# For numerical analysis:


# arr = np.array([10, 20, 30, 40])


# print(arr * 2)        
# print("Mean:" , np.mean(arr))   
# print("Max:" , np.max(arr))    


# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print(matrix.shape)   
# print(matrix.T)        


# Two main types of errors:

# Syntax Error	
# Runtime Error (Exception)	

# print("Start")
# x = int(input("Enter a number: "))
# print(10 / x)
# print("End")


# try:
#     # risky code
# except:
#     # what to do if it fails

# try:
#     x = int(input("Enter a number: "))
#     print(10 / x)
# except:
#     print("Oops! Something went wrong.")
    



# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ValueError:
#     print("Error: Please enter a valid number.")
# except ZeroDivisionError:
#     print("Error: You cannot divide by zero!")



# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
# except ZeroDivisionError:
#     print("You can’t divide by zero!")
# except ValueError:
#     print("Invalid input! Enter numbers only.")
# else:
#     print("Division successful! Result:", result)
# finally:
#     print("Program finished running.")



# -------------------------------------------

# while True:  # Loop until valid input and successful division
#     try:
#         # Ask user for two numbers
#         numerator = float(input("Enter the numerator: "))
#         denominator = float(input("Enter the denominator: "))

#         # Attempt division
#         result = numerator / denominator

#     except ValueError:
#         # Handles invalid (non-numeric) inputs like letters or symbols
#         print("Invalid input! Please enter numeric values only.\n")

#     except ZeroDivisionError:
#         # Handles division by zero
#         print("Division by zero is not allowed! Please try again.\n")

#     else:
#         # Executes only if no error occurs
#         print(f"Division successful! {numerator} ÷ {denominator} = {result}")
#         break  # Exit loop when everything is successful

#     finally:
#         # Runs every time, even after an error
#         print("Attempt complete.\n")

# print("Program finished successfully. Goodbye!")





# -------------------------------------Quiz---------------------------------------
# 1. What is a Python library (or module)?
# a) A file that stores images
# b) A pre-written collection of code that adds functionality
# c) A folder that contains Python projects
# d) A built-in debugger

# 2. Which of the following imports only the sqrt and pi functions from the math module?
# a) import math.sqrt, math.pi
# b) import math(sqrt, pi)
# c) from math import sqrt, pi
# d) import sqrt, pi from math

# 3. Which of the following is the correct way to import a library using an alias?
# a) import pandas as pd
# b) import pandas alias pd
# c) from pandas import pd
# d) alias pandas as pd

# 4. What is Pandas primarily used for?
# a) Image processing
# b) Mathematical operations
# c) Data manipulation and analysis
# d) Game development

# 5. In Pandas, a DataFrame is most similar to:
# a) A Python list
# b) A spreadsheet or table
# c) A dictionary
# d) A string

# 6. In NumPy, what does the .mean() function do?
# a) Finds the largest number in an array
# b) Finds the smallest number in an array
# c) Calculates the average value of an array
# d) Converts an array into a list

# 8. Which block of code is always executed in Python’s error handling?
# a) try
# b) except
# c) else
# d) finally

# 9. Which statement about the try and except blocks is TRUE?
# a) The except block runs before the try block.
# b) The try block runs only if an error occurs.
# c) The except block runs only if an error occurs inside try.
# d) The try block runs after the program ends.