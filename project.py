import random
from tabulate import tabulate

premTeamsStrength = [{"Team": "Arsenal", "strength": 10}, {"Team": "Aston Villa", "strength": 7}, {"Team": "Bournemouth", "strength": 5}, {"Team": "Brentford", "strength": 4}, {"Team": "Brighton", "strength": 6}, {"Team": "Chelsea", "strength": 10}, {"Team": "Crystal Palace", "strength": 5}, {"Team": "Everton", "strength": 5}, {"Team": "Fulham", "strength": 5}, {"Team": "Ipswich Town", "strength": 2}, {"Team": "Leicester City", "strength": 5}, {"Team": "Liverpool", "strength": 10}, {"Team": "Manchester City", "strength": 11}, {"Team": "Manchester United", "strength": 10}, {"Team": "Newcastle", "strength": 7}, {"Team": "Nottingham Forest", "strength": 4}, {"Team": "Southampton", "strength": 4}, {"Team": "Tottenham Hotspur", "strength": 10}, {"Team": "West Ham", "strength": 6}, {"Team": "Wolves", "strength": 5}]
premTeams = ["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Ipswich Town", "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle", "Nottingham Forest", "Southampton", "Tottenham Hotspur", "West Ham", "Wolves"]
champTeams = [{"Team": "Blackburn Rovers", "strength": 3}, {"Team": "Bristol City", "strength": 2}, {"Team": "Burnley", "strength": 3}, {"Team": "Cardiff City", "strength": 2}, {"Team": "Coventry City", "strength": 2}, {"Team": "Derby County", "strength": 2}, {"Team": "Hull City", "strength": 3}, {"Team": "Leeds United", "strength": 4}, {"Team": "Luton Town", "strength": 2}, {"Team": "Middlesbrough", "strength": 3}, {"Team": "Millwall", "strength": 2}, {"Team": "Norwich City", "strength": 3}, {"Team": "Oxford United", "strength": 2}, {"Team": "Plymouth Argyle", "strength": 2}, {"Team": "Portsmouth", "strength": 2}, {"Team": "Preston North End", "strength": 2}, {"Team": "Queens Park Rangers", "strength": 2}, {"Team": "Sheffield Wednesday", "strength": 2}, {"Team": "Stoke City", "strength": 3}, {"Team": "Sunderland", "strength": 3}, {"Team": "Swansea", "strength": 3}, {"Team": "Watford", "strength": 3}, {"Team": "West Bromwich Albion", "strength": 3}, {"Team": "Sheffield United", "strength": 3}]

def main():
    global premTeamsStrength
    global premTeams
    seasons = ["2024/25", "2025/26", "2026/27", "2027/28", "2028/29", "2029/30", "2030/31", "2031/32", "2032/33", "2033/34 (Final)"]
    pos = ["\033[0;33m1\033[0;0m", "\033[1;34m2\033[0;0m", "\033[1;34m3\033[0;0m", "\033[1;34m4\033[0;0m", "\033[1;35m5\033[0;0m", "\033[1;35m6\033[0;0m", "\033[0;32m7\033[0;0m", 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,"\033[1;31m18\033[0;0m" ,"\033[1;31m19\033[0;0m", "\033[1;31m20\033[0;0m"]
    seasonsCompleted = 0
    relegated = False
    cont = True
    titles = 0

    stats = initStats()
    print(tabulate(stats, headers="keys", tablefmt="rounded_grid"))

    myteam = get_team()

    for team in premTeams:
        if team == myteam:
            premTeams.remove(team)

    while seasonsCompleted < 10 and not relegated and cont:
        stats = initStats()
        print(f"\n\033[1mSeason\033[0;0m: {seasons[seasonsCompleted]}")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))

        print("\n\033[1mMatchday 1\033[0;0m:")
        print(f"{premTeams[12]} vs {premTeams[7]}")
        print(f"{premTeams[8]} vs {premTeams[10]}")
        print(f"{premTeams[1]} vs {premTeams[18]}")
        print(f"{premTeams[13]} vs {premTeams[15]}")
        print(f"{premTeams[14]} vs {premTeams[0]}")
        print(f"{premTeams[17]} vs {premTeams[2]}")
        print(f"{premTeams[3]} vs {premTeams[6]}")
        print(f"{premTeams[5]} vs {premTeams[11]}")
        print(f"{premTeams[9]} vs {premTeams[16]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[4]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[12], premTeams[7], stats)
        results(premTeams[8], premTeams[10], stats)
        results(premTeams[1], premTeams[18], stats)
        results(premTeams[13], premTeams[15], stats)
        results(premTeams[14], premTeams[0], stats)
        results(premTeams[17], premTeams[2], stats)
        results(premTeams[3], premTeams[6], stats)
        results(premTeams[5], premTeams[11], stats)
        results(premTeams[9], premTeams[16], stats)

        if result == "W":
            myresults(myteam, premTeams[4], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[4], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[4], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 2\033[0;0m:")
        print(f"{premTeams[4]} vs {premTeams[12]}")
        print(f"{premTeams[6]} vs {premTeams[17]}")
        print(f"{premTeams[15]} vs {premTeams[14]}")
        print(f"{premTeams[7]} vs {premTeams[9]}")
        print(f"{premTeams[11]} vs {premTeams[8]}")
        print(f"{premTeams[2]} vs {premTeams[1]}")
        print(f"{premTeams[0]} vs {premTeams[13]}")
        print(f"{premTeams[18]} vs {premTeams[5]}")
        print(f"{premTeams[10]} vs {premTeams[3]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[16]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[4], premTeams[12], stats)
        results(premTeams[6], premTeams[17], stats)
        results(premTeams[15], premTeams[14], stats)
        results(premTeams[7], premTeams[9], stats)
        results(premTeams[11], premTeams[8], stats)
        results(premTeams[2], premTeams[1], stats)
        results(premTeams[0], premTeams[13], stats)
        results(premTeams[18], premTeams[5], stats)
        results(premTeams[10], premTeams[3], stats)

        if result == "W":
            myresults(premTeams[16], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[16], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[16], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 3\033[0;0m:")
        print(f"{premTeams[1]} vs {premTeams[4]}")
        print(f"{premTeams[14]} vs {premTeams[18]}")
        print(f"{premTeams[9]} vs {premTeams[2]}")
        print(f"{premTeams[8]} vs {premTeams[7]}")
        print(f"{premTeams[3]} vs {premTeams[15]}")
        print(f"{premTeams[17]} vs {premTeams[11]}")
        print(f"{premTeams[5]} vs {premTeams[6]}")
        print(f"{premTeams[13]} vs {premTeams[16]}")
        print(f"{premTeams[12]} vs {premTeams[10]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[0]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[1], premTeams[4], stats)
        results(premTeams[14], premTeams[18], stats)
        results(premTeams[9], premTeams[2], stats)
        results(premTeams[8], premTeams[7], stats)
        results(premTeams[3], premTeams[15], stats)
        results(premTeams[17], premTeams[11], stats)
        results(premTeams[5], premTeams[6], stats)
        results(premTeams[13], premTeams[16], stats)
        results(premTeams[12], premTeams[10], stats)

        if result == "W":
            myresults(myteam, premTeams[0], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[0], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[0], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 4\033[0;0m:")
        print(f"{premTeams[15]} vs {premTeams[12]}")
        print(f"{premTeams[10]} vs {premTeams[14]}")
        print(f"{premTeams[11]} vs {premTeams[3]}")
        print(f"{premTeams[7]} vs {premTeams[17]}")
        print(f"{premTeams[6]} vs {premTeams[9]}")
        print(f"{premTeams[4]} vs {premTeams[8]}")
        print(f"{premTeams[0]} vs {premTeams[5]}")
        print(f"{premTeams[16]} vs {premTeams[1]}")
        print(f"{premTeams[18]} vs {premTeams[13]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[2]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[15], premTeams[12], stats)
        results(premTeams[10], premTeams[14], stats)
        results(premTeams[11], premTeams[3], stats)
        results(premTeams[7], premTeams[17], stats)
        results(premTeams[6], premTeams[9], stats)
        results(premTeams[4], premTeams[8], stats)
        results(premTeams[0], premTeams[5], stats)
        results(premTeams[16], premTeams[1], stats)
        results(premTeams[18], premTeams[13], stats)

        if result == "W":
            myresults(premTeams[2], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[2], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[2], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 5\033[0;0m:")
        print(f"{premTeams[17]} vs {premTeams[5]}")
        print(f"{premTeams[2]} vs {premTeams[18]}")
        print(f"{premTeams[7]} vs {premTeams[13]}")
        print(f"{premTeams[15]} vs {premTeams[8]}")
        print(f"{premTeams[16]} vs {premTeams[3]}")
        print(f"{premTeams[10]} vs {premTeams[0]}")
        print(f"{premTeams[6]} vs {premTeams[12]}")
        print(f"{premTeams[4]} vs {premTeams[14]}")
        print(f"{premTeams[11]} vs {premTeams[1]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[9]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[17], premTeams[5], stats)
        results(premTeams[2], premTeams[18], stats)
        results(premTeams[7], premTeams[13], stats)
        results(premTeams[15], premTeams[8], stats)
        results(premTeams[16], premTeams[3], stats)
        results(premTeams[10], premTeams[0], stats)
        results(premTeams[6], premTeams[12], stats)
        results(premTeams[4], premTeams[14], stats)
        results(premTeams[11], premTeams[1], stats)

        if result == "W":
            myresults(premTeams[9], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[9], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[9], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 6\033[0;0m:")
        print(f"{premTeams[13]} vs {premTeams[11]}")
        print(f"{premTeams[5]} vs {premTeams[4]}")
        print(f"{premTeams[3]} vs {premTeams[17]}")
        print(f"{premTeams[1]} vs {premTeams[9]}")
        print(f"{premTeams[14]} vs {premTeams[7]}")
        print(f"{premTeams[18]} vs {premTeams[10]}")
        print(f"{premTeams[8]} vs {premTeams[2]}")
        print(f"{premTeams[12]} vs {premTeams[16]}")
        print(f"{premTeams[0]} vs {premTeams[15]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[6]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[13], premTeams[11], stats)
        results(premTeams[5], premTeams[4], stats)
        results(premTeams[3], premTeams[17], stats)
        results(premTeams[1], premTeams[9], stats)
        results(premTeams[14], premTeams[7], stats)
        results(premTeams[18], premTeams[10], stats)
        results(premTeams[8], premTeams[2], stats)
        results(premTeams[12], premTeams[16], stats)
        results(premTeams[0], premTeams[15], stats)

        if result == "W":
            myresults(myteam, premTeams[6], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[6], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[6], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 7\033[0;0m:")
        print(f"{premTeams[6]} vs {premTeams[10]}")
        print(f"{premTeams[1]} vs {premTeams[15]}")
        print(f"{premTeams[3]} vs {premTeams[18]}")
        print(f"{premTeams[2]} vs {premTeams[12]}")
        print(f"{premTeams[11]} vs {premTeams[7]}")
        print(f"{premTeams[17]} vs {premTeams[8]}")
        print(f"{premTeams[9]} vs {premTeams[0]}")
        print(f"{premTeams[5]} vs {premTeams[14]}")
        print(f"{premTeams[4]} vs {premTeams[16]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[13]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[6], premTeams[10], stats)
        results(premTeams[1], premTeams[15], stats)
        results(premTeams[3], premTeams[18], stats)
        results(premTeams[2], premTeams[12], stats)
        results(premTeams[11], premTeams[7], stats)
        results(premTeams[17], premTeams[8], stats)
        results(premTeams[9], premTeams[0], stats)
        results(premTeams[5], premTeams[14], stats)
        results(premTeams[4], premTeams[16], stats)

        if result == "W":
            myresults(myteam, premTeams[13], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[13], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[13], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 8\033[0;0m:")
        print(f"{premTeams[18]} vs {premTeams[11]}")
        print(f"{premTeams[16]} vs {premTeams[17]}")
        print(f"{premTeams[10]} vs {premTeams[5]}")
        print(f"{premTeams[12]} vs {premTeams[3]}")
        print(f"{premTeams[7]} vs {premTeams[2]}")
        print(f"{premTeams[13]} vs {premTeams[4]}")
        print(f"{premTeams[0]} vs {premTeams[1]}")
        print(f"{premTeams[14]} vs {premTeams[6]}")
        print(f"{premTeams[15]} vs {premTeams[9]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[8]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[18], premTeams[11], stats)
        results(premTeams[16], premTeams[17], stats)
        results(premTeams[10], premTeams[5], stats)
        results(premTeams[12], premTeams[3], stats)
        results(premTeams[7], premTeams[2], stats)
        results(premTeams[13], premTeams[4], stats)
        results(premTeams[0], premTeams[1], stats)
        results(premTeams[14], premTeams[6], stats)
        results(premTeams[15], premTeams[9], stats)

        if result == "W":
            myresults(premTeams[8], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[8], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[8], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 9\033[0;0m:")
        print(f"{premTeams[11]} vs {premTeams[15]}")
        print(f"{premTeams[6]} vs {premTeams[16]}")
        print(f"{premTeams[3]} vs {premTeams[8]}")
        print(f"{premTeams[5]} vs {premTeams[13]}")
        print(f"{premTeams[1]} vs {premTeams[10]}")
        print(f"{premTeams[4]} vs {premTeams[18]}")
        print(f"{premTeams[9]} vs {premTeams[14]}")
        print(f"{premTeams[2]} vs {premTeams[0]}")
        print(f"{premTeams[17]} vs {premTeams[12]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[7]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[11], premTeams[15], stats)
        results(premTeams[6], premTeams[16], stats)
        results(premTeams[3], premTeams[8], stats)
        results(premTeams[5], premTeams[13], stats)
        results(premTeams[1], premTeams[10], stats)
        results(premTeams[4], premTeams[18], stats)
        results(premTeams[9], premTeams[14], stats)
        results(premTeams[2], premTeams[0], stats)
        results(premTeams[17], premTeams[12], stats)

        if result == "W":
            myresults(myteam, premTeams[7], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[7], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[7], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 10\033[0;0m:")
        print(f"{premTeams[16]} vs {premTeams[2]}")
        print(f"{premTeams[18]} vs {premTeams[6]}")
        print(f"{premTeams[10]} vs {premTeams[4]}")
        print(f"{premTeams[13]} vs {premTeams[1]}")
        print(f"{premTeams[7]} vs {premTeams[3]}")
        print(f"{premTeams[8]} vs {premTeams[9]}")
        print(f"{premTeams[12]} vs {premTeams[5]}")
        print(f"{premTeams[0]} vs {premTeams[11]}")
        print(f"{premTeams[14]} vs {premTeams[17]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[15]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[16], premTeams[2], stats)
        results(premTeams[18], premTeams[6], stats)
        results(premTeams[10], premTeams[4], stats)
        results(premTeams[13], premTeams[1], stats)
        results(premTeams[7], premTeams[3], stats)
        results(premTeams[8], premTeams[9], stats)
        results(premTeams[12], premTeams[5], stats)
        results(premTeams[0], premTeams[11], stats)
        results(premTeams[14], premTeams[17], stats)

        if result == "W":
            myresults(premTeams[15], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[15], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[15], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 11\033[0;0m:")
        print(f"{premTeams[18]} vs {premTeams[15]}")
        print(f"{premTeams[12]} vs {premTeams[9]}")
        print(f"{premTeams[14]} vs {premTeams[13]}")
        print(f"{premTeams[16]} vs {premTeams[8]}")
        print(f"{premTeams[3]} vs {premTeams[0]}")
        print(f"{premTeams[10]} vs {premTeams[2]}")
        print(f"{premTeams[6]} vs {premTeams[7]}")
        print(f"{premTeams[5]} vs {premTeams[1]}")
        print(f"{premTeams[4]} vs {premTeams[11]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[17]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[18], premTeams[15], stats)
        results(premTeams[12], premTeams[9], stats)
        results(premTeams[14], premTeams[13], stats)
        results(premTeams[16], premTeams[8], stats)
        results(premTeams[3], premTeams[0], stats)
        results(premTeams[10], premTeams[2], stats)
        results(premTeams[6], premTeams[7], stats)
        results(premTeams[5], premTeams[1], stats)
        results(premTeams[4], premTeams[11], stats)

        if result == "W":
            myresults(premTeams[17], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[17], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[17], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 12\033[0;0m:")
        print(f"{premTeams[13]} vs {premTeams[17]}")
        print(f"{premTeams[7]} vs {premTeams[18]}")
        print(f"{premTeams[8]} vs {premTeams[12]}")
        print(f"{premTeams[9]} vs {premTeams[5]}")
        print(f"{premTeams[1]} vs {premTeams[14]}")
        print(f"{premTeams[0]} vs {premTeams[4]}")
        print(f"{premTeams[15]} vs {premTeams[10]}")
        print(f"{premTeams[2]} vs {premTeams[6]}")
        print(f"{premTeams[11]} vs {premTeams[16]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[3]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[13], premTeams[17], stats)
        results(premTeams[7], premTeams[18], stats)
        results(premTeams[8], premTeams[12], stats)
        results(premTeams[9], premTeams[5], stats)
        results(premTeams[1], premTeams[14], stats)
        results(premTeams[0], premTeams[4], stats)
        results(premTeams[15], premTeams[10], stats)
        results(premTeams[2], premTeams[6], stats)
        results(premTeams[11], premTeams[16], stats)

        if result == "W":
            myresults(myteam, premTeams[3], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[3], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[3], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 13\033[0;0m:")
        print(f"{premTeams[4]} vs {premTeams[15]}")
        print(f"{premTeams[18]} vs {premTeams[0]}")
        print(f"{premTeams[17]} vs {premTeams[1]}")
        print(f"{premTeams[6]} vs {premTeams[13]}")
        print(f"{premTeams[14]} vs {premTeams[8]}")
        print(f"{premTeams[10]} vs {premTeams[11]}")
        print(f"{premTeams[5]} vs {premTeams[2]}")
        print(f"{premTeams[16]} vs {premTeams[7]}")
        print(f"{premTeams[3]} vs {premTeams[9]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[12]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[4], premTeams[15], stats)
        results(premTeams[18], premTeams[0], stats)
        results(premTeams[17], premTeams[1], stats)
        results(premTeams[6], premTeams[13], stats)
        results(premTeams[14], premTeams[8], stats)
        results(premTeams[10], premTeams[11], stats)
        results(premTeams[5], premTeams[2], stats)
        results(premTeams[16], premTeams[7], stats)
        results(premTeams[3], premTeams[9], stats)

        if result == "W":
            myresults(premTeams[12], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[12], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[12], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 14\033[0;0m:")
        print(f"{premTeams[1]} vs {premTeams[12]}")
        print(f"{premTeams[7]} vs {premTeams[4]}")
        print(f"{premTeams[0]} vs {premTeams[16]}")
        print(f"{premTeams[2]} vs {premTeams[3]}")
        print(f"{premTeams[9]} vs {premTeams[17]}")
        print(f"{premTeams[8]} vs {premTeams[6]}")
        print(f"{premTeams[15]} vs {premTeams[5]}")
        print(f"{premTeams[11]} vs {premTeams[14]}")
        print(f"{premTeams[13]} vs {premTeams[10]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[18]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[1], premTeams[12], stats)
        results(premTeams[7], premTeams[4], stats)
        results(premTeams[0], premTeams[16], stats)
        results(premTeams[2], premTeams[3], stats)
        results(premTeams[9], premTeams[17], stats)
        results(premTeams[8], premTeams[6], stats)
        results(premTeams[15], premTeams[5], stats)
        results(premTeams[11], premTeams[14], stats)
        results(premTeams[13], premTeams[10], stats)

        if result == "W":
            myresults(myteam, premTeams[18], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[18], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[18], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 15\033[0;0m:")
        print(f"{premTeams[3]} vs {premTeams[13]}")
        print(f"{premTeams[7]} vs {premTeams[1]}")
        print(f"{premTeams[2]} vs {premTeams[15]}")
        print(f"{premTeams[6]} vs {premTeams[11]}")
        print(f"{premTeams[9]} vs {premTeams[4]}")
        print(f"{premTeams[16]} vs {premTeams[5]}")
        print(f"{premTeams[17]} vs {premTeams[18]}")
        print(f"{premTeams[12]} vs {premTeams[14]}")
        print(f"{premTeams[8]} vs {premTeams[0]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[10]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[3], premTeams[13], stats)
        results(premTeams[7], premTeams[1], stats)
        results(premTeams[2], premTeams[15], stats)
        results(premTeams[6], premTeams[11], stats)
        results(premTeams[9], premTeams[4], stats)
        results(premTeams[16], premTeams[5], stats)
        results(premTeams[17], premTeams[18], stats)
        results(premTeams[12], premTeams[14], stats)
        results(premTeams[8], premTeams[0], stats)

        if result == "W":
            myresults(myteam, premTeams[10], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[10], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[10], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 16\033[0;0m:")
        print(f"{premTeams[0]} vs {premTeams[17]}")
        print(f"{premTeams[15]} vs {premTeams[16]}")
        print(f"{premTeams[4]} vs {premTeams[6]}")
        print(f"{premTeams[5]} vs {premTeams[3]}")
        print(f"{premTeams[18]} vs {premTeams[8]}")
        print(f"{premTeams[13]} vs {premTeams[9]}")
        print(f"{premTeams[10]} vs {premTeams[7]}")
        print(f"{premTeams[14]} vs {premTeams[2]}")
        print(f"{premTeams[11]} vs {premTeams[12]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[1]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[0], premTeams[17], stats)
        results(premTeams[15], premTeams[16], stats)
        results(premTeams[4], premTeams[6], stats)
        results(premTeams[5], premTeams[3], stats)
        results(premTeams[18], premTeams[8], stats)
        results(premTeams[13], premTeams[9], stats)
        results(premTeams[10], premTeams[7], stats)
        results(premTeams[14], premTeams[2], stats)
        results(premTeams[11], premTeams[12], stats)

        if result == "W":
            myresults(premTeams[1], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[1], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[1], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 17\033[0;0m:")
        print(f"{premTeams[6]} vs {premTeams[1]}")
        print(f"{premTeams[12]} vs {premTeams[0]}")
        print(f"{premTeams[16]} vs {premTeams[10]}")
        print(f"{premTeams[17]} vs {premTeams[4]}")
        print(f"{premTeams[7]} vs {premTeams[15]}")
        print(f"{premTeams[9]} vs {premTeams[18]}")
        print(f"{premTeams[8]} vs {premTeams[13]}")
        print(f"{premTeams[3]} vs {premTeams[14]}")
        print(f"{premTeams[2]} vs {premTeams[11]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[5]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[6], premTeams[1], stats)
        results(premTeams[12], premTeams[0], stats)
        results(premTeams[16], premTeams[10], stats)
        results(premTeams[17], premTeams[4], stats)
        results(premTeams[7], premTeams[15], stats)
        results(premTeams[9], premTeams[18], stats)
        results(premTeams[8], premTeams[13], stats)
        results(premTeams[3], premTeams[14], stats)
        results(premTeams[2], premTeams[11], stats)

        if result == "W":
            myresults(myteam, premTeams[5], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[5], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[5], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 18\033[0;0m:")
        print(f"{premTeams[13]} vs {premTeams[2]}")
        print(f"{premTeams[14]} vs {premTeams[16]}")
        print(f"{premTeams[18]} vs {premTeams[12]}")
        print(f"{premTeams[4]} vs {premTeams[3]}")
        print(f"{premTeams[0]} vs {premTeams[6]}")
        print(f"{premTeams[10]} vs {premTeams[9]}")
        print(f"{premTeams[5]} vs {premTeams[7]}")
        print(f"{premTeams[15]} vs {premTeams[17]}")
        print(f"{premTeams[1]} vs {premTeams[8]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[11]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[13], premTeams[2], stats)
        results(premTeams[14], premTeams[16], stats)
        results(premTeams[18], premTeams[12], stats)
        results(premTeams[4], premTeams[3], stats)
        results(premTeams[0], premTeams[6], stats)
        results(premTeams[10], premTeams[9], stats)
        results(premTeams[5], premTeams[7], stats)
        results(premTeams[15], premTeams[17], stats)
        results(premTeams[1], premTeams[8], stats)

        if result == "W":
            myresults(premTeams[11], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[11], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[11], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 19\033[0;0m:")
        print(f"{premTeams[3]} vs {premTeams[1]}")
        print(f"{premTeams[17]} vs {premTeams[10]}")
        print(f"{premTeams[6]} vs {premTeams[15]}")
        print(f"{premTeams[16]} vs {premTeams[18]}")
        print(f"{premTeams[7]} vs {premTeams[0]}")
        print(f"{premTeams[8]} vs {premTeams[5]}")
        print(f"{premTeams[12]} vs {premTeams[13]}")
        print(f"{premTeams[2]} vs {premTeams[4]}")
        print(f"{premTeams[9]} vs {premTeams[11]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[14]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[3], premTeams[1], stats)
        results(premTeams[17], premTeams[10], stats)
        results(premTeams[6], premTeams[15], stats)
        results(premTeams[16], premTeams[18], stats)
        results(premTeams[7], premTeams[0], stats)
        results(premTeams[8], premTeams[5], stats)
        results(premTeams[12], premTeams[13], stats)
        results(premTeams[2], premTeams[4], stats)
        results(premTeams[9], premTeams[11], stats)

        if result == "W":
            myresults(myteam, premTeams[14], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[14], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[14], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 20\033[0;0m:")
        print(f"{premTeams[4]} vs {premTeams[1]}")
        print(f"{premTeams[2]} vs {premTeams[9]}")
        print(f"{premTeams[18]} vs {premTeams[14]}")
        print(f"{premTeams[7]} vs {premTeams[8]}")
        print(f"{premTeams[6]} vs {premTeams[5]}")
        print(f"{premTeams[15]} vs {premTeams[3]}")
        print(f"{premTeams[16]} vs {premTeams[13]}")
        print(f"{premTeams[10]} vs {premTeams[12]}")
        print(f"{premTeams[11]} vs {premTeams[17]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[0]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[4], premTeams[1], stats)
        results(premTeams[2], premTeams[9], stats)
        results(premTeams[18], premTeams[14], stats)
        results(premTeams[7], premTeams[8], stats)
        results(premTeams[6], premTeams[5], stats)
        results(premTeams[15], premTeams[3], stats)
        results(premTeams[16], premTeams[13], stats)
        results(premTeams[10], premTeams[12], stats)
        results(premTeams[11], premTeams[17], stats)

        if result == "W":
            myresults(premTeams[0], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[0], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[0], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 21\033[0;0m:")
        print(f"{premTeams[14]} vs {premTeams[10]}")
        print(f"{premTeams[17]} vs {premTeams[7]}")
        print(f"{premTeams[3]} vs {premTeams[11]}")
        print(f"{premTeams[8]} vs {premTeams[4]}")
        print(f"{premTeams[9]} vs {premTeams[6]}")
        print(f"{premTeams[1]} vs {premTeams[16]}")
        print(f"{premTeams[5]} vs {premTeams[0]}")
        print(f"{premTeams[13]} vs {premTeams[18]}")
        print(f"{premTeams[12]} vs {premTeams[15]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[2]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[14], premTeams[10], stats)
        results(premTeams[17], premTeams[7], stats)
        results(premTeams[3], premTeams[11], stats)
        results(premTeams[8], premTeams[4], stats)
        results(premTeams[9], premTeams[6], stats)
        results(premTeams[1], premTeams[16], stats)
        results(premTeams[5], premTeams[0], stats)
        results(premTeams[13], premTeams[18], stats)
        results(premTeams[12], premTeams[15], stats)

        if result == "W":
            myresults(myteam, premTeams[2], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[2], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[2], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 22\033[0;0m:")
        print(f"{premTeams[13]} vs {premTeams[0]}")
        print(f"{premTeams[14]} vs {premTeams[15]}")
        print(f"{premTeams[17]} vs {premTeams[6]}")
        print(f"{premTeams[3]} vs {premTeams[10]}")
        print(f"{premTeams[1]} vs {premTeams[2]}")
        print(f"{premTeams[8]} vs {premTeams[11]}")
        print(f"{premTeams[9]} vs {premTeams[7]}")
        print(f"{premTeams[12]} vs {premTeams[4]}")
        print(f"{premTeams[5]} vs {premTeams[18]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[16]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[13], premTeams[0], stats)
        results(premTeams[14], premTeams[15], stats)
        results(premTeams[17], premTeams[6], stats)
        results(premTeams[3], premTeams[10], stats)
        results(premTeams[1], premTeams[2], stats)
        results(premTeams[8], premTeams[11], stats)
        results(premTeams[9], premTeams[7], stats)
        results(premTeams[12], premTeams[4], stats)
        results(premTeams[5], premTeams[18], stats)

        if result == "W":
            myresults(myteam, premTeams[16], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[16], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[16], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 23\033[0;0m:")
        print(f"{premTeams[11]} vs {premTeams[5]}")
        print(f"{premTeams[10]} vs {premTeams[8]}")
        print(f"{premTeams[7]} vs {premTeams[12]}")
        print(f"{premTeams[2]} vs {premTeams[17]}")
        print(f"{premTeams[15]} vs {premTeams[13]}")
        print(f"{premTeams[18]} vs {premTeams[1]}")
        print(f"{premTeams[16]} vs {premTeams[9]}")
        print(f"{premTeams[0]} vs {premTeams[14]}")
        print(f"{premTeams[6]} vs {premTeams[3]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[4]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[11], premTeams[5], stats)
        results(premTeams[10], premTeams[8], stats)
        results(premTeams[7], premTeams[12], stats)
        results(premTeams[2], premTeams[17], stats)
        results(premTeams[15], premTeams[13], stats)
        results(premTeams[18], premTeams[1], stats)
        results(premTeams[16], premTeams[9], stats)
        results(premTeams[0], premTeams[14], stats)
        results(premTeams[6], premTeams[3], stats)

        if result == "W":
            myresults(premTeams[4], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[4], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[4], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 24\033[0;0m:")
        print(f"{premTeams[12]} vs {premTeams[6]}")
        print(f"{premTeams[13]} vs {premTeams[7]}")
        print(f"{premTeams[5]} vs {premTeams[17]}")
        print(f"{premTeams[3]} vs {premTeams[16]}")
        print(f"{premTeams[8]} vs {premTeams[15]}")
        print(f"{premTeams[1]} vs {premTeams[11]}")
        print(f"{premTeams[14]} vs {premTeams[4]}")
        print(f"{premTeams[0]} vs {premTeams[10]}")
        print(f"{premTeams[18]} vs {premTeams[2]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[9]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[12], premTeams[6], stats)
        results(premTeams[13], premTeams[7], stats)
        results(premTeams[5], premTeams[17], stats)
        results(premTeams[3], premTeams[16], stats)
        results(premTeams[8], premTeams[15], stats)
        results(premTeams[1], premTeams[11], stats)
        results(premTeams[14], premTeams[4], stats)
        results(premTeams[0], premTeams[10], stats)
        results(premTeams[18], premTeams[2], stats)

        if result == "W":
            myresults(myteam, premTeams[9], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[9], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[9], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 25\033[0;0m:")
        print(f"{premTeams[9]} vs {premTeams[1]}")
        print(f"{premTeams[17]} vs {premTeams[3]}")
        print(f"{premTeams[15]} vs {premTeams[0]}")
        print(f"{premTeams[2]} vs {premTeams[8]}")
        print(f"{premTeams[10]} vs {premTeams[18]}")
        print(f"{premTeams[11]} vs {premTeams[13]}")
        print(f"{premTeams[4]} vs {premTeams[5]}")
        print(f"{premTeams[7]} vs {premTeams[14]}")
        print(f"{premTeams[16]} vs {premTeams[12]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[6]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[9], premTeams[1], stats)
        results(premTeams[17], premTeams[3], stats)
        results(premTeams[15], premTeams[0], stats)
        results(premTeams[2], premTeams[8], stats)
        results(premTeams[10], premTeams[18], stats)
        results(premTeams[11], premTeams[13], stats)
        results(premTeams[4], premTeams[5], stats)
        results(premTeams[7], premTeams[14], stats)
        results(premTeams[16], premTeams[12], stats)

        if result == "W":
            myresults(premTeams[6], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[6], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[6], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 26\033[0;0m:")
        print(f"{premTeams[2]} vs {premTeams[5]}")
        print(f"{premTeams[0]} vs {premTeams[18]}")
        print(f"{premTeams[9]} vs {premTeams[3]}")
        print(f"{premTeams[8]} vs {premTeams[16]}")
        print(f"{premTeams[15]} vs {premTeams[4]}")
        print(f"{premTeams[1]} vs {premTeams[17]}")
        print(f"{premTeams[13]} vs {premTeams[14]}")
        print(f"{premTeams[11]} vs {premTeams[10]}")
        print(f"{premTeams[7]} vs {premTeams[6]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[12]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[2], premTeams[5], stats)
        results(premTeams[0], premTeams[18], stats)
        results(premTeams[9], premTeams[3], stats)
        results(premTeams[8], premTeams[16], stats)
        results(premTeams[15], premTeams[4], stats)
        results(premTeams[1], premTeams[17], stats)
        results(premTeams[13], premTeams[14], stats)
        results(premTeams[11], premTeams[10], stats)
        results(premTeams[7], premTeams[6], stats)

        if result == "W":
            myresults(myteam, premTeams[12], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[12], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[12], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 27\033[0;0m:")
        print(f"{premTeams[4]} vs {premTeams[0]}")
        print(f"{premTeams[17]} vs {premTeams[9]}")
        print(f"{premTeams[16]} vs {premTeams[11]}")
        print(f"{premTeams[14]} vs {premTeams[1]}")
        print(f"{premTeams[18]} vs {premTeams[7]}")
        print(f"{premTeams[6]} vs {premTeams[2]}")
        print(f"{premTeams[5]} vs {premTeams[15]}")
        print(f"{premTeams[10]} vs {premTeams[13]}")
        print(f"{premTeams[12]} vs {premTeams[8]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[3]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[4], premTeams[0], stats)
        results(premTeams[17], premTeams[9], stats)
        results(premTeams[16], premTeams[11], stats)
        results(premTeams[14], premTeams[1], stats)
        results(premTeams[18], premTeams[7], stats)
        results(premTeams[6], premTeams[2], stats)
        results(premTeams[5], premTeams[15], stats)
        results(premTeams[10], premTeams[13], stats)
        results(premTeams[12], premTeams[8], stats)

        if result == "W":
            myresults(premTeams[3], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[3], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[3], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 28\033[0;0m:")
        print(f"{premTeams[14]} vs {premTeams[11]}")
        print(f"{premTeams[12]} vs {premTeams[1]}")
        print(f"{premTeams[16]} vs {premTeams[0]}")
        print(f"{premTeams[10]} vs {premTeams[15]}")
        print(f"{premTeams[5]} vs {premTeams[9]}")
        print(f"{premTeams[3]} vs {premTeams[2]}")
        print(f"{premTeams[17]} vs {premTeams[13]}")
        print(f"{premTeams[6]} vs {premTeams[8]}")
        print(f"{premTeams[4]} vs {premTeams[7]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[18]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[14], premTeams[11], stats)
        results(premTeams[12], premTeams[1], stats)
        results(premTeams[16], premTeams[0], stats)
        results(premTeams[10], premTeams[15], stats)
        results(premTeams[5], premTeams[9], stats)
        results(premTeams[3], premTeams[2], stats)
        results(premTeams[17], premTeams[13], stats)
        results(premTeams[6], premTeams[8], stats)
        results(premTeams[4], premTeams[7], stats)

        if result == "W":
            myresults(premTeams[18], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[18], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[18], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 29\033[0;0m:")
        print(f"{premTeams[9]} vs {premTeams[12]}")
        print(f"{premTeams[15]} vs {premTeams[18]}")
        print(f"{premTeams[8]} vs {premTeams[14]}")
        print(f"{premTeams[2]} vs {premTeams[10]}")
        print(f"{premTeams[0]} vs {premTeams[3]}")
        print(f"{premTeams[11]} vs {premTeams[4]}")
        print(f"{premTeams[1]} vs {premTeams[5]}")
        print(f"{premTeams[7]} vs {premTeams[16]}")
        print(f"{premTeams[13]} vs {premTeams[6]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[17]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[9], premTeams[12], stats)
        results(premTeams[15], premTeams[18], stats)
        results(premTeams[8], premTeams[14], stats)
        results(premTeams[2], premTeams[10], stats)
        results(premTeams[0], premTeams[3], stats)
        results(premTeams[11], premTeams[4], stats)
        results(premTeams[1], premTeams[5], stats)
        results(premTeams[7], premTeams[16], stats)
        results(premTeams[13], premTeams[6], stats)

        if result == "W":
            myresults(myteam, premTeams[17], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[17], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[17], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 30\033[0;0m:")
        print(f"{premTeams[18]} vs {premTeams[17]}")
        print(f"{premTeams[0]} vs {premTeams[8]}")
        print(f"{premTeams[4]} vs {premTeams[2]}")
        print(f"{premTeams[14]} vs {premTeams[12]}")
        print(f"{premTeams[1]} vs {premTeams[7]}")
        print(f"{premTeams[15]} vs {premTeams[6]}")
        print(f"{premTeams[5]} vs {premTeams[16]}")
        print(f"{premTeams[13]} vs {premTeams[3]}")
        print(f"{premTeams[11]} vs {premTeams[9]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[10]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[18], premTeams[17], stats)
        results(premTeams[0], premTeams[8], stats)
        results(premTeams[4], premTeams[2], stats)
        results(premTeams[14], premTeams[12], stats)
        results(premTeams[1], premTeams[7], stats)
        results(premTeams[15], premTeams[6], stats)
        results(premTeams[5], premTeams[16], stats)
        results(premTeams[13], premTeams[3], stats)
        results(premTeams[11], premTeams[9], stats)

        if result == "W":
            myresults(premTeams[10], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[10], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[10], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 31\033[0;0m:")
        print(f"{premTeams[2]} vs {premTeams[14]}")
        print(f"{premTeams[8]} vs {premTeams[18]}")
        print(f"{premTeams[9]} vs {premTeams[13]}")
        print(f"{premTeams[16]} vs {premTeams[15]}")
        print(f"{premTeams[12]} vs {premTeams[11]}")
        print(f"{premTeams[3]} vs {premTeams[5]}")
        print(f"{premTeams[6]} vs {premTeams[4]}")
        print(f"{premTeams[7]} vs {premTeams[10]}")
        print(f"{premTeams[17]} vs {premTeams[0]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[1]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[2], premTeams[14], stats)
        results(premTeams[8], premTeams[18], stats)
        results(premTeams[9], premTeams[13], stats)
        results(premTeams[16], premTeams[15], stats)
        results(premTeams[12], premTeams[11], stats)
        results(premTeams[3], premTeams[5], stats)
        results(premTeams[6], premTeams[4], stats)
        results(premTeams[7], premTeams[10], stats)
        results(premTeams[17], premTeams[0], stats)

        if result == "W":
            myresults(myteam, premTeams[1], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[1], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[1], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 32\033[0;0m:")
        print(f"{premTeams[15]} vs {premTeams[2]}")
        print(f"{premTeams[1]} vs {premTeams[3]}")
        print(f"{premTeams[5]} vs {premTeams[8]}")
        print(f"{premTeams[18]} vs {premTeams[16]}")
        print(f"{premTeams[13]} vs {premTeams[12]}")
        print(f"{premTeams[10]} vs {premTeams[17]}")
        print(f"{premTeams[11]} vs {premTeams[6]}")
        print(f"{premTeams[0]} vs {premTeams[7]}")
        print(f"{premTeams[4]} vs {premTeams[9]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[14]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[15], premTeams[2], stats)
        results(premTeams[1], premTeams[3], stats)
        results(premTeams[5], premTeams[8], stats)
        results(premTeams[18], premTeams[16], stats)
        results(premTeams[13], premTeams[12], stats)
        results(premTeams[10], premTeams[17], stats)
        results(premTeams[11], premTeams[6], stats)
        results(premTeams[0], premTeams[7], stats)
        results(premTeams[4], premTeams[9], stats)

        if result == "W":
            myresults(premTeams[14], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[14], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[14], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 33\033[0;0m:")
        print(f"{premTeams[2]} vs {premTeams[13]}")
        print(f"{premTeams[8]} vs {premTeams[1]}")
        print(f"{premTeams[3]} vs {premTeams[4]}")
        print(f"{premTeams[9]} vs {premTeams[10]}")
        print(f"{premTeams[17]} vs {premTeams[15]}")
        print(f"{premTeams[16]} vs {premTeams[14]}")
        print(f"{premTeams[6]} vs {premTeams[0]}")
        print(f"{premTeams[12]} vs {premTeams[18]}")
        print(f"{premTeams[7]} vs {premTeams[5]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[11]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[2], premTeams[13], stats)
        results(premTeams[8], premTeams[1], stats)
        results(premTeams[3], premTeams[4], stats)
        results(premTeams[9], premTeams[10], stats)
        results(premTeams[17], premTeams[15], stats)
        results(premTeams[16], premTeams[14], stats)
        results(premTeams[6], premTeams[0], stats)
        results(premTeams[12], premTeams[18], stats)
        results(premTeams[7], premTeams[5], stats)

        if result == "W":
            myresults(myteam, premTeams[11], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[11], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[11], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 34\033[0;0m:")
        print(f"{premTeams[1]} vs {premTeams[6]}")
        print(f"{premTeams[14]} vs {premTeams[3]}")
        print(f"{premTeams[18]} vs {premTeams[9]}")
        print(f"{premTeams[10]} vs {premTeams[16]}")
        print(f"{premTeams[13]} vs {premTeams[8]}")
        print(f"{premTeams[4]} vs {premTeams[17]}")
        print(f"{premTeams[0]} vs {premTeams[12]}")
        print(f"{premTeams[15]} vs {premTeams[7]}")
        print(f"{premTeams[11]} vs {premTeams[2]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[5]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[1], premTeams[6], stats)
        results(premTeams[14], premTeams[3], stats)
        results(premTeams[18], premTeams[9], stats)
        results(premTeams[10], premTeams[16], stats)
        results(premTeams[13], premTeams[8], stats)
        results(premTeams[4], premTeams[17], stats)
        results(premTeams[0], premTeams[12], stats)
        results(premTeams[15], premTeams[7], stats)
        results(premTeams[11], premTeams[2], stats)

        if result == "W":
            myresults(premTeams[5], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[5], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[5], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 35\033[0;0m:")
        print(f"{premTeams[15]} vs {premTeams[11]}")
        print(f"{premTeams[12]} vs {premTeams[17]}")
        print(f"{premTeams[13]} vs {premTeams[5]}")
        print(f"{premTeams[14]} vs {premTeams[9]}")
        print(f"{premTeams[10]} vs {premTeams[1]}")
        print(f"{premTeams[18]} vs {premTeams[4]}")
        print(f"{premTeams[0]} vs {premTeams[2]}")
        print(f"{premTeams[8]} vs {premTeams[3]}")
        print(f"{premTeams[16]} vs {premTeams[6]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[7]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[15], premTeams[11], stats)
        results(premTeams[12], premTeams[17], stats)
        results(premTeams[13], premTeams[5], stats)
        results(premTeams[14], premTeams[9], stats)
        results(premTeams[10], premTeams[1], stats)
        results(premTeams[18], premTeams[4], stats)
        results(premTeams[0], premTeams[2], stats)
        results(premTeams[8], premTeams[3], stats)
        results(premTeams[16], premTeams[6], stats)

        if result == "W":
            myresults(premTeams[7], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[7], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[7], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 36\033[0;0m:")
        print(f"{premTeams[4]} vs {premTeams[13]}")
        print(f"{premTeams[3]} vs {premTeams[12]}")
        print(f"{premTeams[9]} vs {premTeams[15]}")
        print(f"{premTeams[5]} vs {premTeams[10]}")
        print(f"{premTeams[17]} vs {premTeams[16]}")
        print(f"{premTeams[2]} vs {premTeams[7]}")
        print(f"{premTeams[1]} vs {premTeams[0]}")
        print(f"{premTeams[11]} vs {premTeams[18]}")
        print(f"{premTeams[6]} vs {premTeams[14]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[8]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[4], premTeams[13], stats)
        results(premTeams[3], premTeams[12], stats)
        results(premTeams[9], premTeams[15], stats)
        results(premTeams[5], premTeams[10], stats)
        results(premTeams[17], premTeams[16], stats)
        results(premTeams[2], premTeams[7], stats)
        results(premTeams[1], premTeams[0], stats)
        results(premTeams[11], premTeams[18], stats)
        results(premTeams[6], premTeams[14], stats)

        if result == "W":
            myresults(myteam, premTeams[8], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[8], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[8], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 37\033[0;0m:")
        print(f"{premTeams[0]} vs {premTeams[9]}")
        print(f"{premTeams[7]} vs {premTeams[11]}")
        print(f"{premTeams[18]} vs {premTeams[3]}")
        print(f"{premTeams[14]} vs {premTeams[5]}")
        print(f"{premTeams[12]} vs {premTeams[2]}")
        print(f"{premTeams[15]} vs {premTeams[1]}")
        print(f"{premTeams[10]} vs {premTeams[6]}")
        print(f"{premTeams[8]} vs {premTeams[17]}")
        print(f"{premTeams[16]} vs {premTeams[4]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"{premTeams[13]} vs \033[1m{myteam}\033[0;0m")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[0], premTeams[9], stats)
        results(premTeams[7], premTeams[11], stats)
        results(premTeams[18], premTeams[3], stats)
        results(premTeams[14], premTeams[5], stats)
        results(premTeams[12], premTeams[2], stats)
        results(premTeams[15], premTeams[1], stats)
        results(premTeams[10], premTeams[6], stats)
        results(premTeams[8], premTeams[17], stats)
        results(premTeams[16], premTeams[4], stats)

        if result == "W":
            myresults(premTeams[13], myteam, "L", stats, myteam)
        elif result == "L":
            myresults(premTeams[13], myteam, "W", stats, myteam)
        else:
            myresults(premTeams[13], myteam, "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))


        print("\n\033[1mMatchday 38\033[0;0m:")
        print(f"{premTeams[17]} vs {premTeams[14]}")
        print(f"{premTeams[6]} vs {premTeams[18]}")
        print(f"{premTeams[1]} vs {premTeams[13]}")
        print(f"{premTeams[11]} vs {premTeams[0]}")
        print(f"{premTeams[2]} vs {premTeams[16]}")
        print(f"{premTeams[4]} vs {premTeams[10]}")
        print(f"{premTeams[3]} vs {premTeams[7]}")
        print(f"{premTeams[9]} vs {premTeams[8]}")
        print(f"{premTeams[5]} vs {premTeams[12]}")

        result = ""
        while result != "W" and result != "D" and result != "L":
            print(f"\033[1m{myteam}\033[0;0m vs {premTeams[15]}")
            result = input(f"\nDoes\033[1m {myteam} \033[0;0mwin (\033[1mW\033[0;0m), draw (\033[1mD\033[0;0m), or lose (\033[1mL\033[0;0m)? Enter just the letter (uppercase only): ")

        print("\n\033[1mResults\033[0;0m:")

        results(premTeams[17], premTeams[14], stats)
        results(premTeams[6], premTeams[18], stats)
        results(premTeams[1], premTeams[13], stats)
        results(premTeams[11], premTeams[0], stats)
        results(premTeams[2], premTeams[16], stats)
        results(premTeams[4], premTeams[10], stats)
        results(premTeams[3], premTeams[7], stats)
        results(premTeams[9], premTeams[8], stats)
        results(premTeams[5], premTeams[12], stats)

        if result == "W":
            myresults(myteam, premTeams[15], "W", stats, myteam)
        elif result == "L":
            myresults(myteam, premTeams[15], "L", stats, myteam)
        else:
            myresults(myteam, premTeams[15], "D", stats, myteam)

        stats = sorted(stats, key=lambda x: (x["Points"], x["GD"], x["GF"]), reverse=True)
        print("\n")
        print(tabulate(stats, headers="keys", tablefmt="rounded_grid", showindex=pos))

        relegated = is_bottom(myteam, stats)
        if relegated:
            break

        if is_top(myteam, stats):
            titles = titles + 1
            print(f"\n{myteam} has won the league!")

        ans = ""
        while ans.lower() != "y" and ans.lower() != "n":
            ans = input("\nWould you like to continue? (Y/N): ")
        if ans.lower() == "n":
            cont = False

        replaceTeams(stats)
        seasonsCompleted = seasonsCompleted + 1


    if relegated:
        print("\nCommiserations, your team is relegated from the Premier League and the simulation is over.")
    elif not cont and titles == 0:
        print("\nThe simulation is over.")
    elif not cont and titles == 1:
        print(f"\nThe simulation is over, {myteam} won the league once!")
    elif not cont and titles > 1:
        print(f"\nThe simulation is over, {myteam} won {titles} league titles!")
    elif cont and titles == 0:
        print("\nThe simulation is over, you made it to the end!")
    elif cont and titles == 1:
        print(f"\nThe simulation is over, you made it to the end, {myteam} won the league once!")
    elif cont and titles > 1:
        print(f"\nThe simulation is over, {myteam} won {titles} league titles!")


def initStats():
    global premTeamsStrength
    s = []
    for team in sorted(premTeamsStrength, key=lambda team: team["Team"]):
        x = dict(Team = team["Team"], Played = 0, W = 0, D = 0, L = 0, GF = 0, GA = 0, GD = 0, Points = 0)
        s.append(x)
    return s


def get_team():
    valid = False
    while not valid:
        team = input("\nPlease select a Premier League team to simulate (type it exactly as how you see it on the table): ").strip()
        valid = is_valid(team)
    return team


def is_valid(team):
    global premTeams
    if team in premTeams:
        return True
    else:
        return False


def is_bottom(team, stats):
    for i in range(len(stats)):
        if stats[i]["Team"] == team:
            pos = i + 1
    if pos >= 18:
        return True
    else:
        return False


def is_top(team, stats):
    for i in range(len(stats)):
        if stats[i]["Team"] == team:
            pos = i + 1
    if pos == 1:
        return True
    else:
        return False


def replaceTeams(stats):
    global premTeamsStrength
    global premTeams
    global champTeams

    down1 = stats[17]["Team"]
    down2 = stats[18]["Team"]
    down3 = stats[19]["Team"]

    print(f"\n{down1}, {down2}, and {down3} are relegated from the Premier League.\n")

    premTeams.remove(down1)
    premTeams.remove(down2)
    premTeams.remove(down3)

    for i in range(len(premTeamsStrength)):
        if premTeamsStrength[i]["Team"] == down1:
            down1 = premTeamsStrength[i]
        if premTeamsStrength[i]["Team"] == down2:
            down2 = premTeamsStrength[i]
        if premTeamsStrength[i]["Team"] == down3:
            down3 = premTeamsStrength[i]

    premTeamsStrength.remove(down1)
    premTeamsStrength.remove(down2)
    premTeamsStrength.remove(down3)

    promoted = []
    for i in range(3):
        up = random.choice(champTeams)
        champTeams.remove(up)
        promoted.append(up)
        premTeamsStrength.append(up)

    up1 = promoted[0]["Team"]
    up2 = promoted[1]["Team"]
    up3 = promoted[2]["Team"]

    print(f"{up1}, {up2}, and {up3} are promoted to the Premier League.")

    champTeams.append(down1)
    champTeams.append(down2)
    champTeams.append(down3)
    premTeams.append(up1)
    premTeams.append(up2)
    premTeams.append(up3)
    premTeams = sorted(premTeams)


def myresults(team1, team2, result, stats, teambold):
    if result == "W":
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["W"] = team["W"] + 1
                team["Points"] = team["Points"] + 3
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["L"] = team["L"] + 1
        scores(team1, team2, "W", stats, teambold)

    elif result == "D":
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["D"] = team["D"] + 1
                team["Points"] = team["Points"] + 1
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["D"] = team["D"] + 1
                team["Points"] = team["Points"] + 1
        scores(team1, team2, "D", stats, teambold)

    else:
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["L"] = team["L"] + 1
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["W"] = team["W"] + 1
                team["Points"] = team["Points"] + 3
        scores(team1, team2, "L", stats, teambold)


def results(team1, team2, stats):
    global premTeamsStrength

    for team in premTeamsStrength:
        if team["Team"] == team1:
            strength1 = team["strength"]
        if team["Team"] == team2:
            strength2 = team["strength"]

    point1 = random.randint(0, strength1)
    point2 = random.randint(0, strength2)

    if point1 > point2:
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["W"] = team["W"] + 1
                team["Points"] = team["Points"] + 3
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["L"] = team["L"] + 1
        scores(team1, team2, "W", stats)

    elif point1 < point2 and (point2 - point1) > 1:
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["L"] = team["L"] + 1
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["W"] = team["W"] + 1
                team["Points"] = team["Points"] + 3
        scores(team1, team2, "L", stats)

    else:
        for team in stats:
            if team["Team"] == team1:
                team["Played"] = team["Played"] + 1
                team["D"] = team["D"] + 1
                team["Points"] = team["Points"] + 1
            if team["Team"] == team2:
                team["Played"] = team["Played"] + 1
                team["D"] = team["D"] + 1
                team["Points"] = team["Points"] + 1
        scores(team1, team2, "D", stats)

def scores(team1, team2, result, stats, teambold = None):
    global premTeamsStrength

    for team in premTeamsStrength:
        if team["Team"] == team1:
            strength1 = team["strength"]
        if team["Team"] == team2:
            strength2 = team["strength"]

    strengthDiff = strength1 - strength2

    if result == "W":
        if strengthDiff >= 6:
            score1 = 0
            score2 = 0
            while score1 <= score2:
                score1 = random.randint(1,5)
                score2 = random.randint(0,1)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] + (score1 - score2)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] - (score1 - score2)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")

        elif strength1 <= 3:
            score1 = 0
            score2 = 0
            while score1 <= score2:
                score1 = random.randint(1,3)
                score2 = random.randint(0,2)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] + (score1 - score2)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] - (score1 - score2)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")

        else:
            score1 = 0
            score2 = 0
            while score1 <= score2:
                score1 = random.randint(1,3)
                score2 = random.randint(0,1)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] + (score1 - score2)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] - (score1 - score2)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")

    elif result == "D":
        if strengthDiff >= 6:
            score = random.randint(0,2)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score} - {score} {team2}")
                else:
                    print(f"{team1} {score} - {score} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score} - {score} {team2}")

        elif strengthDiff <= -6:
            score = random.randint(0,3)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score} - {score} {team2}")
                else:
                    print(f"{team1} {score} - {score} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score} - {score} {team2}")

        else:
            score = random.randint(0,2)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score
                    team["GA"] = team["GA"] + score

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score} - {score} {team2}")
                else:
                    print(f"{team1} {score} - {score} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score} - {score} {team2}")

    else:
        if strengthDiff >= 6:
            score1 = 0
            score2 = 0
            while score1 >= score2:
                score1 = random.randint(0,1)
                score2 = random.randint(1,2)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] - (score2 - score1)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] + (score2 - score1)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")

        elif strengthDiff <= -7:
            score1 = 0
            score2 = 0
            while score1 >= score2:
                score1 = random.randint(0,1)
                score2 = random.randint(1,4)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] - (score2 - score1)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] + (score2 - score1)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")

        else:
            score1 = 0
            score2 = 0
            while score1 >= score2:
                score1 = random.randint(0,2)
                score2 = random.randint(1,3)
            for team in stats:
                if team["Team"] == team1:
                    team["GF"] = team["GF"] + score1
                    team["GA"] = team["GA"] + score2
                    team["GD"] = team["GD"] - (score2 - score1)
                if team["Team"] == team2:
                    team["GF"] = team["GF"] + score2
                    team["GA"] = team["GA"] + score1
                    team["GD"] = team["GD"] + (score2 - score1)

            if teambold:
                if team1 == teambold:
                    print(f"\033[1m{team1}\033[0m {score1} - {score2} {team2}")
                else:
                    print(f"{team1} {score1} - {score2} \033[1m{team2}\033[0m")
            else:
                print(f"{team1} {score1} - {score2} {team2}")


if __name__ == "__main__":
    main()
