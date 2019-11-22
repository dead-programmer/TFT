import calculate
import team_comps
import champ_and_item
from scrape import scrape
from pprint import pprint

user_input = []


class text_colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END_COLOR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_user_input():
    user_input_string = input("What champions do you have? ")
    user_input_string = user_input_string.split(" ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for i in user_input_string:
        if '-' in i:
            team_comps.delete_champ(i)
        else:
            team_comps.add_champ(i)

    best_team = calculate.match(user_input_string)
    missing = calculate.recommend_multiple(best_team)
    print(text_colors.YELLOW + "Recommended team(s) ----> %s\n" % best_team + text_colors.END_COLOR)
    print(text_colors.BLUE + "Recommended champion(s) ----> %s\n" % missing + text_colors.END_COLOR)


print("\n\nScraping latest meta data...")
_temp, team_comps.team_data = scrape()
print("Updating champion list with latest...")
champ_and_item.update()
print("Done.\n\n")
print("Welcome to our plugin!")
print("This will recommend you team(s) based on what champions you have  :)\n\n")

while 1:
    get_user_input()
