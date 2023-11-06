class Polymino:
    def __init__(self, source_dict: dict | None = None) -> None:
        if source_dict is None:
            self.n = 0
            self.offsets = ()
        else:
            self.n = source_dict['n']
            self.offsets = source_dict['offsets']
    
    def __getitem__(self, item):
        return self.offsets[item]

    def to_dict(self):
        return {'n':self.n,'offsets':self.offsets}

class Polymino_Set:
    def __init__(self, shapes = []) -> None:
        self.shapes = shapes
        self.polys = []

    def create_polyminoes(self):
        for shape in self.shapes:
            self.polys.append(Polymino(shape))

    def n_minoes(self, n) -> None:
        #init shapes dict with stick
        shapes = {'stick':[(0,i) for i in range(n)]}
        
        for i in range(n):
            shapes[f'turned-{i}'] = self.turn(n,i)
        
        self.shapes = shapes.copy()


    def turn(self, n, turn_point):
        vals = []
        for i in range(turn_point):
            vals.append((0,i))
        for i in range(n - turn_point):
            vals.append((turn_point, i))
        return vals