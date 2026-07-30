courses = ["Data science","Data Analyst","Power Bi","AWS"]
#Access
print(courses[-2])
print(courses[:-2])

#Add
courses.append("python")
print(courses)

courses.insert(0,"MySql")
print(courses)

#update
courses = ["Data science","Data Analyst","Power Bi","AWS"]
courses [-2] = "P-BI"
print(courses)

courses [0:2:1] = ["DS","DA"]
print(courses)

#delete
courses = ["Data science","Power BI","Data Analyst","Power BI","AWS"]
courses.remove ("AWS")
print(courses)

courses.pop(-3)
print(courses)

#del
courses = ["Data science","Power BI","Data Analyst","Power BI","AWS"]
 
del courses[1]
print (courses)

del courses [1:-1:1]
print(courses)