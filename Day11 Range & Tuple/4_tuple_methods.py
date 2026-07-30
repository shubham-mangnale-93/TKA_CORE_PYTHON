# Tuple Method: 

# count():------------>

# count() is used to count the number of occurrences of a specified element.
# It returns an integer.
# It does not modify the original tuple.

numbers = (10, 20, 30, 10, 40, 10, 50)

result = numbers.count(10)

print(result)      # 3
print(numbers)     # (10, 20, 30, 10, 40, 10, 50)
#----------------------------------------------------------------------------------

# index():--------------------->

# index() is used to find the index of the first occurrence of a specified element.
# It returns the index position.
# It does not modify the original tuple.

numbers = (10, 20, 30, 40, 50)

result = numbers.index(30)

print(result)      # 2
print(numbers)     # (10, 20, 30, 40, 50)

 