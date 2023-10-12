import json
import math

from scripts.entities import Attacker

BASE_PATH = 'data/levels/'

class EntityPath:
    def __init__(self, game) -> None:
        self.game = game
        self.points = ()
        self.round_num = -1
        self.rounds = {}

        self.active_rnd = {}
    
    def import_level(self, path):
        with open(BASE_PATH + path, 'r') as file:
            level = json.loads(file.read())
            self.points = level['attacker_path']
            round_builder = level["rounds"].copy()

        # {1:{20:[red, red, red, blue], 40:[blue, blue]}, 2:{...}}
        self.rounds = {}
        for round_num, round in enumerate(round_builder):
            self.rounds[round_num] = {}
            for start_time in round:
                for a_type in round[start_time].keys():
                    for a_num in range(round[start_time][a_type]['count']):
                        try:
                            self.rounds[round_num][int(start_time) + (round[start_time][a_type]['spacing'] * a_num)].append(int(a_type))
                        except:
                            self.rounds[round_num][int(start_time) + (round[start_time][a_type]['spacing'] * a_num)] = [int(a_type), ]

    def export_level(self, path):
        with open(BASE_PATH + path, 'w') as file:
            file.write(json.dumps({'rounds':self.rounds, 'attacker_path': self.points}, indent=4))

    def nearest_point(self, pos):
        dists = {}
        for point in self.points:
            dists[(math.sqrt((pos[0] - point[0]) ** 2 + (pos[1] - point[1]) ** 2))] = point
        try:
            return dists[min(dists.keys())]
        except:
            return pos
    
    def next_round(self):
        #print(json.dumps(self.rounds, indent = 4))
        self.game.active_rounds.append(self.rounds[self.round_num % len(self.rounds)].copy())
        self.game.active_rounds[-1]['active'] = True
        self.round_num += 1
    
    def update(self):
        for a_type in (x := self.active_rnd.get(self.game.rnd_timer, {})):
            self.game.rnd_attackers.append(Attacker(self.game, int(a_type), self))