OFFSETS = ((0,-1),(1,0),(0,1),(1,0)) #^>v<

class cell:
    def __init__(self, pos=(0,0), open_dirs={1,2,3,4}) -> None:
        self.pos = pos
        self.open_dirs = open_dirs

class Mino:
    def __init__(self, cells=[cell()]) -> None:
        self.cells = cells
        self.cell_offsets = {cell.pos for cell in self.cells}
        self.active_cell = cells[-1]

        self.open_cells = self.active_cell.open_dirs - self.cell_offsets

def gen_minos(layers):
    print('starting proccess...')
    minos = [Mino()]

    for i in range(layers):
        for j, mino in enumerate(minos):
            #print(len(minos))
            offsets = [OFFSETS[offset] for offset in mino.active_cell.open_dirs]
            for new_offset in offsets:
                new_pos = (new_offset[0]+mino.active_cell.pos[0], new_offset[1]+mino.active_cell.pos[1])
                print(new_pos)
                minos.append(Mino(cells=mino.cells + [cell(new_pos)]))
    print('complete!')
    print([mino.cells for mino in minos])

gen_minos(3)