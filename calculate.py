import team_comps


teams = team_comps.team_data

best_team = []
best_score = 0


def score_calculator(user_team):
    global best_team
    global best_score
    team = {
        'team_name': '',
        'team_champ': []
    }
    for team_comp in teams:
        score = 0
        for champion in user_team:
            if champion in teams[team_comp]:
                score += 1
                print("champion in score calculator: ", champion)
                print("score: ", score)

                if score > best_score:
                    team['team_champ'] += champion
                    team['team_name'] = team_comp
                    del best_team[:]
                    best_team.append(team)
                    best_score = score
                    print(best_score)
                elif score == best_score:
                    found = False
                    for best in best_team:
                        if teams[team_comp] == best['team_name']:
                            found = True
                    if found == False:
                        team['team_champ'] += champion
                        team['team_name'] = team_comp
                        best_team.append(team)

                # elif score == team['team_score']:
                #     team['team_score'] = score
                #     team['team_champ'] += champion
                #     team['team_name'] = team_comp
                #     best_team += team

    # result = best_team + team
    for best in best_team:
        print(best['team_name'])
    # return best_team
    return best_score



#
# def match(input_list, data):
#     score = 0
#     for champion in input_list:
#         for match in data:
#             if champion in match:
#                 score += 1
#                 print(champion)
#                 print(score)
