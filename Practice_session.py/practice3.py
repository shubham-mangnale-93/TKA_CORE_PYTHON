data = {
    'KA001': ['kiran', 'srushti', 'minakshi', 'satya', 'pragati'],
    'KA002': ['kiran12', 'srushti567', 'minakshi', 'satya55554', 'pragati','kavya'],
    'KA003': ['kiran345', 'srushti8899', 'minakshi777', 'satya', 'pragati'],
}

# Q1. Print all dictionary keys.
for k in data:
    print(":--->",k)

# Q2. Print all dictionary values.
print(data.values())         

# Q4. Print only students of KA001
for name in data ["KA001"]:
    print(name)

# Q5. Print the first student from every batch.
# for batch in data:
#     print(data[batch][0])    
for batch, students in data.items():
    print(batch, ":", students[0])    

# Q6. Print the last student from every batch.
# for batch in data:
#     print(data[batch][-1])   

for batch, students in data.items():
    print(batch, ":", students[-1])  

# Q7. Count how many batches are there.
print(len(data))      

# Q8. Count students in every batch.
for batch in data:
    print(batch,":",len(data[batch]))

# Q9. Count total students in all batches.
# count = 0
# for batch in data.values():
#     count = count + len(batch)  
# print(count)   
# 
count = 0
for student in data:
    # print(student)
    count = count + len(data[student])
    # print(count)

print(count)    