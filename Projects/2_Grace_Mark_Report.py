'''
# Project Requirement:------------------>>>>

Suppose:
Total Marks = 60
Passing Marks = 20
Every student has 5 subjects
'''
'''
# Rule:--------------------->>>>
  A student gets grace marks only if:
: They fail in exactly one subject.
: Their marks in that subject are 16, 17, 18, or 19 (1-4 marks short of passing).

Passing Marks = 20
''' 
# Data:---------------->>>>>>
students = [
    {
        "name": "Rahul",
        "marks": [25, 18, 30, 22, 40]
    },
    {
        "name": "Amit",
        "marks": [20, 21, 22, 23, 24]
    },
    {
        "name": "Priya",
        "marks": [19, 35, 30, 40, 50]
    },
    {
        "name": "Rohan",
        "marks": [17, 25, 28, 30, 35]
    },
    {
    "name": "Akash",
    "marks": [15, 25, 28, 30, 35]
},
{
    "name": "Sagar",
    "marks": [18, 19, 28, 30, 35]
},
{
    "name": "Sneha",
    "marks": [22, 24, 26, 20, 21]
},
{
    "name": "Pooja",
    "marks": [16, 25, 30, 40, 45]
},
{
    "name": "Karan",
    "marks": [14, 18, 25, 30, 40]
},
{
    "name": "Neha",
    "marks": [19, 21, 23, 24, 28]
},
{
    "name": "Vikas",
    "marks": [20, 20, 20, 20, 20]
},
{
    "name": "Anjali",
    "marks": [12, 15, 30, 35, 40]
},
{
    "name": "Riya",
    "marks": [18, 25, 20, 30, 45]
},
{
    "name": "Om",
    "marks": [17, 18, 19, 25, 30]
},
{
    "name": "Meena",
    "marks": [35, 38, 40, 42, 45]
},
{
    "name": "Ajay",
    "marks": [16, 20, 25, 30, 35]
},
{
    "name": "Nikita",
    "marks": [19, 20, 21, 22, 23]
},
{
    "name": "Ramesh",
    "marks": [10, 20, 30, 40, 50]
},
{
    "name": "Kavita",
    "marks": [18, 22, 24, 26, 28]
},
{
    "name": "Yash",
    "marks": [13, 14, 20, 25, 30]
},
{
    "name": "Sakshi",
    "marks": [17, 23, 27, 29, 31]
},
{
    "name": "Aditya",
    "marks": [20, 18, 22, 25, 28]
},
{
    "name": "Komal",
    "marks": [19, 35, 40, 45, 50]
},
{
    "name": "Rutuja",
    "marks": [11, 19, 21, 25, 30]
}
]


print("========== STUDENT GRACE MARKS REPORT ==========\n")

PASS_MARK = 20
for student in students:

    fail_count = 0
    failed_mark = None
    failed_index = -1

    # Check all 5 subjects
    for i in range(len(student["marks"])):
        # print("-----------",i)

        mark = student["marks"][i]
        print("----------->>",mark)

        if mark < PASS_MARK:
            fail_count += 1
            failed_mark = mark
            failed_index = i

    print("Student Name :", student["name"])
    print("Original Marks :", student["marks"])
    print("Fail_Count :", fail_count)
    print("Failed Mark :", failed_mark)
    print("Failed Index :", failed_index)

    # Grace Marks Logic
    if fail_count == 1:

        if failed_mark >= 16 and failed_mark <= 19:

            grace = PASS_MARK - failed_mark

            student["marks"][failed_index] += grace

            print("Grace Marks Given :", grace)
            print("Updated Marks :", student["marks"])
            print("Final Result : PASS")

        else:

            print("Grace Marks : Not Eligible")
            print("Reason : Student needs more than 4 grace marks.")

    elif fail_count > 1:

        print("Grace Marks : Not Eligible")
        print("Reason : Student failed in more than one subject.")

    else:

        print("Grace Marks : Not Required")
        print("Reason : Student already passed in all subjects.")

    print("-" * 50)
     

















