#-Dictionary_Methods :

details = {"name":"shubham", "age":22}

#Add:---> var [key] = value
details ["city"] = "pune"
print(details)  # {'name': 'shubham', 'age': 22, 'city': 'pune'}
#--------------------------------------------------------------------------------------------------

#var.update (parameter = value):---> (by using update method.)
details.update(course = "Data Analyst", institute = "TKA")
print(details)  # {'name': 'shubham', 'age': 22, 'city': 'pune', 'course': 'Data Analyst', 'institute': 'TKA'}}

details ["course_duration"] = "6 month"
print(details)   
#{'name': 'shubham', 'age': 22, 'city': 'pune', 'course': 'Data Analyst', 'institute': 'TKA', 'course_duration': '6 month'}

details.update(branch = "karvenagar")
print(details)  
