'''
Section D: Challenging List Tasks
'''
# 36. Merge two lists without using the + operator.
# Method 1:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = []
for item in list1:
    merged.append(item)
for item in list2:
    merged.append(item)
print("36. Merged list:", merged)

# Method 2:
# merged = []
# merged.extend(list1)
# merged.extend(list2)
# print("Merged list:", merged)
#-----------------------------------------------------------------------------------------------

# 37. Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []
for n in list1:
    if n in list2:
        common.append(n)
print("37. Common elements:", common)

# 38. Elements present in list1 but not in list2
only_in_list1 = []
for n in list1:
    if n not in list2:
        only_in_list1.append(n)
print("38. Only in list1:", only_in_list1)

# 39. Rotate a list one position to the right
numbers = [12, 45, 7, 23, 89, 34, 5, 67]
rotated_right = [numbers[-1]] + numbers[:-1]
print("39. Rotated right:", rotated_right)













