from pyray import *

import numpy as np

class Main:

    SCREEN_SIZE = (960,640)

    MARGIN = 2

    DEBUG = True

    def __init__(self) -> None:
        ## Raylib / OpenGL / Window Inits
        set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
        init_window( *self.SCREEN_SIZE, 'Window :)' )

        self.debug_font = load_font('/Users/732592/Library/Fonts/FiraCode-Retina.ttf')

        # Shader Inits
        self.basic_shader = load_shader('shaders/basic.vert', 'shaders/basic.frag')

        self.last_time = get_time()
        self.delta_time=0

        ## Functional Inits
        self.mouse_pos = ffi.new('struct Vector2 *', (0,0))

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
        # self.mouse_pos.x = get_mouse_x()
        # self.mouse_pos.y = get_mouse_y()
        # set_shader_value(self.basic_shader, get_shader_location(self.basic_shader, 'mouse_pos'),
        #                   self.mouse_pos, ShaderUniformDataType.SHADER_UNIFORM_VEC2)
        ...
        
    def draw(self) -> None:
        ## Flow Field drawing
        begin_shader_mode(self.basic_shader)

        # setup
        clear_background(BLACK)#(20,90,110,255))

        sw = get_screen_width()
        sh = get_screen_height()

        # drawing
        draw_triangle((0,0),(-sw//2, sh//2+30),(sw//2, sh//2), WHITE)
        
        # cleanup
        end_shader_mode()

        # no shader drawing (debug)
        if self.DEBUG:
            draw_text_ex(self.debug_font, f'FPS: {1/self.delta_time:.2f}', (10, 10), 16, 0.1, GREEN)


if __name__ == "__main__":
    Main().mainloop()