import config
from config import Player
import random


queue = []

def print_queue(queue):
    print(["{}".format(pl.mmr) for pl in queue])


def populate_queue(num_players):
    queue = []
    for i in range(num_players):
        p = Player(name="p{}".format(i), mmr=random.randint(config.MMR_MIN, config.MMR_MAX))
        queue = queue_player(p)

    print_queue(queue)


def queue_player(player):
    def binary_insert(q, mmr):
        min_ind = 0
        max_ind = len(q) - 1
        while True:
            i = (min_ind + max_ind) // 2
            if max_ind < min_ind:
                return i+1
            if q[i].mmr < mmr:
                min_ind = i + 1
            elif q[i].mmr > mmr:
                max_ind = i - 1
            else:
                return i+1

    queue_index = binary_insert(queue, player.mmr)
    queue.insert(queue_index, player)

    return queue


populate_queue(16)

player = Player("New Player", 600)

queue_player(player)

print_queue(queue)







