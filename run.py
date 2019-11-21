import calculate
import team_comps
import champ_and_item
from scrape import scrape

user_input = []


def get_user_input():
    user_input_string = input("What champions do you have?")
    user_input_string = user_input_string.split(" ")
    for i in user_input_string:
        if '-' in i:
            team_comps.delete_champ(i)
        else:
            team_comps.add_champ(i)

    best_team = calculate.match(user_input_string)
    missing = calculate.recommend(best_team)
    print("Recommended team(s) ----> %s\n" % best_team)
    print("Recommended champion(s) ----> %s\n" % missing)


print("Welcome to our plugin!")
print("This will recommend you team(s) based on what champions you have  :)\n\n")
print("Scraping latest meta data...")
_temp, team_comps.team_data = scrape()
print("Updating champion list with latest...")
champ_and_item.update()
print("Done.\n\n")

while 1:
    get_user_input()
