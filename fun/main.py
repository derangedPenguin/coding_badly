import pygame as pg

class Config:
    SCREEN_SIZE = (960, 640)
    FPS = 60

class Theme:
    MENU_BACKGROUND = pg.Color(40,40,40)
    GAME_BACKGROUND = pg.Color(40,40,40)

class Main:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(Config.SCREEN_SIZE, flags=0, vsync=True)
        self.clock = pg.time.Clock()

        self.currentLoop = self.update_menu

    def mainloop(self):
        while True:
            if pg.event.get(pg.QUIT):
                pg.quit()
                exit(0)
            
            self.currentLoop()

            pg.display.update()
            self.clock.tick(60)
    
    def update_menu(self):
        for event in pg.event.get(pg.KEYDOWN):
            if event.key == pg.K_SPACE:
                self.currentLoop = self.update_game

        self.screen.fill(Theme.MENU_BACKGROUND)
    
    def update_game(self):
        for event in pg.event.get(pg.KEYDOWN):
            if event.key == pg.K_SPACE:
                self.currentLoop = self.update_game

        self.screen.fill(Theme.MENU_BACKGROUND)


if __name__ == "__main__":
    Main().mainloop()
