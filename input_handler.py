
def get_user_scores(num_scores):
    list_of_scores = []
    for i in range(num_scores):
        print(f"Enter score {i + 1}:")
        score = int(input())
        list_of_scores.append(score)
    return list_of_scores

    