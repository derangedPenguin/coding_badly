import numpy as np

def figure_circle_snap(p1, p2):
    goal_dist = self.radius + oth_p.radius # how far apart should they be
                snap_distance = (goal_dist - np.sqrt(sq_dist)) / 2 # how far does each need to move to not intersect
                angle = np.tan( abs(self.y - oth_p.y) / abs(self.x - oth_p.x) ) # angle of the line between their centerpoints

                shift = np.array((np.cos(angle), np.sin(angle))) # x and y shift to apply to each circle

                self.pos += shift * snap_distance
                oth_p.pos -= shift * snap_distance