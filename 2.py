
# Create an empty list
mylist = []

#Take size from user
n = int(input("Enter size of list: "))

#Append elements 
for i in range(n):
    num = int(input("Enter element: "))
    mylist.append(num)

print("Final List:", mylist)