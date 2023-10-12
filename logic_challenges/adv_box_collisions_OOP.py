class Rect:
    def __init__(self, width, height, num) -> None:
        self.left = int(input(f'Enter rect {num} x: '))
        self.right = self.left + width
        self.bottom = int(input(f'Enter rect {num} y: '))
        self.top = self.bottom + height
    
    def collide(self, rect2):
        if rect2.left < self.left < rect2.right or rect2.left < self.right < rect2.right:
            if rect2.bottom < self.bottom < rect2.top or rect2.bottom < self.top < rect2.top:
                return True
            
    def collide_rects(self, rects):
        collisions = []
        for rect in rects:
            if self.collide(rect):
                collisions.append((self, rect))
        return collisions


rect_count = int(input('Enter number of rects: '))
width = int(input('Enter rect widths: '))
height = int (input('Enter height of rects: '))

rects = []
for i in range(rect_count):
    rects.append(Rect(width, height, i))

collisions = []
for i in range(len(rects)):
    rect = rects.pop(0)
    collisions += rect.collide_rects(rects)
    print(rect.left, rect.right, rect.bottom, rect.top)
print(len(collisions))
