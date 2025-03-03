from pyray import *

class Main:

    WINDOW_SIZE = (960,640)

    DEBUG = True

    def __init__(self) -> None:
        ## Raylib / OpenGL / Window Inits
        set_config_flags(ConfigFlags.FLAG_WINDOW_RESIZABLE)
        init_window( *self.WINDOW_SIZE, 'Window :)' )

        self.debug_font = load_font('/Users/732592/Library/Fonts/FiraCode-Retina.ttf')

        # Shader Inits

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
        ...
        
    def draw(self) -> None:
        ## Standard Drawing

        ## Debug Drawing
        if self.DEBUG:
            draw_text('hallo', 10, 10, 10, WHITE)

if __name__ == "__main__":
    Main().mainloop()