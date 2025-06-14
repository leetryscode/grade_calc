from grade_utils import calculate_average, get_letter_grade
from data_processor import analyze_scores
from input_handler import get_user_scores

def main():
    
    print(f"How many scores do you want to enter?")
    num_scores = int(input())
    score_list = get_user_scores(num_scores)

    average_grade = calculate_average(score_list)
    letter = get_letter_grade(average_grade)
    top_score, bottom_score, big_average = analyze_scores(score_list)
    print(f"Your highest grade was {top_score}, your lowest grade was {bottom_score}, and your class average is {big_average}. You have a {letter} in this class.")
    


#grades = [85, 92, 78, 96, 88]
main()
