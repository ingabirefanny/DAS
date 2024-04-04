#accessing using positive indexing
students = ("bosco","peter","claude","paul")
print(students[2])
# accessing using negative indexing
print(students[-1])
#accessing using range of indexes
print(students[1:-2])
teachers=("Fanny","grace","sandra")
#concatening tuples
classes = students+teachers
print(classes)
#check if an item exists
if "grace" in teachers:
    print("yes,'grace is a teacher") 
#repittion
    print(classes*2)