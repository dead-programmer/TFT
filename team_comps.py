from pprint import pprint
# def get_data():
#     for key in data:
#         tier_S.append(key)
#         print("KEY = " + key)
#     return tier_S


def get_data():
    pprint(data)
    return data


def build_data(input):
    user_team.append(input)
    print(user_team)


def delete_champ(deletion_input):                            # -champion_name
    champ_name_length = len(deletion_input) - 1              # length = len(champion_name)
    user_team.remove(deletion_input[-champ_name_length:])    # remove("champion_name")
    print(user_team)


tier_S = []
user_team = []

# TODO: use web scraper to pull the following data automatically
data = {
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