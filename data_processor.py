from grade_utils import calculate_average

def analyze_scores(grades):
    high_score = max(grades)
    low_score = min(grades)
    overall_average = calculate_average(grades)
    return high_score, low_score, overall_average
    print(f"Your high score is {high_score}, Your low score is {low_score}, Your average is  {overall_average}")
