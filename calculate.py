

def match(input_list, data):
    score = 0
    for champion in input_list:
        for match in data:
            if champion in match:
                score += 1
                print(champion)
                print(score)
