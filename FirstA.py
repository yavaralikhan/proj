students = ["john", "jennie", "jin"]
print(students)
print(type(students))

#concatenation
print(students + ["daman", "gagan"])

#membership testing
print("john" in students)
print("yavar" in students)
print("yavar" not in students)

#repetation
print(students*2)

#indexing

print(students[0])
print(students[len(students)-1])

#slicing

print(students[0:2]) #0 is inclusive and 2 is exclusive
print(students[1:2])

#tukda nikalna



for i in range(0, len(students)):
    print(students[i])

for student in students:
    print(student)



students = ["yavar", "tania","daman", "gagan"]
print(students, hex(id(students)))
