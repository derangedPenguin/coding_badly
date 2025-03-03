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

    SCREEN_SIZE = (960,640)

    MARGIN = 2

    DEBUG = True

    def __init__(self) -> None:
        ## Raylib / OpenGL / Window Inits
        set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
        init_window( *self.SCREEN_SIZE, 'Window :)' )

        # Shader Inits
        self.flow_shader = load_shader('shaders/flow.vert', 'shaders/flow.frag')

        self.last_time = get_time()
        self.delta_time=0

        ## Functional Inits
        self.point_spacing = 10

        self.mouse_pos = ffi.new('struct Vector2 *', (0,0))
    
    def __getitem__(self, key):
        return self.grid[key]
    def __setitem__(self, key, value):
        self.grid[key] = value

    def mainloop(self) -> None:

        while not window_should_close():
            self.delta_time = get_time() - self.last_time
            self.last_time = get_time()
            self.update()
            begin_drawing()
            self.draw() 
            end_drawing()

            rl_check_errors()

        close_window()
    
    def update(self) -> None:
        set_shader_value(self.flow_shader, get_shader_location(self.flow_shader, 'time'),
                          ffi.new('float *', get_time()), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
        set_shader_value(self.flow_shader, get_shader_location(self.flow_shader, 'costime'),
                          ffi.new('float *', np.cos(get_time())), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
        set_shader_value(self.flow_shader, get_shader_location(self.flow_shader, 'sintime'),
                          ffi.new('float *', np.sin(get_time())), ShaderUniformDataType.SHADER_UNIFORM_FLOAT)
        
        self.mouse_pos.x = get_mouse_x()
        self.mouse_pos.y = get_mouse_y()
        set_shader_value(self.flow_shader, get_shader_location(self.flow_shader, 'mouse_pos'),
                          self.mouse_pos, ShaderUniformDataType.SHADER_UNIFORM_VEC2)
        
    def draw(self) -> None:
        ## Flow Field drawing
        begin_shader_mode(self.flow_shader)
        # Uniforms
        

        # setup
        clear_background(BLACK)#(20,90,110,255))

        sw = get_screen_width()
        sh = get_screen_height()

        # drawing
        for x in range(-self.MARGIN, sw//self.point_spacing + self.MARGIN):
            for y in range(-self.MARGIN, sh//self.point_spacing + self.MARGIN):
                sx, sy = x * self.point_spacing - sw//2, y * self.point_spacing - sh//2
                draw_line( sx, sy, sx, sy+20, GREEN) # if this actually gets drawn green something is probably wrong
        
        end_shader_mode()

        if self.DEBUG:
            draw_text(f'FPS: {1/self.delta_time:.2f}', 10, 10, 14, GREEN)

        

if __name__ == "__main__":
    Main().mainloop()