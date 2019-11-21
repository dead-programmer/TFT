# Stores Champions' data, including name and synergies
# TODO: Stores Item data

import team_comps


champ_data = []


def update():
    for key in team_comps.team_data:
        for champion in team_comps.team_data[key]:
            if champion not in champ_data:
                champ_data.append(champion)
