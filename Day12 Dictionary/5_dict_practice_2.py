# Create a dictionary to represent states and their capitals. :--->

state_capital = {
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur",
    "Kerala": "Thiruvananthapuram",
    "Punjab": "Chandigarh",
    "West Bengal": "Kolkata",
    "Uttar Pradesh": "Lucknow",
    "Madhya Pradesh": "Bhopal"
}

print(state_capital)
print(type(state_capital))   # <class 'dict'>
#--------------------------------------------------------------------------------------------

# Create a dictionary to represent programming languages (Java, Python, C) and their creators.:--->
lang_creators = {
    "Java": ["James Gosling"],
    "Python": ["Guido van Rossum"],
    "C": ["Dennis Ritchie"],
    "C++": ["Bjarne Stroustrup"],
    "R": ["Ross Ihaka", "Robert Gentleman"] 
}

print(lang_creators)
#---------------------------------------------------------------------------------------------

# Create a dictionary to represent single employee details:--->
employee = {
    "emp_id": 101,
    "name": "Pranav Patil",
    "department": "IT",
    "designation": "Software Developer",
    "salary": 45000,
    "email": "pranav.patil@company.com",
    "phone": 9876543210,
    "experience": 3,
    "skills": ["Python", "Java", "SQL"],
    "is_permanent": True
}

print(employee)
print(type(employee))   # <class 'dict'>
#---------------------------------------------------------------------------------------------

department = {
    "placement": {
        "emp1": {
            "name": "Pranav Patil",
            "designation": "Placement Officer",
            "salary": 45000,
            "skills": ["Communication", "HR"]
        },
        "emp2": {
            "name": "Kunal Kale",
            "designation": "Placement Coordinator",
            "salary": 38000,
            "skills": ["Networking", "Excel"]
        },
        "emp3": {
            "name": "Vijay Sharma",
            "designation": "Assistant Placement Officer",
            "salary": 32000,
            "skills": ["Documentation", "Communication"]
        }
    }
}

print(department)
print(type(department))   # <class 'dict'>
#---------------------------------------------------------------------------------------------

placement_dep = {
    "p101": {"name": "rahul", "salary": 50000},
    "p102": {"name": "om", "salary": 40000}
}
#---------------------------------------------------------------------------------------------

#Create a dictionary to represent a single student's data with name and percentage.
student = {"name": "Pranav Patil", "percentage": 87.5}

print(student)
print(type(student))   # <class 'dict'>
#---------------------------------------------------------------------------------------------

#Create a nested dictionary to represent student data (roll number as key, and name & percentage as value) for a batch of students.
batch_1336 = {
    1: {"name": "om", "per": 78},
    2: {"name": "umesh", "per": 89},
    3: {"name": "rahul", "per": 67}
}
#---------------------------------------------------------------------------------------------

# Create a nested dictionary using department name as the key, and employee details (name, salary) as the value.:---->

company = {
    "department": {
        "IT": {
            "emp1": {"name": "Pranav", "salary": 45000},
            "emp2": {"name": "Kunal", "salary": 42000}
        },
        "HR": {
            "emp1": {"name": "Sneha", "salary": 38000},
            "emp2": {"name": "Amit", "salary": 40000}
        },
        "Sales": {
            "emp1": {"name": "Rahul", "salary": 35000},
            "emp2": {"name": "Om", "salary": 36000}
        }
    }
}

print(company)
#---------------------------------------------------------------------------------------------

# Create a nested dictionary to represent departments and their employees' details (name, salary).
tka_emp = {
    "placement": {
        "p101": {"name": "ram", "sal": 78000},
        "p102": {"name": "ramesh", "sal": 78897}
    },
    "sales": {
        "s101": {"name": "ram", "sal": 78},
        "s102": {"name": "ram", "sal": 78}
    }
}
print (tka_emp )
#---------------------------------------------------------------------------------------------


