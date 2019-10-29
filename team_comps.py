# from pprint import pprint


def get_team_data():
    # pprint(team_data)
    return team_data


def add_champ(champ_name):
    user_team.append(champ_name)
    print(user_team)


def delete_champ(deletion_input):                            # -champion_name
    champ_name_length = len(deletion_input) - 1              # length = len(champion_name)
    user_team.remove(deletion_input[-champ_name_length:])    # remove("champion_name")
    print(user_team)


tier_S = []
user_team = []

# TODO: use web scraper to pull the following data automatically
team_data = {
    'void_brawlers':
        ['khazix',
         'blitzcrank',
         'reksai',
         'vi',
         'akali',
         'chogath',
         'jinx',
         'kaisa']
    ,

    'imperial_knights':
        ['darius',
         'garen',
         'mordekaiser',
         'poppy',
         'katarina',
         'draven',
         'sejuani',
         'kayle',
         'swain']
}