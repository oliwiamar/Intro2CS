name = "Oliwia"
age = 22.4
height = 1.65
student_now = True 
city = "Poznan"
print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type (student_now))
print(type(city))

#PizzaPythonParty
slices_per_student = 3
students = 25
present_students =  students - 14
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8)%present_students
print("Since there are", present_students, "students present, we will need to order",boxes_to_order, "boxes of pizza and we will have", total_slices_needed, "slices of pizza so each student will have to pay", cost_per_student, "złotych and there will be", leftover_slices, "slices left over.")