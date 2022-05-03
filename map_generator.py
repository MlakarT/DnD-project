# Code for anything to do with the map, seed, seed generating, seed reading and map generating


import random as rd
import linear_congruetal_generator as lcg

# Generate seed
def generate():
    l = str(rd.randint(5,50))
    l = l.zfill(2)
    h = str(rd.randint(2,50))
    h = h.zfill(2)
    z = str(rd.randint(1,5))
    unique_identifier = str(rd.randint(0,99999))
    unique_identifier = unique_identifier.zfill(5)
    return l + h + z + unique_identifier

    #return str(rd.randint(0,50)) + str(rd.randint(0,50)) + str(rd.randint(0,5)) + str(rd.randint(0,99999))

def read(strg):
    l = int(strg[:2])
    h = int(strg[2:4])
    c = int(strg[4])
    unique_identifier = int(strg[5:])
    return (l,h,c, unique_identifier)

def sum_1(strg):
    sum = 0
    for i in strg[:3]:
        sum += int(i)
    if sum == 0:
        sum = 1
    return sum

def sum_2(strg):
    sum = 0
    for i in strg[3:]:
        sum += int(i)
    if sum == 0:
        sum = 1
    return sum

def start_and_end(coords:tuple):
    if coords[3] % 4 == 0: #na vrhu, na desni
        starting_x, starting_y = coords[0] // sum_1(str(coords[3])), 0
        ending_x, ending_y = coords[0], coords[1] // sum_2(str(coords[3]))
    elif coords[3] % 4 == 1: #na levi, na desni
        starting_x, starting_y = 0, coords[1] // sum_1(str(coords[3]))
        ending_x, ending_y = coords[0], coords[1] // sum_2(str(coords[3]))
    elif coords[3] % 4 == 2: #na vrhu, na podnu
        starting_x, starting_y = coords[0] // sum_1(str(coords[3])), 0
        ending_x, ending_y = coords[0] // sum_2(str(coords[3])),coords[1]
    elif coords[3] % 4 == 3: #na levi, na podnu
        starting_x, starting_y = 0, coords[1] // sum_1(str(coords[3]))
        ending_x, ending_y = coords[0] // sum_2(str(coords[3])), coords[1]
    return starting_x,starting_y,ending_x,ending_y


#test_lcg1 = lcg(2 ** 32,1664525,1013904223,int(generate())) #testing lcg type NUMERICAL RECIPIES at https://en.wikipedia.org/wiki/Numerical_Recipes
#test_lcg2 = lcg(2 ** 32, 134775813, 1, int(generate())) at https://en.wikipedia.org/wiki/Virtual_Pascal
#print([next(test_lcg1) for i in range(20)])
#print([next(test_lcg2) for i in range(20)])

class Map:
    def __init__(self,seed_str:str):
        self.seed = seed_str
        self.dimensions = read(self.seed)
        self.x, self.y, self.complexity, self.unique_identifier = self.dimensions[0],self.dimensions[1], self.dimensions[2], str(self.dimensions[3])
        self.length = self.x + self.y -1
        for i in self.unique_identifier:
            self.length += int(i)
        self. length = self.length * self.complexity
        self.lcg = lcg.num_rec_lcg(int(self.seed))
        self.lcg_list = [next(self.lcg) for _ in range(self.length)]
        self.start_x, self.start_y, self.end_x, self.end_y = start_and_end(self.dimensions)
        self.starting_coords = self.start_x, self.start_y
        self.finish_coords = self.end_x, self.end_y
        #print(self.seed, self.dimensions, self.length)


    def __repr__(self) -> str:
        return f"map object"

    def __str__(self) -> str:
        return f"{self.dimensions}"

    def exception_library(self):
        """Creates the positions of ones in the matrix"""
        self.exceptions = {}
        self.exceptions[self.starting_coords] = 1
        self.exceptions[self.finish_coords] = 1
        k = 2
        while k <= self.length:
            for num in self.lcg_list:
                tup = lcg.lcg_read(num)
                #print(tup)
                if tup[0] > self.x: #primerja prvo koordinato z sirino
                    if tup[1] > self.y: #primerja drugo koordinato z visino
                        self.exceptions[(tup[0] % self.x, tup[1] % self.y)] = 1
                    else:
                        self.exceptions[(tup[0] % self.x, tup[1])] = 1
                else:
                    if tup[1] > self.y:
                        self.exceptions[(tup[0], tup[1] % self.y)] = 1
                    else:
                        self.exceptions[(tup[0], tup[1])] = 1
                k+=1                  
        #this will change more, will be adjusted later
        #This fucker right here can fuck right the fuck off fuckin g piece of shit fuck shit
        #return self.exceptions

    def grid_matrix(self):
        """creates the grid matrix"""
        matrix = []
        for i in range(self.y):
            row = []
            for j in range(self.x):
                if (j,i) in self.exceptions:
                    row.append(self.exceptions[(j,i)])
                else:
                    row.append(0)
            print(row)
            matrix.append(row)
        self.matrix = matrix.copy()

#done

