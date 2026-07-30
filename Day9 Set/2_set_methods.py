# SET METHODS :---->

s = {10, 20, 30, 40}
# add
s.add(50)  # Add an element to a set
print(s)

# delete :
# remove
s = {10, 20, 30.6, 40}
s.remove(20)  # Remove a specific element from a set (gives error if element not found)
print(s)  # {40, 10, 30.6}

s = {10, 20, 30.6, 40}
# pop
print(s.pop())  # Removes and returns a random element from the set
print(s)        # Prints remaining elements after pop

#discard
s = {10, 20, 30.6, 40}
s.discard(200)
print("......",s)
s.discard(20)
print("......",s)

#intersection
s1 = {10, 20, 30, 40}
s2 = {10, 20, 30, 40, 50, 60, 70}
print(s1.intersection(s2))


batch1336 = {"Shiv", "Rahul", "Priya", "Amit", "Sneha"}
batch1337 = {"Rahul", "Priya", "Amit", "Rohit", "Neha"}
batch1338 = {"Priya", "Amit", "Sneha", "Rohit", "Riya"}

# print(batch1336.intersection(batch1337, batch1338))
result = batch1336.intersection(batch1337, batch1338)
print("Common students:", result)
print(f"Students present in all 3 batches: {result}")

#difference
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {50, 60, 70, 80, 90, 100}
l1 = [60,70,33,44,55]
s = s1.intersection(s2,l1)
print(s)

print(s1.difference(s2))
print(s2.difference(s1))
#Return a new set with elements in the set that are not in the others.
print(s1.symmetric_difference(s2))
#Return a new set with elements in either the set or other but not both.

#intersection_update
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {50, 60, 70, 80, 90, 100}

print(s1.intersection_update(s2) )
print(s1)
print(s2)

#difference_update
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {50, 60, 70, 80, 90, 100}
print(s1.difference_update(s2))
print(s1)
print(s2)


#update and union
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {50, 60, 70, 80, 90, 100}
print(s1.update(s2)) 
print(s1)

s1 = {1,2,3,4}
s2 = {5,6,7,8,9,10}

s1.update(s2)
print(s1)

s = s1.union(s2)
print(s)
print(s1)

# issubset and issuperset
s1 = {10, 20, 30, 40, 50, 60, 70}
s2 = {30,40,50}
print(s2.issubset(s1)) #Report whether another set contains this set.
print(s1.issuperset(s2)) #Report whether this set contains another set.

