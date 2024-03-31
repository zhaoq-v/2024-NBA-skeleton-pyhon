from Player import Player


class Players:
    def __init__(self, players):
        self.Players = players

    def initial_add_player(self, name, credit, age, team, No):
        for player in self.Players:
            if player == Player(name, credit, age, team, No):
                return
        self.Players.append(Player(name, credit, age, team, No))

    def get_player_list(self):
        return self.Players

    def add_player(self, name, credit, age, team, No):
        self.Players.append(Player(name, credit, age, team, No))

    def delete_player(self, del_player):
        self.Players.remove(del_player)
