# Task 1 :--->
# l1=['kiran','srushti','minakshi','satya','pragati']

# final out come should be printing 2 lists
#1. strings having length less than or equal to 5
#2. strings having length greater than 5

# short_names = []
# long_names = []

# for name in l1:
#     if len(name) <= 5:
#         short_names.append(name)
#     else:
#         long_names.append(name)

# print("Length <= 5:", short_names)
# print("Length > 5:", long_names)

l1=['kiran','srushti','minakshi','satya','pragati']
badi = list()
chhoti = list()
for nameInList in l1:
    # print(nameInList)
    lenOfString=len(nameInList)
    print(lenOfString)
    if lenOfString >5:
        badi.append(nameInList)
    else:
        chhoti.append(nameInList)
print(badi)
print(chhoti)


#---------------------------------------------------------------------------------------------------
#TASK 1.1 :---->

l1=[[2,4,6],[10,20,30],[50,60,90,99]]
# create a list with avg of above each group
# [ avg of first group , , , ]

avglist=list()
for sublistnumbers in l1:
    # print(f"length of sub list {len(sublistnumbers)}")
    # print(f"sum of sub list {sum(sublistnumbers)}")
    avg = sum(sublistnumbers)/len(sublistnumbers)
    # print(avg)
    avglist.append(avg)
print(avg)
print(f"final list is -- > {avglist}")


#---------------------------------------------------------------------------------------------------

# Task 2 :--->
data={
    'KA001':['kiran','srushti','minakshi','satya','pragati'],
    'KA002':['kiran12','srushti567','minakshi','satya55554','pragati'],
    'KA003':['kiran345','srushti8899','minakshi777','satya','pragati'],
    }
#return a list with names having lenth more than or equal to 8

long_names = []

# Outer loop to access each list of names
for name_list in data.values():
    # Inner loop to check individual names
    for name in name_list:
        if len(name) >= 8:
            long_names.append(name)

print(long_names)
# Output: ['minakshi', 'srushti567', 'minakshi', 'satya55554', 'kiran345', 'srushti8899', 'minakshi777']



