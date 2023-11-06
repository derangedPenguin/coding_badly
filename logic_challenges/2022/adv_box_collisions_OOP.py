class Rect:
    """holds basic data and methods to handle rect collision"""
    def __init__(self, width, height, num) -> None:
        self.left = int(input(f'Enter rect {num} x: '))
        self.right = self.left + width
        self.bottom = int(input(f'Enter rect {num} y: '))
        self.top = self.bottom + height
    
    def collide(self, rect2):
        """checks for a collision between self and argument rect object"""
        if rect2.left < self.left < rect2.right or rect2.left < self.right < rect2.right:
            if rect2.bottom < self.bottom < rect2.top or rect2.bottom < self.top < rect2.top:
                return True
            
    def collide_rects(self, rects):
        """runs Rect collide function against an argument list of rect objects"""
        collisions = []
        for rect in rects:
            if self.collide(rect):
                collisions.append((self, rect))
        return collisions

#input data of rects
rect_count = int(input('Enter number of rects: '))
width = int(input('Enter rect widths: '))
height = int (input('Enter height of rects: '))

#constructs a list containing each rect object based on input
rects = []
for i in range(rect_count):
    rects.append(Rect(width, height, i))

#runs collision methods over the rects and handles my unhelpful logic bits
collisions = []
for i in range(len(rects)):
    rect = rects.pop(0)
    collisions += rect.collide_rects(rects)
    print(rect.left, rect.right, rect.bottom, rect.top)
print(len(collisions))
