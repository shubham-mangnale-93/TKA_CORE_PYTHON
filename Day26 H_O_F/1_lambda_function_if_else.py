# def check(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"

#------------------------------------------------------------------------------------------------
# lambda function in if else using:----->>

check = lambda num: "Even" if num%2==0 else "Odd"
print(check(6))
#------------------------------------------------------------------------------------------------

# create a function to check number is divisible by 10 or not:----->>
check = lambda num: "Number is divisible by 10" if num%10==0 else "Number is not divisible by 10"
print(check(10))
print(check(52))
print(check(100))
#------------------------------------------------------------------------------------------------
'''
Q. Write a program (using lambda function) to calculate the discount 
   on a given bill amount, such that:
   
   - If bill_amount > 10000  --> 10% discount is applied
   - If bill_amount <= 10000 --> 5% discount is applied
   
   Print the final amount after applying the discount.
'''

apply_discount = lambda bill_amount : bill_amount-bill_amount*10/100 if bill_amount>10000 else bill_amount-bill_amount*5/100

print(apply_discount(12000))
#------------------------------------------------------------------------------------------------

# create a function to check pass or fail:---->>

check = lambda marks: "Pass" if marks>=90 else "Fail"
print(check(89)) #fail
print(check(90)) #pass
print(check(45)) #fail

grade = lambda marks: "A" if marks>=90 else "B" if marks>=70 else "C" if marks>=50 else "fail"
#------------------------------------------------------------------------------------------------
 
'''
filter(fun,iterable)
'''
#wap to check whose length is less than 4 characters, using the filter() function and a lambda expression.:--->>
students = ["kunal","raj","om","vishal","akshay","abhishek"]
print(list(filter(lambda name : len(name)<4,students)))   #[F,T,T,F,F,F]


result = {"kunal":90,"raj":21,"om":89,"vishal":31,"akshay":78,"abhishek":32}
#print list of name passed student
print(list(filter(lambda name : result[name]>=35,result)))  #[kunal,om,akshay]

#------------------------------------------------------------------------------------------------
# print dict of failed student
result = {"kunal":90,"raj":21,"om":89,"vishal":31,"akshay":78,"abhishek":32}
#print list of name passed student

print(dict(filter(lambda student: student[1]<40,result.items())))
#----------------------------------------------------------------------------------------------

