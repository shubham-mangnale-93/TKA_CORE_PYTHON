# WAP to create dict of square of all numbers

numbers = [1, 2, 3, 4, 5, 6, 7]

square = {}

for num in numbers:
    sq = num**2
    square[num] = sq

print(square)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
#---------------------------------------------------------------------------------------------

#wap to cal percentage :--->

marks = {"python":67,"java":78,"testing":88,"cpp":90}

total_obtained = 0

# loop through all marks to calculate total
for m in marks.values():
    print("value--->",m)
    total_obtained = total_obtained + m

# 4 subjects * 100 maximum marks each
out_of_marks = len(marks) * 100

# calculate percentage
percentage = (total_obtained / out_of_marks) * 100

print("Total Marks:", total_obtained)
print("Out of Marks--->",out_of_marks)
print("Percentage:", percentage, "%")
# Output:
# Total Marks: 323
# Out of Marks---> 400
# Percentage: 80.75 %
#---------------------------------------------------------------------------------------------
 