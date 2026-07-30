data = ["Maharashtra",["Pune", ["shegaon","Mulshi", "Maval", "Shirur"], "Nagpur", "Kolhapur", "Buldhana","Ahmedabad"], "Gujarat","Karnataka", "Rajasthan", "Madhya Pradesh"]

# Append "Punjab" to the end of the list, right after "Madhya Pradesh"
print(data.append("Punjab"))  
print(data)

# Insert "Goa" at the very beginning (index 0) of the list
print(data.insert(0,"Goa"))
print(data)

# Insert "Jalgaon" right after "Ahmedabad" inside that inner sub-list
# print(data[2].insert(6,"Jalgaon"))
# print(data)

print(data[2].append("Jalgaon"))
print(data)

# delete --> "nagpur" at the nested list 
print(data[2].remove("Nagpur"))
print(data)

# delete ---> "mulshi"
# del data [2] [1] [1]
# print(data)

data[2][1].remove("Mulshi")
print(data)

# add ---> "Shirur" after "Yavatmal"
data[2][1].append("Yavatmal")
print(data)

print("---------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------------------
# SHOW ME THIS OUTPUT---> Goa, Maharashtra, Gujarat, Karnataka, Rajasthan, Madhya Pradesh, Punjab, shegaon, Maval, Shirur, Yavatmal, Pune, Kolhapur, Buldhana, Ahmedabad, Jalgaon

#step1:---------------> 
data1 = data[2].pop(1)
print(data1)

#step2:--------------->
data2 = data.pop(2)
print(data2)
print(data)

#step3:--------------->
data.extend(data1)
print(data)

# #step4:--------------->
data.extend(data2)
print(data)

# #step4:--------------->
data3 = ", ".join(data)
print(data3)
