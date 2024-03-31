class Game:
    teams = []

    def __init__(self, term):
        self.term = term
        self.teams = []
        self.results = []

    def get_term(self):
        return self.term

    def add_team(self, team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams

    def has_teams(self):
        return len(self.teams) > 0