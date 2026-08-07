'''
Section C: String List Tasks
'''
students = ["Rahul", "Priya", "Amit", "Sneha", "Raj", "Anjali"]

# 26. Print all student names
# for name in students:
#     print(name)
print("26.", students)

# 27. Print names that start with "A".
start_a = []
for n in students:
    if n.startswith("A"):
        start_a.append(n)
print("27.", start_a)

# 28. Print names containing more than five characters
more_than_5 = []
for n in students:
    if len(n) > 5:
        more_than_5.append(n)
print("28.", more_than_5)

# 29. Convert every name to uppercase
upper_names = []
for n in students:
    uppercase = n.upper()
    upper_names.append(uppercase)
print("29.", upper_names)

# 30. Sort the names alphabetically
sorted_names = sorted(students)
print("30.", sorted_names)

# 31. Find the longest student name
longest = students[0]
for n in students:
    if len(n) > len(longest):
        longest = n
print("31. Longest name:", longest)

# 32. Check whether "Sneha" exists in the list
print("32.", "Sneha" in students)

# 33. Create a new list containing the length of every name
lengths = []
for n in students:
    l = len(n)
    lengths.append(l)
print("33. Length of every name:",lengths)

# 34. Remove "Raj" from the list.
students = ["Rahul", "Priya", "Amit", "Sneha", "Raj", "Anjali"]

students.remove("Raj")
print("34. List after removing Raj:", students)

# 35. Print all names in reverse alphabetical order.
students.sort(reverse=True)
print("35. Reverse alphabetical order:", students)
