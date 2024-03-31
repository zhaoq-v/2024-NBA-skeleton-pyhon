from Players import Players


class Team:
    def __init__(self, name):
        self.name = name
        self.players = Players([])

        if name == "Suns":
            self.players.initial_add_player("Devin Booker", 2500.0, 26, "Suns", 1)
            self.players.initial_add_player("Chris Paul", 1500.0, 37, "Suns", 3)
            self.players.initial_add_player("Deandre Ayton", 2000.0, 24, "Suns", 22)
            self.players.initial_add_player("Kevin Durant", 3000.0, 34, "Suns", 35)
            self.players.initial_add_player("Terrence Ross", 1000.0, 32, "Suns", 8)

        if name == "Bulls":
            self.players.initial_add_player("Andre Drummond", 1500.0, 29, "Bulls", 3)
            self.players.initial_add_player("Zach LaVine", 3000.0, 28, "Bulls", 8)
            self.players.initial_add_player("Dalen Terry", 900.0, 20, "Bulls", 25)
            self.players.initial_add_player("Terry Taylor", 1000.0, 23, "Bulls", 32)
            self.players.initial_add_player("Carlik Jones", 800.0, 25, "Bulls", 22)

        if name == "Hawks":
            self.players.initial_add_player("Trae Young", 2200.0, 24, "Hawks", 11)
            self.players.initial_add_player("John Collins", 2000.0, 25, "Hawks", 20)
            self.players.initial_add_player("Aaron Holiday", 800.0, 26, "Hawks", 3)
            self.players.initial_add_player("Jalen Johnson", 1000.0, 21, "Hawks", 1)
            self.players.initial_add_player("Trent Forrest", 1200.0, 24, "Hawks", 2)

        if name == "Nets":
            self.players.initial_add_player("Mikal Bridges", 2400.0, 26, "Nets", 1)
            self.players.initial_add_player("Ben Simmons", 2000.0, 26, "Nets", 10)
            self.players.initial_add_player("Patty Mills", 900.0, 34, "Nets", 8)
            self.players.initial_add_player("Joe Harris", 1200.0, 31, "Nets", 12)
            self.players.initial_add_player("Seth Curry", 1900.0, 32, "Nets", 30)

    def get_name(self):
        return self.name

    def get_players(self):
        return self.players

    def set_players(self, players):
        self.players = Players(players)

    def __str__(self):
        return ""

    def average_credit(self):
        team_players = self.get_players().get_player_list()
        player_count = 0
        avg_credit = 0
        for player in team_players:
            player_count += 1
            avg_credit += player.get_credit()
        avg_credit = avg_credit / player_count if player_count > 0 else 0
        return avg_credit
