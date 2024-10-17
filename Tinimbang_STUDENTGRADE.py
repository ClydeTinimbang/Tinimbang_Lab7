name=(input("Student Name:"))
section=(input("Section:"))
prelim=float(input("Prelim grade:"))
midterm=float(input("Midterm grade:"))
final=float(input("Final grade:"))


prelim_grade= 0.3333 * prelim
midterm_grade= 0.3333 * midterm
final_grade= 0.3333* final
total_grade=prelim_grade+midterm_grade+final_grade
final= round(total_grade)

if(prelim>=40 and prelim<=100 and midterm>=40 and midterm<=100 and final>=40 and final<=100):
    if 99<= total_grade<= 100:
        print("Grade is 1.00 Excellent Student")
    elif 96<=total_grade<=100:
        print("Grade is 1.25 Outstanding Student")
    elif 93 <=total_grade<=100:
        print("Grade is 1.50 Superior Grade")
    elif 90<=total_grade<=100:
        print("Grade is 1.75 Very Good Student")
    elif 87<=total_grade<=100:
        print("Grade is 2.00 Good Student")
    elif 84<=total_grade<=100:
        print("Grade is 2.25 Fair Student")
    elif 81<=total_grade<=100:
        print("Grade is 2.50 Satisfactory Student")
    elif 78<=total_grade<=100:
        print("Grade is 2.75 Poor Student")
    elif 75<=total_grade<=100:
        print("Grade is 3.00 Passed")
    else:
        print("The grade is below 75, You failed!")

