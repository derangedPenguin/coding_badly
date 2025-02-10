from pyray import *

import numpy as np

a = np.array((0.66, 0.56, 0.68))
b = np.array((0.71, 0.43, 0.72))
c = np.array((0.52, 0.8, 0.52))
d = np.array((-0.43, 0.39, 0.083))

def palatte(val):
    global a, b, c, d
    color = a + b * np.cos(6.28318*(c*val*d))
    return ((color[0]+1)*88, (color[1]+1)*88, (color[2]+1)*88)
def idk(val):
    global a, b, c, d
    color = a + b * np.cos(6.28318*(c*val*d))
    return sum(color)/len(color)/255

class Main:

    SCREEN_SIZE = (640,640)

    MARGIN = 1

    def __init__(self) -> None:
        ## Raylib / OpenGL / Window Inits
        set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
        init_window( *self.SCREEN_SIZE, 'Window :)' )

        # self.shiny_shader = load_shader('shaders/basic.vert', 'shaders/shiny.frag')
        self.flow_shader = load_shader('shaders/basic.vert', 'shaders/basic.frag')
        set_shader_value(self.flow_shader, 2, ffi.new('float []', self.SCREEN_SIZE), ShaderUniformDataType.SHADER_UNIFORM_IVEC2)


        self.last_time = get_time()
        self.delta_time=0

        
        ## Function Inits
        self.spacing = 10

        self.grid = [
            [[np.pi*2/3,10,(255,255,255,255)] 
             for __ in range(int(get_screen_width()*-(self.MARGIN-1)), int(get_screen_width()*self.MARGIN), self.spacing)
             ] for _ in range(int(get_screen_height()*-(self.MARGIN-1)), int(get_screen_height()*self.MARGIN), self.spacing)
            ]
    
    def __getitem__(self, key):
        return self.grid[key]
    def __setitem__(self, key, value):
        self.grid[key] = value

    def mainLoop(self) -> None:
        while not window_should_close():
            self.delta_time = get_time() - self.last_time
            self.last_time = get_time()
            self.update()
            self.draw() 

        close_window()
    
    def update(self) -> None:
        for x, row in enumerate(self.grid):
            for y, data in enumerate(row):
                dist = np.sqrt((x-len(self.grid)/2)**2+(y-len(self.grid[0])/2)**2)
                data[1] = ((dist-10)/2)+15
                self[x][y][0] = dist * np.pi * (get_time()/10) # direction
                self[x][y][1] = idk(dist+get_time()*20) * 20000 # magnitude
                # self[x][y][2] = (*(int(i) for i in palatte(dist+get_time()*2)),255) # color
        
    def draw(self) -> None:
        begin_drawing()

        ## Flow line testing
        begin_shader_mode(self.flow_shader)
        clear_background(BLACK)
        # draw_line(-get_screen_width()//2,get_screen_height()//2, -get_screen_width()//2 - 20, get_screen_height()//2, WHITE)
        # draw_line(get_screen_width()//2, get_screen_height()//2, get_screen_width()//2,0, WHITE)
        draw_triangle( (get_screen_width()//2, get_screen_height()//2), (get_screen_width()//2,0), (get_screen_width()//2,2), WHITE )
        # draw_rectangle(0,0,get_screen_width(), get_screen_height(), WHITE)
        # draw_line(2,2,2,0,WHITE)
        # draw_rectangle(0,0,get_screen_width(),get_screen_height(),GREEN)


        ## Shiny frag testing
        # begin_shader_mode(self.shiny_shader)

        # set_shader_value(self.shiny_shader, 0, ffi.new('float *', get_time()), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)

        # draw_rectangle(-get_screen_width()//2,get_screen_height()//2,get_screen_width(), -get_screen_height(), WHITE)

        ## Full flow field drawing
        # draw_triangle((0,0), (500,0),(250,250),WHITE)
        
        # clear_background( (0,125,125) )

        # for y_, row in enumerate(self.grid):
        #         for x_, data in enumerate(row):
        #             point_angle, magnitude, color = data
        #             x, y = x_*self.spacing, y_*self.spacing
        #             draw_line(int(x), int(y),
        #                       int(x+magnitude*np.cos(point_angle)), int(y+magnitude*np.sin(point_angle)),
        #                       color)
        
        end_shader_mode()
        end_drawing()

if __name__ == "__main__":
    Main().mainLoop()