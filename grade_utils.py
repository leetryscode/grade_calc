def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def get_letter_grade(average_grade):
    letter_grade = ""
    if average_grade >= 90:
        letter_grade = "A"
    elif average_grade >= 80:
        letter_grade = "B"
    elif average_grade >= 70:
        letter_grade = "C"
    elif average_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade