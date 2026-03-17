list_ex = [1,2,3, "r", "Ram Thapa", 2.3, -0.5]

# print(list_ex)
print(type(list_ex))

student_list = ["Ram", "Hari"]

print(student_list)
print(student_list[0]) # 0 index means first position
print(student_list[1])

student_list.append("Ramesh")



student_list.append("Roshan")


student_list.insert(0, "Ram Kumar")

student_list[0] = "Ram Thapa"

# print(student_list)

print("Let's welcome ", student_list[0])
["Ram", "Hari", "Ramesh", "Roshan"]
for student_name in student_list:
    print("Let's welcome ", student_name)
    
    if student_name == "Roshan":
        break
    
else:
    print("All students got chance to perform")


student_list = ["ram", "hari", "shyam", "hari"]

del student_list[1]

student_list.remove("hari")
student_list.remove("ram")
student_list.remove("roshan")

stu_index = student_list.index("hari")
print(stu_index)

student_list.reverse()


popped_item = student_list.pop(0)
print("Popped item is ", popped_item)
print(student_list)

students_final = ["hari"]
for student_name in student_list:
    if student_name not in students_final:
        students_final.append(student_name)
        

print(students_final)

students_db = []
MENU = """
    1. Add student (participant)
    2. Show all students
    3. Exit
"""

while True:
    print(MENU)
    
    user_choice = input("Choice (1/2/3): ").strip()
    
    if user_choice == "1":
        name = input("Students Name: ")
        students_db.append(name)
    elif user_choice == "2":
        print(students_db)
    elif user_choice == "3":
        break
    else:
        print("Invalid choices, please selct (1/2/3)")

student_list = ["ram", "hari", "shyam", "roshan"]


student_list[-1] # last index
student_list[-2] # second last index
student_list[-3] # second last index
student_list.insert(0, )

Slicing
sub_list = student_list[1:3]
sub_list = student_list[-3:-1]
sub_list = student_list[-3:]
sub_list = student_list[:4]

print(sub_list)
student_list.sort()
student_list.sort(reverse=True)

print(student_list)





student_list = ["ram", "hari", "shyam", "roshan"]

final_list = tuple(student_list)

final_list.append("Roshan")
final_list[1]

final_list = ("ram", "hari", "roshan")


student_list = {"ram", "hari", "shyam", "hari"}

print(student_list[0])

student_list = ["ram", "hari", "shyam", "roshan", "hari"]

new_student_list = set(student_list)

print(new_student_list)

ram_hobbies = {"reading", "writing", "football"}
hari_hobbies = {"cricket", "writing", "drumming", "reading"}

common_hobbies = ram_hobbies.intersection(hari_hobbies)
common_hobbies = ram_hobbies & hari_hobbies

print(common_hobbies)

all_hobbies = ram_hobbies.union(hari_hobbies)
all_hobbies = ram_hobbies | hari_hobbies

print(all_hobbies)



ram_only = ram_hobbies.difference(hari_hobbies)
print(ram_only)
hari_only = hari_hobbies.difference(ram_hobbies)
hari_only = hari_hobbies - ram_hobbies # setA - setB


all_unique_hobbies = ram_hobbies.symmetric_difference(hari_hobbies)


print(all_unique_hobbies)


ram_hobbies = {"reading", "writing", "football"}
hari_hobbies = {"cricket", "writing", "drumming", "reading"}

ram_hobbies.add("vlogging")
ram_hobbies.update(["drawing", "singing"])

ram_hobbies.remove("vlogging")
ram_hobbies.pop()

print(ram_hobbies)


