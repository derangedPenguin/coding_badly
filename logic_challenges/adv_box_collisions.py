def box_collisions():
    rect_count = int(input('Enter number of rects: '))
    rect_width = int(input('Enter width of rects: '))
    rect_height = int(input('Enter height of rects: '))

    rect_coords = []
    for rect in range(rect_count):
        rect_coords.append([int(input(f'Enter x-coord of rect {rect}: ')), int(input(f'Enter y-coord of rect {rect}: '))])
    
    
    for rect in rect_coords:
        rect_coords[rect_coords.index(rect)] = {'left':rect[0], 'right':rect[0] + rect_width, 'bottom':rect[1], 'top':rect[1] + rect_height}

    collisons = []
    for i, rect in enumerate(rect_coords):
        other_rects = rect_coords.copy().remove(rect)
        for rect2 in other_rects:
            if rect2['right'] > rect['left'] > rect2['left']:
                if rect2['top'] > rect['bottom'] > rect2['bottom']:
                    collision = (())
                    collisons.append(())
    
box_collisions()

        