# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 6, 5, 6]

# A list of strings
movies = ["Interstellar", "Inception", "Oppenheimer"]

# A list with mixed data types
mixed_list = ["hello", 123, True, 3.14]

# A nested list (a list containing another list)
nested_list = [1, [2, 3], 4]

# -----------------List Operations-----------------

#Append

numbers.append(7)
print(numbers)  
movies.append("Dunkirk")
print(movies)  
nested_list.append([5, 6])
print(nested_list)

# Extend

numbers.extend([8, 9])
print(numbers)
movies.extend(["Tenet", "Memento"])
print(movies)

# Insert

nested_list = [1, [2, 3], 4]
movies.insert(1, "The Dark Knight")
print(movies)
nested_list.insert(1, [0])
print(nested_list)


# Remove
numbers = [1, 2, 3, 4, 6, 5, 6]
numbers.remove(6)
print(numbers)


# Reverse

numbers.reverse()
print(numbers)
mixed_list.reverse()
print(mixed_list)

# Index

print(movies.index("Inception"))  

# Count

print(numbers.count(6))

print(movies.count("Inception"))


# Slicing

# list[start:end]

numbers = [1, 2, 3, 4, 6, 5, 6]
numbers[1:5]
print(numbers[1:5])
numbers[:4]
print(numbers[:4])
numbers[3:]
print(numbers[3:])
numbers[-4:]
print(numbers[-4:])
numbers[::2]
print(numbers[::2])

# # List Length

print(len(numbers))

# #constructor

numbers = [1, 2, 3, 4, 6, 5, 6]
numbers_list = list(numbers)
word = "hello"
letters = list(word)
print(type(letters))



# ------------------ list comprehension---------------------

# [expression for item in iterable]
numbers = [1, 2, 3, 4, 6, 5, 6]
double = []
for n in numbers:
  doubled_value = n * 2
double.append(doubled_value)
print(double)

double = [n * 2 for n in numbers]
print(double)

evens = [n for n in numbers if n % 2 == 0]
print(evens)

add_ten = [n + 10 for n in numbers]
print(add_ten)

movies = ["Interstellar", "Inception", "Oppenheimer"]
uppercase_movies = [movie.upper() for movie in movies]
print(uppercase_movies)

i_movies = [movie for movie in movies if "I" in movie]
print(i_movies)


#[expression for item in iterable if condition ]

#-------------------------Mini quiz -------------------------

# What does the append() method do?
# a) Adds multiple elements to the end of a list
# b) Removes an element from a list
# c) Adds one element to the end of a list
# d) Inserts an element at the beginning


# Which of the following creates an empty list using a constructor?
# a) empty_list = []
# b) empty_list = list()
# c) empty_list = list([])
# d) Both b and c

a = []
b = list(a)
print (a is b)
print(a)
print(b)

# What is the purpose of the list() constructor?
# a) To convert other data types into a list
# b) To delete a list
# c) To reverse a list
# d) To make lists immutable

#-------------------------------Tuples--------------------------

# # Empty tuple
empty_tuple = ()

# # Tuple with integers
numbers = (1, 2, 3, 4)

# # Tuple with mixed data
info = ("Alice", 25, True)

# # Tuple without parentheses (Python allows this)
colors = "red", "green", "blue"
# # Single element tuple (note the comma)
single = (10,)
print(type(single)) 
