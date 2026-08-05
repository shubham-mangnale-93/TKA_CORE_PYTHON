numbers = [12, 45, 7, 23, 45, 69 , 70, 89, 12, 34, 5, 67]

# 16. Create a new list containing the square of every number.
squares = []
for num in numbers:
    sq = num*num
    squares.append(sq)
print("16.List of Square:",squares)    

# 17. Create a new list containing only numbers greater than 30
greater_than_30 = []
for n in numbers:
    if n > 30:
        greater_than_30.append(n)
print("17.Numbers greater than 30:", greater_than_30)

# 18. Print the list in reverse order without using reverse().
reversed_list = numbers[::-1]
print("18.Reversed list:", reversed_list)

# 19. Find the second-largest number.
unique_number = list(set(numbers))
unique_number.sort()
print("19.Second-largest Number:",unique_number[-2])

# 20. Find the second-smallest number
# unique_number = list(set(numbers))
# unique_number.sort()
print("20.Second smallest:", unique_number[1])

# 21. Count how many times each number appears.
# count_dict = {}
for num in numbers:
    c = numbers.count(num)      # list.count(value)- use like this
    print(num, "->", c)

# 22. Separate the numbers into two lists: even numbers and odd numbers.
even_numbers = []
odd_numbers = []
for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print("22.Even numbers:", even_numbers)
print("   Odd numbers:", odd_numbers)

# 23. Find all duplicate elements.
duplicates = []
for n in numbers:
    c = numbers.count(n)
    # print(n,c)
    if c > 1:
        duplicates.append(n)
print("23.Duplicate elements:", duplicates)

# 24. Find all elements that appear only once.
result = []
for n in numbers:
    c = numbers.count(n)
    if c == 1:
        result.append(n)
print("24.Elements appearing only once:", result)

# 25. Replace every number smaller than 20 with 0.
new_list = []
for n in numbers:
    if n < 20:
        new_list.append(0)
    else:
        new_list.append(n)
print("25.Updated list:", new_list)











