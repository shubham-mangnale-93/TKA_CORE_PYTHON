# wap to check valid number:---->
def mobile_number(mobile):
    smobile = str (mobile)
    if len(smobile)== 10 and smobile.isnumeric():
        return True
    else:
        return False

print(mobile_number(9325779222))   
#----------------------------------------------------------------------------------------------------

def xyz(parameter):
    #code
    if len(parameter) == 10 and parameter.isdigit() and parameter[0] in '6789':
        result = "Valid mobile number"
    else:
        result = "Invalid mobile number"
    return result

var = xyz("9876543210")
print(var)


print(xyz("9876543210"))   # Valid mobile number
print(xyz("5876543210"))   # Invalid mobile number  
print(xyz("98765432"))     # Invalid mobile number 
print(xyz("98765432"))     # Invalid mobile number 
print(xyz("987654321a"))   # Invalid mobile number