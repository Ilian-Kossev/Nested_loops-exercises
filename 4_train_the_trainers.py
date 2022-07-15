jury_number = int(input())
command = input()
average_grade_all_presentations = 0
while command != "Finish":
    grade = float(input())
    counter_presentations = 0
    sum_grades = 0
    average_grade_current_presentation = 0
    for number in range(1, jury_number + 1):
        sum_grades += grade
    average_grade_current_presentation = sum_grades / jury_number
    average_grade_all_presentations += average_grade_current_presentation / counter_presentations
    print(f"{command} - {average_grade_current_presentation}.")
    command = input()
print(f"Student's final assessment is {average_grade_all_presentations:.2f}.")










