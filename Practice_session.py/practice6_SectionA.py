numbers = [12,45,7,23,45,89,12,34,5,67]

# Section A: Basic List Tasks:---------------->>>>>>

# 1.Print all elements from the list.
print("1.",numbers)

# 2.Print the first and last element.
print("2.",numbers[0],numbers[-1])

# 3.Find the total number of elements without manually counting them
print("3.",len(numbers))

# 4.Calculate the sum of all elements
print("4.",sum(numbers))

# 5.Find the largest and smallest number.
print("5.","Largest Num:",max(numbers),"Smallest Num:",min(numbers))

# 6.Print all even numbers
even_num = []
for n in numbers:
    if n % 2 == 0:
        even_num.append(n)
print("6. All Even Numbers:",even_num)

numbers = [12, 45, 7, 23, 45, 89, 12, 34, 5, 67]

# 7.Print all odd numbers.
odd_num = []
for n in numbers:
    if n % 2 != 0:
        odd_num.append(n)
print("7. All Odd Numbers:", odd_num)

# 8.Count how many even and odd numbers are present
even_count = 0
odd_count = 0 
for num in numbers:
    if num%2==0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f"8. Even count: {even_count} and Odd count:{odd_count}")

# 9.Check whether 23 exists in the list.
if 23 in numbers:
    print("9. 23 exists in the list")
else:
    print("9. 23 does not exist in the list")

# 10.Find the index position of 89    
numbers = [12, 45, 7, 23, 45, 89, 12, 34, 5, 67]
print("10. Index position of 89:", numbers.index(89))

# 11.Add 100 at the end of the list.
numbers.append(100)
print("11.List after adding 100:",numbers)

# 12.Insert 50 at index position 3
numbers.insert(3,50)
print("12.Insert 50 at index position 3:",numbers)

# 13.Remove the first occurrence of 45.
numbers.remove(45)
print("13.List after removing first 45:", numbers)

# 14.Remove duplicate values from the list:
unique_numbers = list(set(numbers))
print("14.remove duplicates values:",unique_numbers)

# 15.Sort the list in ascending and descending order
numbers.sort()  
print("15.ascending order:",numbers)
numbers.sort(reverse=True)
print("   descending order:",numbers)
numbers = [12, 45, 7, 23, 45, 89, 12, 34, 5, 67]

# print(f'Ascending order: {sorted(numbers)}')
# print(f'Descending order: {sorted(numbers, reverse=True)}')

print("<<__Section 1 Done All Task!__>>".center(80,"-"))
#--------------------------------------------------------------------------------------------------

'''
Section B: Logical List Tasks
'''

# 16.Create a new list containing the square of every number.




