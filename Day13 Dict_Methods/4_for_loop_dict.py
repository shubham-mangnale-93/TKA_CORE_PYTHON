# Initial dictionary
course_details = {"course": "DA", "Duration": "4 month", "Trainer name": "vaibhav"}

# 1. Loops through keys by default
for i in course_details:
    print(i)
# Output:
# course
# Duration
# Trainer name

# 2. Loops through values only
for i in course_details.values():
    print(i)
# Output:
# DA
# 4 month
# vaibhav

# 3. Loops through key-value pairs as tuples
for i in course_details.items():
    print(i)
# Output:
# ('course', 'DA')
# ('Duration', '4 month')
# ('Trainer name', 'vaibhav')

# 4. Unpacks key (i) and value (j), then prints only values
for i, j in course_details.items():
    print(j)
# Output:
# DA
# 4 month
# vaibhav


