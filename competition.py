class Competition:

    def __init__(self):
        self.teams = []
    

    def check_teams(self):
        print(self.teams)
    def check_all_scores(self):
        for team in self.teams:
            print(f'team {team.name} has {team.score} score(s)')

    def team_in_comp(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return True
        else: return False

    def add_team(self, new_team):
        self.teams.append(new_team)
        self.teams.sort(key=lambda team : team.score, reverse=True)
        print("you have successfully added a team.")
        print(f'there is {len(self.teams)} teams in the competition.')
    def remove_team(self, team_name):
        for team in self.teams:
            if team.name in team_name:
                self.teams.remove(team)
                print("you have successfully removed a team.")
                print(f'there is {len(self.teams)} teams in the competition.')
        else: print("team not found, invalid request")
    
    def add_player_to_team(self, team_name, new_player):
        for team in self.teams:
            if team.name == team_name:
                team.add_player(new_player)
                break
        else:
            print("team not found")
    def remove_player_from_team(self, team_name, player_name):
        for team in self.teams:
            if team.name == team_name:
                team.remove_player(player_name)
                break
        else:
            print("team not found")
    