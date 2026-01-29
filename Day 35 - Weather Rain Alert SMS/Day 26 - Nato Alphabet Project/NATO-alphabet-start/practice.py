import pandas

# #create and print a list of the each item in numbers squared. Print each number squared using a generator expression
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = [number * number for number in numbers]
# print(squared_numbers)
#
# print("\n".join(f"{value * value}" for value in numbers)) #join (each number times itself) with a new line

#create dictionary with student name as key and their highest score as value
# students_scores = {
#     "Alice": [78, 85, 90, 88],
#     "Bob": [92, 89, 84, 91],
#     "Charlie": [65, 72, 80, 77],
#     "Diana": [99, 95, 97, 98],
#     "Eva": [55, 60, 58, 62]
# }
#
# highest_scores = {key:max(value) for key,value in students_scores.items()}
# for key,value in highest_scores.items():
#     print(f"{key}: {value}")


# #create a dictionary with name for the key and 'child' under 13, teen ager 13 - 19, adult 20 - 59, senior 60 plus
# people = [
#     {"name": "Alice", "age": 10},
#     {"name": "Bob", "age": 17},
#     {"name": "Charlie", "age": 35},
#     {"name": "Diana", "age": 65},
#     {"name": "Eva", "age": 45},
#     {"name": "Frank", "age": 12}
# ]
#
# people_dict = {item["name"]:"Child" if item["age"] < 13 else "Teenager" if item["age"] < 20 else "Adult" if item["age"] < 60 else "Senior" for item in people}
# print(people_dict)

#create dictionary with each number as a key and small if number under 10, medium if between 10 and 20 and large if over 20
# numbers = [3, 10, 15, 25, 8, 20, 30, 7,20, 21]
#
# number_dict = {item: "small" if item < 10 else "medium" if item < 21 else "long" for item in numbers}
# print(number_dict)

# products = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Headphones", "price": 150},
#     {"product": "Mouse", "price": 25},
#     {"product": "Keyboard", "price": 85},
#     {"product": "Monitor", "price": 200}
# ]
#
# all_items_with_discounts_on_over_100 = {item["product"]: item["price"] - (item["price"]*0.20) if item["price"] > 100 else item["price"] for item in products}
# items_over_100_with_discounts = {item["product"]:item["price"] - (item["price"]*0.20) for item in products if item["price"] > 100}
# print(all_items_with_discounts_on_over_100)
# print(items_over_100_with_discounts)


#create a dictionary containing the square root of each number over 5
# numbers = [2, 3, 4, 5, 6, 7, 8]
# squared = {number: number * number for number in numbers if number > 5}
# print(squared)

#create a dictionary containing each number and whether it is even or odd
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_even = {number:"Even" if number %2 == 0 else "Odd" for number in numbers}
# print(odd_even)

#flatten a list of nested lists using comprehension
#the order of the nested lists threw me a bit. think of it as it is written. Get the sublist, get the value
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flat_list = [value for sublist in nested_list for value in sublist]
# print(flat_list)

# #create dictionary with students and average grades
# students = [
#     {"name": "Alice", "grades": [85, 90, 92]},
#     {"name": "Bob", "grades": [78, 80, 88]},
#     {"name": "Charlie", "grades": [95, 92, 98]},
#     {"name": "Diana", "grades": [89, 91, 93]},
# ]
#
# average = {student["name"]: sum(student["grades"]) / len(student["grades"]) for student in students}
# print(average)
#this uses average from numpy.ma when i typed this it automatically imported average so it worked. To do it in normal python/pandas see above
# average_grades = {student["name"]:int(average(student["grades"])) for student in students}
# print(average_grades)


#dictionary containing products costing over 500 with 10% taken off price
# products = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Smartphone", "price": 800},
#     {"product": "Tablet", "price": 450},
#     {"product": "Headphones", "price": 150},
#     {"product": "Smartwatch", "price": 250}
# ]
#
# product_dict = {item["product"]: item["price"] - (item["price"]* 0.10)  for item in products if item["price"] > 500}
# print(product_dict)

#create a dictionare of each person and their income after 15% tax
# people = [
#     {"name": "Alice", "income": 5000},
#     {"name": "Bob", "income": 8000},
#     {"name": "Charlie", "income": 12000},
# ]
#
# post_tax_dict = {person["name"]:person["income"] - (person["income"]*0.15) for person in people}
# print(post_tax_dict)


#dictionary - minor if under 18, adult otherwise
# people = [
#     {"name": "Alice", "age": 17},
#     {"name": "Bob", "age": 21},
#     {"name": "Charlie", "age": 15},
#     {"name": "Diana", "age": 22}
# ]
#
# my_dict = {item["name"]: "Minor" if item["age"] < 18 else "Adult" for item in people}
# print(my_dict)

#create dictionary of the count of each letter
# text = "Hello World" #set creates an unordered collection of each unique character
# my_set = set(text) # eg my_set = {'d', ' ', 'e', 'o', 'r', 'W', 'H', 'l'}
# letter_counts = {letter: text.lower().count(letter) for letter in set(text.lower()) if letter.isalpha()}
# print(letter_counts)

#dictionary of if word is short , med or long
#words = ["apple", "banana", "kiwi", "strawberry", "grape", "mango"]
# word_dict = {word:("short" if len(word) < 5 else "medium" if len(word) < 7 else "long") for word in words }
# print (word_dict)

#dict of pass or fail based on study hours
# study_hours = {
#     "Alice": 5,
#     "Bob": 2,
#     "Charlie": 8,
#     "David": 6,
#     "Eve": 3
# }
#
# study_result = {student:"Pass" if result >= 5 else "Fail" for student,result in study_hours.items()}
# print(study_result)



#dictionary of if students passed based on score
# students_scores = {
#     "Alice": 85,
#     "Bob": 42,
#     "Charlie": 77,
#     "David": 59,
#     "Eve": 90,
#     "Frank": 33
# }
#
# passed_students = {student:score for student,score in students_scores.items() if score >= 60}
# print(passed_students)

