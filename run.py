import calculate
import team_comps
import scrape

user_input = []


def get_user_input():
    user_input_string = input("What champions do you have?")
    user_input_string = user_input_string.split(" ")
    for i in user_input_string:
        if '-' in i:
            team_comps.delete_champ(i)
        else:
            team_comps.add_champ(i)

    result = calculate.match(user_input_string)
    print("Recommended team(s) ----> %s\n" % result)


while 1:
    team_comps.get_team_data()
    get_user_input()
