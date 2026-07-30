'''
# Keywords Arguments:----> there is no need to maintain position in a keywords argument.
  These arguments are passed to the function by explicitly specifying the name of the parameter along with 
  the value. The order of the arguments doesn't matter.
Eg,
 def details(name, city):
        return f'my name is {name} and i am from {city}'

print(details(name='vaibhav patil', city='pune'))
#my name is vaibhav patil and i am from pune

syntax: 
    def function_name(p1, p2, p3):
         # function body
           pass
    function_name(p1=v1, p2=v2, p3=v3)
    function_name(p2=v2, p3=v3, p1=v1)
'''

def full_name(fn,mn,ln):
    fname = f"{fn} {mn} {ln}"
    print(fname)
full_name(fn="rahul",mn="ram",ln="patil")
full_name(mn="ram",fn="rahul",ln="patil")

     




