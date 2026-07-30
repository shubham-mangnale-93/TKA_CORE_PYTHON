# num = [10,20,30,40,50,60,70,80,90]

# print(num[:4])
# print(num[:-4:-1])
# print(num[5:])
# print(num[2::-1])
# print(num[-7:])
# print(num[::-1])
#------------------------------------------------------------------------

#Nested list :
numbers = [10,20,30,40,[11,22,33,[1,2,3,4,5,6],44,55],50,60,70,80]

#indexing :
# print (numbers)
# print (numbers[-4])
# print (numbers[-5] [-1])
# print (numbers[4][1])
# print (numbers[4] [3] [2])

#slicing :
print(numbers[-4:-1])
print(numbers[2::-1])
print (numbers[4][:3])
print (numbers[4][-2::-2])
print (numbers[-5][-2::-2])
print (numbers[4][-3][::-1])
print (numbers[4][-3][::-2])

#-----------------------------------------------------------------------------------------------
l = [[[[["rajeshkumar"]]]]]
# print (l[0])
# print (l[0] [0])
# print (l[0] [0] [0])
print(l[0][0][0][0][0])
name = l[0][0][0][0][0] 
print(name[0] + name[1] + name[8:9])
print(f"{name[0]}{name[1]}{name[-3]}")

word =  l[0][0][0][0][0] 
ram = word[0] + word[1] + word[8]
print(ram)
#------------------------------------------------------------------------------------------------

