def team_lineup(*args):
    team = {}
    print_text = ''

    for player, country in args:
        if country not in team.keys():
            team[country] = []

        team[country].append(player)

    sorted_team = sorted(team.items(), key=lambda x: (-len(x[1]), x[0]))
    for country, names in sorted_team:
        print_text += f"{country}:\n"
        for name in names:
            print_text += f"  -{name}\n"

    return print_text

