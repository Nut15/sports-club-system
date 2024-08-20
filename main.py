from teams import Team
from player import Player
from competition import Competition

def all_options():
    print("\nyou can input:\n 1 for adding/removing a team\n 2 for checking all teams in competition\n 3 for checking the score board\n 4 for checking players on a team\n 5 for adding/removing players into a team\n or enter -1 to exit")
    user_choice = int(input("your choice: "))
    return user_choice

def check_players(team_choice):
    for team in competition.teams:
        if team.name == team_choice:
            print(team.check_players())
            break
    else:
        print("team not found")


competition = Competition()

user_choice = all_options()
while user_choice != -1:
    if user_choice == 1:
        add_or_remove = int(input("would you like to add (1) or remove (2) a team?: "))
        if add_or_remove == 1:
            team = Team(input("team name: "), int(input("team score: ")))
            competition.add_team(team)
        elif add_or_remove == 2:
            team_name = input("team name: ")
            competition.remove_team(team_name)
        else: print("invalid request")
    elif user_choice == 2:
        competition.check_teams()
    elif user_choice == 3:
        competition.check_all_scores()
    elif user_choice == 4:
        team_choice = input("which team?: ")
        check_players(team_choice)
    elif user_choice == 5:
        competition.check_teams()
        _continue = 2
        while _continue != -1:
            if _continue == 2 or 1:
                if _continue == 2:
                    team_in_comp = False
                    team_name = input("which team?: ")
                    team_in_comp = competition.team_in_comp(team_name)
                if _continue == 1 or team_in_comp == True:
                    add_or_remove = int(input("would you like to add (1) or remove (2) a player?: "))
                    if add_or_remove == 1:
                        new_player = Player(input("player name: "))
                        competition.add_player_to_team(team_name,new_player)
                    elif add_or_remove == 2:
                        player_name = input("player name: ")
                        competition.remove_player_from_team(team_name,player_name)
                    else: print("invalid request")
                elif team_in_comp == False:
                    print("team doesn't exist, invalid request")
            else: print("invalid request")
            _continue = int(input("would you like to make changes to this current team (1) or another team (2) or exit to main menu (-1)?: "))
    else: print("invalid request")
    user_choice = all_options()