#Write a Python program using a for loop to print the word "Hello" 5 times.
for i in range(5):
    print("hello")

#Write a Python program using a for loop to print each character of the following string on a new line.
name = 'PYTHON'
for ch in name:
    print(ch)  

#Write a Python program using a for loop to print each character of the string along with its position.
name = 'PYTHON'
position = 1
# position = 0
for ch in name:
    # position = position + 1
    print(position,ch)
    position = position + 1

#Print Each Student Name with "Hello"
student = ["sham","ram","kavya","manas"]
for name in student:
    print(f"Hello,{name}")

#Write a Python program using a for loop to print the square of each number from the list below.
numbers = [2, 4, 6, 8]
for num in numbers:
    Square = num*num
    print(f"square of {num} is {Square}")   

#Write a Python program using a for loop to multiply each number in the list by 10 and print the result.
numbers = [5, 10, 15, 20]
for num in numbers:
    print(num*10)    

#Write a Python program using a for loop to find the sum of all numbers in the list.
numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
     total = total + num
     print(num)        
print("Total Sum =", total)  

#
data = [10, "Python", 5.5, True]
for l in data:
    print(type(l))