class Record:
    def __init__(self, WinTeam, LoseTeam, GameNo, Round):
        self.WinTeam = WinTeam
        self.LoseTeam = LoseTeam
        self.GameNo = GameNo
        self.Round = Round

    def get_win_team(self):
        return self.WinTeam

    def get_lose_team(self):
        return self.LoseTeam

    def get_game_no(self):
        return self.GameNo

    def get_round(self):
        return self.Round