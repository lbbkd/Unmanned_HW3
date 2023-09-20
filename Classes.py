class Obstacle():
    def __init__(self, x:float, y:float, radius:float=0.5) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        
class Node():
    def __init__(self,x:float,y:float,parent_index:float,cost:float, Acost:float):
        self.x = x
        self.y = y
        self.parent_index = parent_index
        self.cost = cost
        self.Acost = Acost
