
'''
#Add :
var[key] = value    or    var.update(k=value)    or    var.update(dict)

#access
var[key]    or    var.get()

#delete
var.pop(key)    or    var.popitem()

#update
var[key] = uvalue    or    var.update(k=uvalue)
'''

details = {
    "name": "Shubham Mangnale",
    "age": 22
}

# Add
details["city"] = "Pune"
print(details)

details.update(country="India")
print(details)

details.update({"State": "Maharadhtra", "skills": ["Python", "Java"]})
print(details)
#------------------------------------------------------------------------------------------------

# Access
print(details["name"])      # Shubham Mangnale
print(details.get("age"))   # 22
#------------------------------------------------------------------------------------------------

# Delete
details.pop("city")
print(details)

details.popitem()
print(details)
#------------------------------------------------------------------------------------------------

# Update
details["age"] = 23
details.update(name="Shubham S. Mangnale")

print(details)


