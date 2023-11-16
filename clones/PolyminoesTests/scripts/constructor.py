INT_DIR_TO_OFFSET = {
    0:(0,-1),#up
    1:(1,0),#right
    2:(0,1),#down
    3:(-1,0)#left
}

class custom_gen:
    def __init__(self, min=0, max=4) -> None:
        self.min = min #incclusive
        self.max = max #non-inclusive

        self.next = min+1
        self.current = min
        self.last = max
    
    def grab(self):
        print(self.current)
        result = self.current
        self.increment()
        return result
    
    def increment(self):
        self.next = (self.next+1) % self.max
        self.current = (self.next+1) % self.max
        self.last = (self.next+1) % self.max

def gen_minos(n):
    tiles = []
    gens = []
    crnt_tile = []
    crnt_offset = [0,0]
    count = n

    for i in range(100000):
        if len(crnt_tile) == n:
            #store current tile
            tiles.append(crnt_tile)
            #check if all gens at 4 (finished state)
            finished = True
            for gen in gens:
                if gen.current != 4:
                    finished = False
                    break
            #return mino list if finished
            if finished: return tiles

            #remove most recent pieces to cycle through next position
            for i in range(len(gens)-1,-1,-1):
                if gens[i].current == 4:
                    del gens[i]
                    del crnt_tile[i]

            move = INT_DIR_TO_OFFSET[gens[-1].grab()]
            crnt_offset = (crnt_offset[0]+move[0], crnt_offset[1]+move[1])
        else:
            crnt_tile.append(crnt_offset)
            gens.append(custom_gen(0,4))
            move = INT_DIR_TO_OFFSET[gens[-1].grab()]
            crnt_offset = (crnt_offset[0]+move[0], crnt_offset[1]+move[1])
    return tiles
