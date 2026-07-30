# Nested List containing 3 groups of students

liststu = [['kanchan', 'kiran', 'mahesh'],['shruti', 'pruthvi', 'saiyee'],['kavya', 'shubhangi', 'kanika']]


# Initialize group number
group_num = 0

# Outer loop: Iterate through each group
for stugroup in liststu:

    # Reset count for every new group
    count = 0

    # Increment group number
    group_num = group_num + 1

    # Display current group number and group members
    # print("Group Number -->", group_num, stugroup)

    # Inner loop: Iterate through each student in the current group
    for stuname in stugroup:

        # Display current student name
        # print("Student Name -->", stuname)

        # Check if the student's name starts with 'k'
        if stuname.startswith('k'):

            # Increment count if the condition is True
            count = count + 1

            # Display students whose names start with 'k'
            # print("Starts with 'k' -->", stuname)

    # Display the final count for the current group
    print("Final Count -->", group_num, "------", count)