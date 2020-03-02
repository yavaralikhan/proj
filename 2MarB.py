from Mar2 import HashTable
class Student:

    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

    def __str__(self):
        return "{}\t{}\t{}".format(self.roll, self.name, self.age)


s1 = Student(101, "john", 22)
s2 = Student(311, "jen", 20)
s3 = Student(432, "jenny", 24)
s4 = Student(191, "fionna", 27)
s5 = Student(715, "fee", 25)

hTable = HashTable(13)
hTable.put(s1)
hTable.put(s2)
hTable.put(s3)
hTable.put(s4)
hTable.put(s5)

hTable.iterate()