# Exercise: Day 8

# 1. Create  an empty dictionary called dog
dog= {}
print("Empty dict ::",dog)

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'Name':'Winnie','Color':'White','breed':'Street Dog','legs': 4,'age':1}
print("dictionaries after filling details ::",dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Sneh','last_name':'Kandoi','gender':'male','age':20,'marital status':'unmarried','skills':'Web developer','country':'India','address':'Anjar-Kutch'}
print("Student Dictonarie ::",student)

# 4. Get the length of the student dictionary
print("length of Student Dictonarie ::",len(student))

# 5. Get the value of skills and check the data type, it should be a list
print("Getting Skill ::",student['skills'])
print("Data type of skills ::",type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills']="Volleyball","Cricket"
print("Modifiying the skills of student ::",student)

# 7. Get the dictionary keys as a list
all_key = list(student.keys())
print("All Keys after Transfer as List ::",all_key)

# 8. Get the dictionary values as a list
all_value = list(student.values())
print("All Values after Transfer as List ::",all_value)

# 9. Change the dictionary to a list of tuples using _items()_ method
list1=student.items()
print("Changing the List to Tuples ::",list1)

# 10. Delete one of the items in the dictionary
del student['address']
print("Deleting last name from Dict ::",student)

# 11. Delete one of the dictionaries
empty = {}
del empty
