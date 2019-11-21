import team_comps

teams = team_comps.team_data
best_team = []
unique_list = []
hit_list = []
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
                    team['team_champ'].append(champion)
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
                    if found is False:
                        team['team_champ'].append(champion)
                        team['team_name'] = team_comp
                        best_team.append(team)

                # elif score == team['team_score']:
                #     team['team_score'] = score
                #     team['team_champ'] += champion
                #     team['team_name'] = team_comp
                #     best_team += team
                score = 0

    # result = best_team + team
    for best in best_team:
        print(best['team_name'])
    # return best_team
    return best_score


def match(input_list):
    # Iterate through user inputs, then append matches to hit_list
    for champion in input_list:
        for match in team_comps.team_data:
            if champion in team_comps.team_data[match]:
                hit_list.append(match)
    if hit_list:
        # FIND UNIQUE
        for hit in hit_list:
            if hit not in unique_list:
                unique_list.append(hit)

        max_count = 0

        # Logic for deciding ties between teams
        for team in unique_list:
            count = hit_list.count(team)
            if count > max_count:
                max_count = count
                del best_team[:]
                best_team.append(team)
            elif count == max_count:
                best_team.append(team)
    return best_team


# Returns the difference between the user team and the calculated best team(s)
def recommend(team_list):
    results = []
    for team in team_list:
        results.append(list(set(team_comps.team_data[team]) - set(team_comps.user_team)))
    return results


def remove_from_hit_list(removed_champ):
    for hit in hit_list:
        if removed_champ in teams[hit]:
            hit_list.remove(hit)
