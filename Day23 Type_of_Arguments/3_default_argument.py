'''
#Default Arguments:---->
These are parameters that have a default value. If no argument is provided for that parameter, the default value is used.

def About_Institute(institute_name,course='Python'):
	return f'{institute_name} is The Best institute for {course} course in pune'

print(About_Institute('Kiran Academy','Java'))
#Kiran Academy is The Best institute for Java course in pune
print(About_Institute('Kiran Academy'))
#Kiran Academy is The Best institute for Python course in pune

syntax: 
def fun_name(p1,p2=value):
     pass
fun (v1,v2)
fun (v1)      
'''
# def course_details (cname,duration,institute):
# def course_details (cname,duration,institute="The Kiran Academy"):
#     data = f'''
#             Institute_Name: {institute}
#             Course_Name: {cname} 
#             Duration: {duration}
#            '''   
    # print(data)
# course_details("Python Development","4 Month","The Kiran Academy")    
# course_details("Java Development","5 Month","The Kiran Academy")

# course_details("Python Development","4 Month")
# course_details("Python Development","4 Month")    
# course_details("Aws","4 Month","Java By Kiran")    
#---------------------------------------------------------------------------------------------


# def course_details (cname,duration,institute="The Kiran Academy"):  # Parameter
#     data = f'''
#             Institute_Name: {institute}
#             Course_Name: {cname} 
#             Duration: {duration}
#            '''   
#     print(data)

# course_details("Data Science","4 Month","TKA")   #Positional arg
# course_details(cname="Data Analyst", duration="5 Month",institute="Java By Kiran")  #Keywords arg
# course_details("Web Development",duration="6 Month",institute="TKA")  #Positional arg + Keywords arg

#--------------------------------------------------------------------------------------------------

def course_details (cname="-",duration="0 Month",institute="The Kiran Academy"):
    data = f'''
                Institute_Name: {institute}
                Course_Name: {cname} 
                Duration: {duration}
               '''   
    print(data)  

course_details()
course_details(institute="Jbk",cname="Cyber Security")
course_details(cname="Cyber Security")

















