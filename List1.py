# Exercise Level-1:

# 1)
# Declaring an empty list
empty_list = []
print("1. Printing Empty List ::",empty_list)

# 2)
# Declaring a list with more than 5 items of the same data type (integers)
integer_list = [1, 2, 3, 4, 5, 6, 7]
print("2. Printing Integer List ::",integer_list)

# 3)
# Find the length of the list
list = [1, 2, 3, 4, 5, 6, 7]

length_of_list = len(list)
print("3. Length of the list:", length_of_list)

# 4)
my_list = [1, 2, 3, 4, 5, 6, 7]

# the first item
first_item = my_list[0]

# the middle item 
middle_item = my_list[len(my_list) // 2] if len(my_list) % 2 != 0 else None

# the last item
last_item = my_list[-1]

print("4. -First Item:", first_item)
print("   -Middle Item:", middle_item)
print("   -Last Item:", last_item)

# 5)

# Declare a list with mixed data types
mixed_data_types = ["Sneh", 20, 5.5, False, "Anjar-Kutch"]
print("5. Printing Mixed data::",mixed_data_types)

# 6)

# Declare a list variable with initial values
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("6. Printing List Variable::",it_companies)

# 7)
print("7. Printing List Using Print::",my_list)

# 8)
# Get the number of companies in the list
n_companies = len(it_companies)
print("8. Number of companies::", n_companies)

# 9)
print("9. -First Company : ",it_companies[0])
middle_company=len(it_companies)//2
print("   -Middle Company : ",it_companies[middle_company])
print("   -Last Company : ",it_companies[-1])

# 10)

# Modify one of the companies (e.g., the company at index 2)
print("6. Before Modifying ::",it_companies)
it_companies[2] = "New Microsoft"

print("   After Modifying :: ",it_companies)

# 11)
# Add a new IT company to the end of the list
it_companies.append("Agile")
print("11. Adding new Company in IT Companies List:: ",it_companies)

# 12)
# Calculate the middle index
middle_index = len(it_companies) // 2

# Add a new IT company in the middle of the list
it_companies.insert(middle_index, "Googly")
print("12. Adding new IT Company in the Middle of Existing List ::",it_companies)

# 13)
print("13. Printing One Company to Uppercase :: ",it_companies[0].upper())

# 14)
# Join the list with a string using '#; ' separator
join_string = '#; '.join(it_companies)
print(join_string)

# 15)
# Company to check
company_to_check = "Microsoft"

# Check if the company exists in the list
if company_to_check in it_companies:
    print("15. {company_to_check} exists in the list.")
else:
    print("15. {company_to_check} does not exist in the list.")

# 16)
# Sort the list in-place
it_companies.sort()

print("16. Printing Sorted List ::",it_companies)

# 17)
# Reverse the list in-place
it_companies.reverse()
print("17. Printing List in Descending Order ::",it_companies)

# 18)
# Slice out the first 3 companies
slice_three_companies = it_companies[0:3]

print("18. Printing after Sliceing First 3 Items From List ::",slice_three_companies)

# 19)
# Slice out the last 3 companies
last_three_companies = it_companies[-3:]

print("19. Printing after Sliceing Last 3 Items From List ::",last_three_companies)

# 20)
# Calculate the middle index for an even-sized list
middle_index = len(it_companies) // 2

# Sliceign out the middle companies
middle_companies = it_companies[middle_index - 1:middle_index + 1]

print("20. Sliced Companies ::",middle_companies)

# 21)
# Removing the first IT company 
del it_companies[0]
print("21. Removing 1st from the list ::", it_companies)

# 22)
#  Removing middle company or companies from the list
del it_companies[middle_index]
print("22. After Removing middle company ::",it_companies)

# 23)
# Removing the last company from the list
del it_companies[-1]
print("23. After Removing Last Company ::",it_companies)

# 24)
# Remove all IT companies from the list
it_companies.clear()
print("24. Removing all Company from list ::",it_companies)

# 25)
# Destroy the IT companies list
del it_companies[0:]
print("24. Removing all Company from list ::",it_companies)

# 26)
#  Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
merge = front_end+back_end
print("26. After Merging Two List : ",merge)


# 27)

full_stack=merge
full_stack.append("Python")
full_stack.append("SQL")
print("27. Printing Appending values to List : ",full_stack)



# Exercise Level-2:
# 1. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# -

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting the list
ages.sort()

# Finding the minimum and maximum ages
min_age = min(ages)
max_age = max(ages)

# Printing the sorted list, minimum age, and maximum age
print("Sorted Ages:", ages)
print("Minimum Age:", min_age)
print("Maximum Age:", max_age)

# Exercise Level-2:

# 1. The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# -

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sorting the list
ages.sort()

# Finding the minimum and maximum ages
min_age = min(ages)
max_age = max(ages)

# Printing the sorted list, minimum age, and maximum age
print("1. Sorted Ages ::", ages)
print("   Minimum Age ::", min_age)
print("   Maximum Age ::", max_age)

# - Add the min age and the max age again to the list

# Add the min and max ages back to the list
ages.append(min_age)
ages.append(max_age)

print("2. Updated Ages List ::", ages)

# - Find the median age (one middle item or two middle items divided by two)
median_age=len(ages)//2
print("3. Printing Median Age :: ",ages[median_age])

# - Find the average age (sum of all items divided by their number )

# Calculating the sum of all and average age
average_age = sum(ages)//len(ages)
print("4. Average Age ::", average_age)

# - Find the range of the ages (max minus min)

# Calculating the range
ages.sort()
age_range = ages[-1] - ages[0]
print("5. Finding Range : ",age_range)

# - Compare the value of (min - average) and (max - average), use abs() method

n1 = abs(ages[0]-average_age)
n2 = abs(ages[-1]-average_age)
print(" 6. Minimum Average ::",n1)
print("    Maximum Average ::",n2)

# - Find the middle country(ies) in the [countries list]

countries=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

num_countries = len(countries)

# Find the middle index or indices
middle_index = num_countries // 2
print("7. Middle Country is : ",middle_index)

# -Find the middle country(ies) in the [countries list]

first_half=countries[:middle_index]
sec_half=countries[middle_index:]
if len(first_half)<len(sec_half):
    first_half.append("India")
print("8. First Half Of Company ::",first_half)
print("   Second Half Of Country::",sec_half)

# - ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
scandic=countries[3:]
print("9. Scandic Countries Are : ",scandic)