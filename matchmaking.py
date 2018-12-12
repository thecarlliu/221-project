import config
from config import Player, Queue, Match
import random


def populate_queue(queue, num_players):
    queue.master_queue = []
    for i in range(num_players):
        p = Player(name="P{}".format(i), mmr=random.randint(config.MMR_MIN, config.MMR_MAX))
        queue.master_queue = queue_player(queue, p)


def queue_player(queue, player):
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

    queue_index = binary_insert(queue.master_queue, player.mmr)
    queue.master_queue.insert(queue_index, player)
    queue.time_queue.append(player)

    return queue.master_queue


def make_match(queue, player):

    matched_players = [player]

    k = queue.master_queue.index(player)
    i = 1
    while True:

        mmr_good_1 = True
        if k - i >= 0:
            p1 = queue.master_queue[k-i]
            mmr_good_1 = abs(p1.mmr - player.mmr) <= config.MMMR_QUEUE_THRESH
            if mmr_good_1 and not p1.being_matched:
                p1.being_matched = True
                matched_players.append(p1)
        else:
            break

        if len(matched_players) == config.TEAM_SIZE*2:
            break

        mmr_good_2 = True
        if k + i < len(queue):
            p2 = queue.master_queue[k + i]
            mmr_good_2 = abs(p2.mmr - player.mmr) <= config.MMMR_QUEUE_THRESH
            if mmr_good_2 and not p2.being_matched:
                p2.being_matched = True
                matched_players.append(p2)
        else:
            break

        if len(matched_players) == config.TEAM_SIZE*2 or (not mmr_good_1 and not mmr_good_2):
            break

        i += 1

    if len(matched_players) == config.TEAM_SIZE*2:
        for pl in matched_players:
            queue.master_queue.remove(pl)
            queue.time_queue.remove(pl)
        return Match(matched_players)
    else:
        for p in queue.master_queue:  # Bad loop
            p.being_matched = False
        return None


def search_matchmaking(queue):
    for p in queue.time_queue:

        m = make_match(queue, p)
        if m is not None:
            return m

    return None


def make_all_matches(queue):
    matches = []
    m = search_matchmaking(queue)
    while m is not None:
        matches.append(m)
        m = search_matchmaking(queue)

    # Enable tracking time in queue
    # for p in queue.time_queue:
    #     p.time_in_queue += 1

    return matches


# Runs simulation of matchmaking process with random player joins
def simulate_matchmaking(time=10000):

    match_counter = 0
    player_counter = 10

    make_matches_every = 10

    qo = Queue()

    populate_queue(qo, player_counter)

    for i in range(time):
        if random.randint(0, 10) == 0:
            mmr = random.randint(config.MMR_MIN, config.MMR_MAX)
            player = Player("P{}".format(i), mmr)
            queue_player(qo, player)
            player_counter += 1
            #print("New Player added to queue: {}".format(player))

        if i % make_matches_every == 0:
            ms = make_all_matches(qo)
            if len(ms) != 0:
                for m in ms:
                    match_counter += 1
                    print("\n{}".format(m))

    print("\n\nMatchmaking Simulations Complete")
    print("Players Queued: {}".format(player_counter))
    print("Matches Created: {}".format(match_counter))

    print(qo.time_queue)

simulate_matchmaking()





