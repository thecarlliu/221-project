
TEAM_SIZE = 5
MMR_MIN = 0
MMR_MAX = 1000

class Player(object):

    def __init__(self, name, mmr):
        self.name = name
        self.mmr = mmr
        self.role = ""

    def set_role(self, role):
        self.role = role