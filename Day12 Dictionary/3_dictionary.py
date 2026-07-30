# Dictionary (Dict):
'''
# Dict: it is comma sep key and value pairs within {}
# syntax:
    var = {k1:v1, k2:v2, ...}
'''

square = {1:1, 2:4, 3:9}
print(type(square))   # <class 'dict'>

details = {"roll":2, "name": "pranav patil", "city":"pune"}
print(type(details))   # <class 'dict'>

# Create a dictionary to represent course details:---->
course = {
    "course_name": "Python Programming",
    "course_id": "CS101",
    "duration": "3 months",
    "instructor": "Pranav Patil",
    "fees": 15000,
    "students_enrolled": 45,
    "start_date": "01-08-2026"
}

print(course)
print(type(course))   # <class 'dict'>


#  Create a dictionary representing cubes of numbers from 11 to 15 :--->
cube = {11:11**3, 12:12**3, 13:13**3, 14:14**3, 15:15**3}
print(cube)

