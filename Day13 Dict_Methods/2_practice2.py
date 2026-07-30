#-How to Access data in dectionary :

details = {"name":"shubham", "age":22}

# var [key]:---> (return value)
print(details["name"])
print(details["age"])
#--------------------------------------------------------------------------------------------------

# var.get:--->
print(details.get("name"))
print(details.get("age","no data"))
print(details.get("course","No Data"))  # it retunrs none, its not present.
#--------------------------------------------------------------------------------------------------

# Delete:--->
# var.pop:
details = {"name":"shubham", "age":22}
print(details.pop("name")) # shubham
print(details) # {'age': 22}

# var.popitem():
details = {"name":"shubham", "age":22}
print(details.popitem()) # ('age', 22)
print(details) # {'name': 'shubham'}
#--------------------------------------------------------------------------------------------------

# update:--->

#var[key] = uvalue
#var.update(key = uvalue)

details = {"name":"Vaibhav Patil","age":26}

details["age"] = 27
details.update(name = "vaibhav s patil")
print(details)
#--------------------------------------------------------------------------------------------------
 
# clear, copy :--->

# Initial dictionary
details = {"name": "Vaibhav Patil", "age": 26}

# 1. copy() Method - Creates a duplicate copy of the dictionary
new_details = details.copy()
print("Copied Dictionary:", new_details)
# Output: {"name": "Vaibhav Patil", "age": 26}

# 2. clear() Method - Removes all elements, making the dictionary empty
details.clear()
print("Cleared Original Dictionary:", details)
# Output: {}
#--------------------------------------------------------------------------------------------------

# keys, values, items :--->

details = {"name":"Vaibhav Patil","age":26}
print(details.keys()) #dict_keys(['name', 'age'])
print(details.values()) #dict_values(['Vaibhav Patil', 26])
print(details.items()) #dict_items([('name', 'Vaibhav Patil'), ('age', 26)])
#--------------------------------------------------------------------------------------------------

# setdefault :--->
# dict.setdefault(key, default_value)

details = {
    "name": "Shubham Mangnale",
    "age": 22
}

city_value = details.setdefault("city", "Pune")

print(details)     # Output: {'name': 'Shubham Mangnale', 'age': 22, 'city': 'Pune'}
print(city_value)  # Output: Pune (Mhanje ha method tya key chi value return karto)

# print(details.setdefault("city", "Pune"))  # Output: Pune (Mhanje ha method tya key chi value return karto)
# print(details) # Output: {'name': 'Shubham Mangnale', 'age': 22, 'city': 'Pune'}

# age_value = details.setdefault("age", 25)

# print(details)    # Output: {'name': 'Shubham Mangnale', 'age': 22, 'city': 'Pune'}
# print(age_value)  # Output: 22 (Juni valuech parat milali)
#--------------------------------------------------------------------------------------------------









