def f1():
    print("welcome to f1 function")
    def f2():
        print("welcome to f2 function")
    return f2   

f2 = f1()
f2()
#----------------------------------------------------------------------------------------

def numbers1():
    num1 = 10
    def numbers2():
        num2 = 20
        return num1 + num2    
    return numbers2()         

result = numbers1()           
print(result)
#----------------------------------------------------------------------------------------

def numbers1():
   num1=10
   def numbers2():
      num2=20
      return num2
   return num1,numbers2()

num1,num2=numbers1()
print(num1+num2)
#----------------------------------------------------------------------------------------

def numbers1():
    num1 = 10
    def numbers2():
        num2 = 20
        return num2
    return num1, numbers2

num1, numbers2 = numbers1()
num2 = numbers2()
print(num1 + num2)
#----------------------------------------------------------------------------------------

def fname():
    fn = "vaibhav"
    def lname():
        ln = "patil"
        return ln
    return fn, lname

fn, lname = fname()
ln = lname()
print(fn+" "+ln)

#---------------------------------------------------------------------------------

def square(num1):
    sq = num1**2
    def cube(num2):
        cu = num2**3
        return cu
    return sq, cube

sq, cube = square(5)
cu = cube(3)
print(sq + cu)
#---------------------------------------------------------------------------------

def f1(n1):
    r1 = n1/2
    def f2(n2):
        r2 = n2/2
        def f3(n3):
            r3 = n3/2
            return r3
        return r2, f3
    return r1, f2

f1()



