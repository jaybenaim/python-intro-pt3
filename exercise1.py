

grade = ""

def print_grade(grade): 
    return "You got a {}\n".format(grade)

def return_grade(percentage): 
    num = input("What is the grade you got?\n") 

    if int(num) < 50: 
        grade = "F"
        return print_grade(grade)
    elif int(num) >= 50 and int(num) <= 54: 
        grade = "D"
        return print_grade(grade)
    elif int(num) >= 55 and int(num) <= 59: 
        grade = "D+"
        return print_grade(grade)
    elif int(num) >= 60 and int(num) <= 62: 
        grade = "C-"
        return print_grade(grade)
    elif int(num) >= 63 and int(num) <= 68: 
        grade = "C"
        return print_grade(grade)
    elif int(num) >= 67 and int(num) <= 69: 
        grade = "C+"
        return print_grade(grade)
    elif int(num) >= 70 and int(num) <= 72: 
        grade = "B-"
        return print_grade(grade)
    elif int(num) >= 73 and int(num) <= 76: 
        grade = "B"
        return print_grade(grade)
    elif int(num) >= 77 and int(num) <= 79: 
        grade = "B+"
        return print_grade(grade)
    elif int(num) >= 80 and int(num) <= 84: 
        grade = "A-"
        return print_grade(grade)
    elif int(num) >= 85 and int(num) <= 89: 
        grade = "A"
        return print_grade(grade)
    elif int(num) >= 90 and int(num) <= 100: 
        grade = "A+"
        return print_grade(grade)
    elif int(num) >= 67 and int(num) <= 69: 
        grade = "C+"
        return print_grade(grade)


print(return_grade(1))
