import turtle

class CustomTurtle(turtle.Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

    def hidebrush_goto(self, pos):
        self.penup()
        self.goto(pos)
        self.pendown()
    
    def infinity(self, radius):
        for i in range(1000):
            self.forward(1)
            self.left(i)

brush = CustomTurtle(visible=False)

def draw_orbital(energy_level, type):
    match type:
        case 's':
            brush.hidebrush_goto((0,-energy_level*10))
            brush.circle(energy_level*10)
        case 'p':
            brush.hidebrush_goto((0,0))
            brush.infinity


for level in range(1,100):
    draw_orbital(level, 's')


screen = turtle.Screen()
screen.mainloop()