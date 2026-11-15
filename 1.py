# Create an array using list
arr = [10, 20, 30, 40, 50]

print("Original Array:", arr)

# a) Update array
arr[1] = 25
print("After Update:", arr)

# b) Slice array
print("Sliced Array:", arr[1:4])

# c)extend array
arr.extend([60, 70])
print("After Extend:", arr)

# d)append element
arr.append(80)
print("After Append:", arr)

# e) remove element
arr.remove(30)
print("After Remove:", arr)