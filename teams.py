class Team:
    player_limit = 23

    def __init__(self, name, score):
        self.players = []
        self.name = name
        self.score = score
    def __repr__(self):
        return f'[name={self.name}, players={self.players}, score={self.score}]'
    def __str__(self):
        return f'team {self.name} has {len(self.players)} players'
    

    def add_player(self, player):
        if len(self.players) < self.player_limit:
            self.players.append(player)
            print(f'you have successfully added player {player.name} into {self.name} team. Now {self.name} team has {len(self.players)} player(s).')
        else: print("player limit reached, invalid request")
    def remove_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)
                print(f'you have successfully removed player {player_name} into {self.name} team. Now {self.name} team has {len(self.players)} player(s).')
                break
        else: print("player doesn't exist, invalid request")
    
    def check_players(self):
        print(self.players)
    