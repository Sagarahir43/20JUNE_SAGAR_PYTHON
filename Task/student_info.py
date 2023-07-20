students={}
num_student=int(input("enter number of students:"))
for i in range(num_student):
    print(f"enter information students{i+1}:")
    name=input("name:")
    age=int(input("age:"))
    grade=input("grade:")

    students_info={"name":name,"age":age,"grade":grade,}
    students[f"students{i+1}"]=students_info
print(students)