'''
Basic Dictionary Tasks:--->>
'''
student = {
 "name": "Rahul",
 "age": 22,
 "course": "Python",
 "city": "Pune",
 "marks": 78
}

# 1. Print the complete dictionary.
print("1.", student)

# 2. Print only the student's name.
print("2.", student["name"])

# 3. Print the value of the course key.
print("3.", student["course"])

# 4. Display all dictionary keys.
print("4.", student.keys())

# 5. Display all dictionary values.
print("5.", student.values())

# 6. Display all key-value pairs.
print("6.", student.items())

# 7. Find the total number of key-value pairs.
print("7.", len(student))

# 8. Check whether the key "city" exists.
if "city" in student:
    print("8. 'city' does exists")
else:
    print("8. 'city' does not exists")

# 9. Add a new key "email" with any email address.
student["email"] = "rahulp787@gmail.com"
print("9.", student)

# 10. Update the marks from 78 to 85.
student["marks"] = 85
print("10.", student)

# 11. Change the city from Pune to Mumbai.
student["city"] = "Mumbai"
print("11.", student)

# 12. Remove the age key from the dictionary.
student.pop("age")
print("12.", student)

# 13. Use get() to display the value of the phone key without causing an error
print("13.", student.get("phone","key not found"))

# 14. Create a copy of the dictionary.
copy = student.copy()
print("14.", copy)

# 15. Clear all elements from the copied dictionary
copy.clear()
print(copy)
#--------------------------------------------------------------------------------------------------