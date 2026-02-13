n = int(input("Enter the number of students: "))
listA = []
listB= []
for i in range(n):
    listA.append(input("Enter the students' names: "))
    listB.append(int(input("Enter their marks: ")))
t1 = tuple(listA)
print("The tuple representing students' names is: ", t1)
print("The list representing students' marks is: ", listB)
E1 = {}
for i in range(n):
    name = listA[i]
    marks = listB[i]
    E1[name] = marks
print("The dictionary representing students marks and names is: ", E1)
s = set(listB)
print("The set of unique marks is: ", s)