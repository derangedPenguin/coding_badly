import pygame, random as rand#, my_colors as colors

pygame.init()
options = ("mountain","ocean")
running = True
tile_width = 8
board_width, board_height = 20, 20
tiles = {x:{y:["undef",[i for i in options]] for y in range(board_height)} for x in range(board_width)}
screen = pygame.display.set_mode(((tile_width+1)*board_width,(tile_width+1)*board_height))

tile_colors = {"undef":(255,255,255),"mountain":(75,37,0),"ocean":(0,0,255)}

tiles[10][7][0] = "mountain"
tiles[15][3][0] = "ocean"

def rules(x,y,tile_type=None):
    if len(tiles[x][y][1]) == 1:
        tiles[x][y][0] = tiles[x][y][1][0]
    tile_type = tiles[x][y][0]
    add = {}
    rem = {}
    match tile_type:
        case "undef":
            return None
        case "mountain":
            add["mountain"] = [(0,-1),(0,1)]
            rem["mountain"] = [(-1,0),(1,0)]
        case "ocean":
            add["ocean"] = [(-1,0),(1,0)]
    for key in add:
        for tuple in add[key]:
            tiles[x+tuple[0]][y+tuple[1]][1].append(key)
    for key in rem:
        for tuple in rem[key]:
            try:
                tiles[x+tuple[0]][y+tuple[1]][1].remove(key)
            except:
                pass

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                for x in range(board_width):
                    for y in range(board_height):
                        tiles[x][y][0] = rand.choice(tiles[x][y][1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(tiles[pos[0]//(board_width+1)][pos[1]//(board_height+1)][1])
            tiles[pos[0]//(board_width+1)][pos[1]//(board_height+1)][0] = rand.choice(tiles[pos[0]//(board_width+1)][pos[1]//(board_height+1)][1])

    screen.fill((0,0,0))

    for x in range(board_width):
        for y in range(board_height):
            pygame.draw.rect(screen,tile_colors[tiles[x][y][0]],(x*(tile_width+1)+1,y*(tile_width+1)+1,tile_width,tile_width,))
            rules(x,y)

    pygame.display.flip()

pygame.quit()