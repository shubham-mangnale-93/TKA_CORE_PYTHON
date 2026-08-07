'''
Logical and Nested Dictionary Tasks:--------->>>>
'''
employees = {
 101: {"name": "Amit", "department": "IT", "salary": 45000},
 102: {"name": "Priya", "department": "HR", "salary": 38000},
 103: {"name": "Sneha", "department": "IT", "salary": 52000},
 104: {"name": "Raj", "department": "Sales", "salary": 41000},
 105: {"name": "Anjali", "department": "HR", "salary": 47000}
}
#--------------------------------------------------------------------------------------------------

# 16. Print the name of every employee.
for emp_id,details in employees.items():
    print(details ["name"])
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 17. Print employee ID with employee name.
for emp_id,details in employees.items():
    print(f"Emp Id: {emp_id} : {details ["name"]}" )
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 18. Print employees who belong to the IT department.
for emp_id,details in employees.items():
    if details["department"] == "IT":
        # print(details)
        print(emp_id, "-", details["name"])        
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 19. Print employees whose salary is greater than 40,000.
for emp_id,details in employees.items():
    if details["salary"]>40000:
        # print(details)
        print(emp_id, "-", details["name"], "-", details["salary"])        
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 20. Find the employee with the highest salary.
highest_salary = 0
# highest_emp = None
for emp_id,details in employees.items():
    if details["salary"]> highest_salary:
        highest_salary = details["salary"]     
        # highest_emp = (emp_id, details["name"])  
# print(highest_emp, "-", highest_salary)  
print("20.employee with the highest salary:",emp_id, '-', details["name"], '-', highest_salary)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 21. Find the employee with the lowest salary.
lowest_salary = 100000
for emp_id,details in employees.items():
    if details["salary"]  < lowest_salary:
        lowest_salary = details["salary"]       
print("21.employee with the lowest salary:",emp_id, '-', details["name"], '-', lowest_salary)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 22. Calculate the total salary of all employees.
total_salary = 0
for emp_id,details in employees.items():
    total_salary = total_salary + details["salary"]
print("22.Total Salary: ",total_salary)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 23. Calculate the average salary of all employees.
print("23.Average salary of all emp:", total_salary/len(employees))
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 24. Count how many employees are present in each department.
dept_count = {}
count_dept = 0
for emp_id, details in employees.items():
    dept = details["department"]
    count_dept = count_dept + 1
    dept_count [dept] = count_dept   
print("24. employees are present in each department:",dept_count)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 25. Increase the salary of every employee by 10%.
for emp_id, details in employees.items():
    salary = details["salary"]
    per_sal = salary*10/100
    inc_salary = salary + per_sal      
    # details["salary"] = inc_salary   # this line update original dict
    print(inc_salary)
# print(employees)    # original dict not update  
print("--"*30)
#--------------------------------------------------------------------------------------------------
     
# 26. Create a new dictionary containing employee names and salaries.
new_dict = {}
for emp_id, details in employees.items():
    new_dict[details["name"]] = details["salary"]
print("new dict containing employee names and salaries:",new_dict)    
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 27. Create a new dictionary containing only HR employees.
new_dict = {}
for emp_id, details in employees.items():
    if details["department"]=="HR":
        new_dict[emp_id] = details  
print(new_dict)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 28. Find whether employee ID 103 exists.
if 103 in employees:
    print("28.Emp id 103 - does exists")
else:
    print("Emp id 103 does - not exists")
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 29. Remove employee ID 104 from the dictionary.
del employees[104]
print("Remove employee ID 104:",employees)
print("--"*30)
#--------------------------------------------------------------------------------------------------

# 30. Add a new employee with ID 106.
employees[106] = {"name": "Vikram", "department": "Finance", "salary": 50000}
print("30.Add new emp id 106:",employees)
print("--"*30)
#--------------------------------------------------------------------------------------------------
# employees[108] = None   #{}   
# print(employees)