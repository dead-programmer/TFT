import calculate
import team_comps


user_input = []


def get_user_input():
    user_input_string = input("What champions do you have?")
    user_input = user_input_string.split(" ")

    print(user_input)

    for i in user_input:
        if '-' in i:
            team_comps.delete_champ(i)
        else:
            team_comps.add_champ(i)

    print(user_input)
    # calculate.match(user_input, team_comps.tier_S)
    # print(calculate.score_calculator(user_input)['team_name'])


while 1:

    get_user_input()
    team_comps.get_team_data()