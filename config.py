
TEAM_SIZE = 5
MMR_MIN = 0
MMR_MAX = 1000
MMMR_QUEUE_THRESH = 50


class Player(object):

    def __init__(self, name, mmr):
        self.name = name
        self.mmr = mmr
        self.role = ""
        self.being_matched = False

    def __repr__(self):
        return "{} ({})".format(self.name, self.mmr)


    def set_role(self, role):
        self.role = role


class Queue(object):

    def __init__(self):
        self.master_queue = []
        self.time_queue = []


    def __repr__(self):
        return str(self.master_queue)


    def __len__(self):
        return len(self.master_queue)


class Match(object):

    def __init__(self, players):
        self.team_size = len(players) // 2
        self.team_1 = players[:self.team_size]
        self.team_2 = players[self.team_size:]

    def __repr__(self):
        return "New {} Player Match\nTeam 1: {}\nTeam 2: {}".format(self.team_size*2, self.team_1, self.team_2)
