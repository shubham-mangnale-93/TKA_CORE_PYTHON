# method is a reusable block of code it is used to perform operation on data.

name = "shubham"
print(name.upper()) # output - SHUBHAM

name = "DATA ANALYST"
print(name.lower()) # output - data analyst
#--------------------------------------------------------------------------------------------

#title and capitalize
course = "java full stack"
print (course.title())  # output - Java Full Stack
print (course.capitalize()) #output - Java full stack
#--------------------------------------------------------------------------------------------

#isalpha
name = "shubhammangnale"
print(name.isalpha())

name = "12345"
print(name.isalpha())
#--------------------------------------------------------------------------------------------

#isnumeric
name = "shubhammangnale"
print(name.isnumeric())

name = "123455"
print(name.isnumeric())

name = "shubhammangnale@12345"
print(name.isnumeric())
#--------------------------------------------------------------------------------------------

#isalnum

name = "shubhammangnale"
print(name.isalnum())

name = "12344"
print(name.isalnum())

name = "shubham12345"
print(name.isalnum())

name = "shubhammangnale@989898"
print(name.isalnum())
#--------------------------------------------------------------------------------------------

#isspace and replace

course ="data analyst"
print(course.isspace())

print(course.replace('analyst','science'))

de = "java is simple java is dynamic java is..."
print(de.replace("java","python"))
print(de.replace("java","python",2))
print(de.replace("java","python",-1))
#--------------------------------------------------------------------------------------------

#count

course = "machine learning"
print(course.count("a"))
print(course.count("a",8))

course = "data analyst coursea"
print(course.count("a",5))
print(course.count("a",5,-8))

#--------------------------------------------------------------------------------------------

#startswith
#startswith() returns True if the string starts with the specified prefix; otherwise, it returns False.

institute = "the kiran academy"

print(institute.startswith("T"))
print(institute.startswith("t"))
print(institute.startswith("k"))
print(institute.startswith("k",4))
print(institute.startswith("k",4,-8))
#--------------------------------------------------------------------------------------------

#endswith()
#endswith() returns True if the string ends with the specified suffix; otherwise, it returns False.

text = "python"
print(text.endswith("on"))
print(text.endswith("py"))

filename = "resume.pdf"
print(filename.endswith(".pdf"))

email = "abc@gmail.com"
print(email.endswith(".com"))
#--------------------------------------------------------------------------------------------

#split

fullname = "amit sham kendre"

print(fullname.split()) #return list of string
print(fullname.split("a")) 

course = "python,java,cpp,devops,aws,testing"
print(course.split(","))
#--------------------------------------------------------------------------------------------

#strip, rstrip, lstrip

name = "     amit"
print(name.strip(" "))
print(name.lstrip("a"))
print(name.rstrip("t"))
#--------------------------------------------------------------------------------------------

#center

institute = "kiran"
print(institute.center(7,"-"))

ins = "the kiran academy"
print(ins.center(100,"-"))
#--------------------------------------------------------------------------------------------

#join

list = ['amit', 'hari', 'yadav']
full_name = ",".join(list)
print(full_name)
print(' @'.join(list))
#--------------------------------------------------------------------------------------------

#isupper, islower, istitle

#.isupper : checks if all letters in the string are in UPPERCASE:
print("PYTHON".isupper())      # True  → all letters are capital
print("Python".isupper())      # False → some letters are small
print("PYTHON 123".isupper())  # True  → numbers are ignored, all letters are capital

#.islower() — checks if all letters in the string are in lowercase:
print("python".islower())      # True  → all letters are small
print("Python".islower())      # False → 'P' is capital
print("python 123".islower())  # True  → numbers are ignored, all letters are small

#.istitle() — checks if first letter of every word is capital and rest are small:
print("Python Programming".istitle())   # True  → first letter of both words is capital
print("Python programming".istitle())   # False → 'p' of 'programming' is small
print("PYTHON PROGRAMMING".istitle())   # False → all letters are capital






