# Create a list
mylist = [10, 20, 10, 40, 30]

print("Original List:", mylist)

# a) Update
mylist[1] = 25
print("After Update:", mylist)

# b) Count
print("Count of 10:", mylist.count(10))

# c) Sort
mylist.sort()
print("After Sort:", mylist)

# d) Insert
mylist.insert(2, 15)
print("After Insert:", mylist)

# e) Append
mylist.append(50)
print("After Append:", mylist)

# f) Extend
mylist.extend([60, 70])
print("After Extend:", mylist)

# g) Pop
mylist.pop()
print("After Pop:", mylist)