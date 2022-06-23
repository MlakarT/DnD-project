import random as rd
from dataclasses import dataclass
from math import sqrt
from lcg import Linear_congruetal_generator as lcg


STEPS = {
    0: (1,0),
    2: (-1,0),
    1: (0,1),
    3: (0,-1),
}
#for testing purposes
def generate_seed(c:int = None) -> tuple:
    x = rd.randint(3,50)
    y = rd.randint(2,50)
    if c:
        comp = c
    else:
        comp = rd.randint(1,9)
    ui = rd.randint(0,99999)
    return x,y,comp,ui


def possible_steps(location:tuple):
    return [(location[0]+a,location[1]+b) for (a,b) in STEPS.values()]

@dataclass
class Map:
    width: int
    height: int
    complexity: int
    unique_id: int

    def make_seed(self) -> str:
        self.seed = str(self.width) + str(self.height) + str(self.complexity) + str(self.unique_id)
        return self.seed

    def calc_start(self) -> None:
        num = sum(int(i) for i in str(self.unique_id))
        if self.unique_id % 2 == 0:
            self.starting_x, self.starting_y = int(self.width * sqrt(self.complexity / num)), 0
        elif self.unique_id % 2 == 1:
            self.starting_x, self.starting_y = 0, int(self.width * sqrt(self.complexity / num))

    def calc_length(self) -> int:
        num = sum(int(i) for i in str(self.unique_id))
        self.length = int((self.width + self.height + num) * sqrt(self.complexity))
    
    def prefered_steps(self) -> list:
        cifre = lcg.num_rec_lcg(int(self.seed))
        sez_cifr = [next(cifre) for _ in range(self.length)]
        koraki = [(cifra % int(self.unique_id)) % 4 for cifra in sez_cifr]
        return koraki

    def check_step(self,location,path) -> bool:
        """Checks if the location is available: checks all neighbours of the desired position."""
        x,y = location
        if not (0 <= x < self.width and 0 <= y < self.height):
            return False
        sosedje = set((x+a,y+b) for (a,b) in STEPS.values())
        if len(set(path).intersection(sosedje))>1:
            return False
        return True        

    def make_path(self) -> dict|None:
        self.path = {}
        koraki = self.prefered_steps().copy()
        x,y = (self.starting_x,self.starting_y)
        self.path[x,y] = 2
        for i in range(self.length-1):
            #tukej podas mozne korake
            pos_steps = possible_steps((x,y))
            k = koraki[i] #kle pogledas ce gres loh najprj unga k je v korakih #this feels evil
            while pos_steps:
                step = pos_steps[k]
                if self.check_step(step,self.path):
                #za vsak korak preveris ce je izvedljiv
                    x,y = step
                    self.path[x,y] = 1
                    break
                    #vzames prvega
                else:
                    pos_steps.remove(step)
                    k = 0
                    #ce ni ok ga vrzes vn probas dalje tapruga od unh k so ostal
        self.path[x,y] = 3
        return self.path
            

def draw_map(map:Map) -> None:
    width, height, path = map.width, map.height, map.path
    matrix = []
    for j in range(height):
        row = []
        for i in range(width):
            if (i,j) in path:
                row.append(path[(i,j)])
            else:
                row.append(0)
        matrix.append(row)
    for row in matrix:
        print(row)

"""Sample code for testing purposes"""
x,y,c,ui = generate_seed()
#x,y,c,ui = 49, 42, 20, 45542
#x,y,c,ui = 12,8,1,12345
SAMPLE_MAP_1 = Map(x,y,c,ui)
SAMPLE_MAP_1.make_seed()
SAMPLE_MAP_1.calc_start()
SAMPLE_MAP_1.calc_length()
SAMPLE_MAP_1.prefered_steps()
SAMPLE_MAP_1.make_path()
draw_map(SAMPLE_MAP_1)
print(SAMPLE_MAP_1,'seed:', SAMPLE_MAP_1.seed, 'start:', SAMPLE_MAP_1.starting_x, SAMPLE_MAP_1.starting_y,'length:', SAMPLE_MAP_1.length, 'path:', SAMPLE_MAP_1.path)