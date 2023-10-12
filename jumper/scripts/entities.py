class PhysicsEntity:
    def __init__(self, game, pos) -> None:
        self.game = game
        self.pos = list(pos)
        self.velocity = [0,0]

    def update(self, movement):
        self.pos[0] += (movement[1] - movement[0]) + self.velocity[0]