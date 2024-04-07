import typing

class Collideable:
    def __init__(self, pos:typing.Sequence[float], elasticity:float=1.0) -> None:
        self.pos = list(pos)
        self.elasticity = elasticity


class Border(Collideable):
    def __init__(self, pos: typing.Sequence[float], width:int, height:int, elasticity: float = 1.0) -> None:
        super().__init__(pos, elasticity)
        self.width = width
        self.height = height