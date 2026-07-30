student_marks = {"om patil":79,"umesh wagh":20,"prathmesh gandhi":79,"pratik tayade":67,
                 "rahul bhoyar":31,"suraj chavan":90,"vijay chopde":23}

# wap to list of all name:
students = []
for name in student_marks:
    # print(name)
    students.append(name)
print(students)

# wap to print list of all marks:
marks =[]
for m in student_marks.values():
    # print(m)
    marks.append(m)
print(marks)    
#--------------------------------------------------------------------------------------

# wap to print name of pass student ---->list---->mk>40
list=[]
for name,mk in student_marks.items():
    if mk>40:
        list.append(name)
print(list) 

#---------------------------------------------------------------------------------

#wap to print list -->fail and set of pass

student_marks = {"om patil":79,"umesh wagh":20,"prathmesh gandhi":79,"pratik tayade":67,
                 "rahul bhoyar":31,"suraj chavan":90,"vijay chopde":23}

fail = []
pass_set = set ()

for name, marks in student_marks.items():
    if marks < 35:
        fail.append(name)
    else:
        pass_set.add(name)

print("Fail list:", fail)
print("Pass set:", pass_set)
#---------------------------------------------------------------------------------

# wap to print dict of final result----> {"om":"pass", "umesh wagh":"fail".....}

student_marks = {"om patil":79,"umesh wagh":20,"prathmesh gandhi":79,"pratik tayade":67,
                 "rahul bhoyar":31,"suraj chavan":90,"vijay chopde":23}

result = {}
for name,mk in student_marks.items():
    if mk>40:
        result[name]="pass"
    else:
        result[name]='fail'

print("final_result: ",result) 
#-------------------------------------------------------------------------------------

employee_salary = {"om patil":79000,"umesh wagh":20000,"prathmesh gandhi":79000,"pratik tayade":67000,
                   "rahul bhoyar":31000,"suraj chavan":90000,"vijay chopde":23000}
# 50k---->count
count = 0
for salary in employee_salary.values():
    # print (salary)
     if salary < 50000:
        count += 1
        print(salary)

print("Count of employees with salary < 50k:", count)


count_gt = 0
count_lt = 0
for salary in employee_salary.values():
    # print (salary)
     if salary > 50000:
        count_gt += 1
        # print(salary)
     else:
         if salary < 50000:
          count_lt += 1
        #   print(salary)
        
print("Count of employees with salary > 50k:", count_gt)
print("Count of employees with salary < 50k:", count_lt)
#-------------------------------------------------------------------------------------

employee_salary = {"om patil":79000,"umesh wagh":20000,"prathmesh gandhi":79000,"pratik tayade":67000,
                   "rahul bhoyar":31000,"suraj chavan":90000,"vijay chopde":23000}

# new_emp_sal = {}    #after 10% increment
new_emp_sal = {}
for name,salary in employee_salary.items():
    increment = salary * 10/100
    new_sal = salary + increment
    # print(new_sal)
    new_emp_sal [name] = new_sal
print(increment)        
print(new_emp_sal)    

# new_emp_sal = {}    #after 10% increment
# for name, salary in employee_salary.items():
#     new_emp_sal[name] = salary + (salary * 0.10)

# print(new_emp_sal)