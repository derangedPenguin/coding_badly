from scripts.tilemap import Tilemap

SURROUNDING_OFFSETS = {
            (-1,-1),(0,-1),(1,-1),
            (-1,0),       (1,0),
            (-1,1),(0,1),(1,1),
        }

class Updator:
    def __init__(self, board: Tilemap) -> None:
        self.board = board
    
    def mono_tile_update(self):
        """to be overwritten and called in mono_board_update"""
        pass
    
    def mono_board_update(self, tile_updator):
        check_tiles = set()
        for live_tile in self.board.tiles:
            live_tile = live_tile.split(';')
            coord = (int(live_tile[0]),int(live_tile[1]))
            near = {(coord[0]+off_x, coord[1]+off_y) for off_x,off_y in SURROUNDING_OFFSETS}
            check_tiles.add(coord)
            check_tiles = check_tiles.union(near)


        updated_board = self.board.copy(include_tiles=False)
        for tile in check_tiles:
            if tile_updator(tile):
                updated_board.add_tile(tile)
            else:
                updated_board.rem_tile(tile)
        return updated_board

class ConwayUpdator(Updator):
    def __init__(self, board: Tilemap) -> None:
        super().__init__(board)
    
    def mono_tile_update(self, tile: str):
        """update one tile based on ruleset"""
        #try to keep performance in this and anything it calls good, its called a lot
        #coord = [int(i) for i in tile.split(';')]
        other_tiles = self.board.get_surrounding(tile).values()
        crnt_state = self.board[f'{tile[0]};{tile[1]}']
        surround_sum = sum(other_tiles)
        #print(other_tiles, surround_sum)
        if surround_sum == 3 or (surround_sum == 2 and crnt_state == 1):
            result = True
        else:
            result = False
        return result

    def mono_board_update(self):
        return super().mono_board_update(self.mono_tile_update)