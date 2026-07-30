numbers = [11, 22, 333, 44, [10, 20, [1, 2, 3, 4, 5], 30, 20, 50, 666], 55, 66]

# Step 1: Added 77 at the end
numbers.append(77)
print(numbers)
# [11, 22, 333, 44, [10, 20, [1, 2, 3, 4, 5], 30, 20, 50, 666], 55, 66, 77]

# Step 2: Replaced 333 with 33
numbers[2] = 33
print(numbers)
# [11, 22, 33, 44, [10, 20, [1, 2, 3, 4, 5], 30, 20, 50, 666], 55, 66, 77]

# Step 3: Replaced 666 with 60
numbers[4][6] = 60
print(numbers)
# [11, 22, 33, 44, [10, 20, [1, 2, 3, 4, 5], 30, 20, 50, 60], 55, 66, 77]

# Step 4:  remove 20
numbers[4].pop(4)
print(numbers[4])
# [10, 20, [1, 2, 3, 4, 5], 30, 50, 60]

# Step 5: Added 5 before 10
numbers[4].insert(0, 5)
print(numbers[4])
# [5,10,20,[1,2,3,4,5],30,50,60]

# Step 6: Added 6 after 5
numbers[4].insert(1, 6)
print(numbers[4])
# [5,6,10,20,[1,2,3,4,5],30,50,60]
