class Player:
    def __init__(self, name, credit, age, team, No):
        self.name = name
        self.credit = credit
        self.age = age
        self.No = No
        self.team = team

        if credit < 1000:
            self.level = "Edge"
        elif 1000 <= credit < 1500:
            self.level = "Common"
        elif 1500 <= credit < 2000:
            self.level = "Core"
        else:
            self.level = "All Star"

    def set_credit(self, credit):
        self.credit = credit
        if credit < 1000:
            self.level = "Edge"
        elif 1000 <= credit < 1500:
            self.level = "Common"
        elif 1500 <= credit < 2000:
            self.level = "Core"
        else:
            self.level = "All Star"

    def get_credit(self):
        return self.credit

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_no(self):
        return self.No