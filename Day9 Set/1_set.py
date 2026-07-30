numbers = {10,20,30,40,50,60}
print (numbers)

numbers.add (80)
print (numbers)

print ("-------------------------------------------------------------------------------------")

# 1. Unordered (Order is not fixed)
numbers = {10, 20, 30, 40, 50}
print(numbers)
# Output: {40, 10, 50, 20, 30} → order is changed!

# 2. Mutable (Set itself can be changed)
numbers = {10, 20, 30}
numbers.add(40)       # added new value
numbers.remove(10)    # deleted a value
print(numbers)
# Output: {20, 30, 40} → Set is changed!

# 3. Heterogeneous (different data types are allowed together)
mixed = {10, "shiv", 3.14, True}
print(mixed)
# Output: {True, 10, 3.14, 'shiv'} → int, string, float, bool together!

# 4. Immutable Elements (elements inside cannot be changed)
numbers = {10, 20, 30}
numbers[0] = 99    # Error!
# TypeError: 'set' object does not support item assignment

# List cannot be added inside Set (because List is mutable)
numbers = {10, 20, [30, 40]}    # Error!
# TypeError: unhashable type: 'list'

# Tuple can be added inside Set (because Tuple is immutable)
numbers = {10, 20, (30, 40)}    # Works!

# 5. Duplicate not allowed
numbers = {10, 20, 20, 30, 30, 10}
print(numbers)
# Output: {10, 20, 30} → duplicates automatically removed!

print ("-------------------------------------------------------------------------------------")
