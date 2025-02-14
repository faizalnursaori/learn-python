# Convert variable ke data type tertentu
#str() => mengubah ke string
#int() => mengubah ke integer
#float() => mengubah ke float
#bool() => mengubah ke boolean

name = "Faizal Nursaori"
age = 25
gpa = 3.5
is_student = False

gpa = int(gpa)
print(type(gpa))
print(gpa)

name = bool(name) # Kalau ada value hasilnya true
print(name)