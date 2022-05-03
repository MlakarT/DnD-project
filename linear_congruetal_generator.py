#stuff to do with the linear congruetal generator and pseudo-randomness
#more info on this at https://en.wikipedia.org/wiki/Linear_congruential_generator
#aswell as for the two generators used specifically:
#Numerical Recipies generator: https://en.wikipedia.org/wiki/Numerical_Recipes
#Virtual Pascal generator: https://en.wikipedia.org/wiki/Virtual_Pascal
#for the purposes of the matrix generation, the Numerical Recipies generator was used. 


def lcg(modulus: int, a: int, c: int, seed: int): # Main generator, different miltupliers and increments used below
    while True:
        seed = (a * seed + c) % modulus
        yield seed

def num_rec_lcg(seed:int):
    return lcg(2 ** 32, 1664525,1013904223, seed)

def virt_pascal_lcg(seed:int):
    return lcg( 2 ** 32, 134775813, 1, seed)

def read(strg): #code copied from map.py
    l = int(strg[:2])
    h = int(strg[2:4])
    c = int(strg[4])
    unique_identifier = int(strg[5:])
    return (l,h,c, unique_identifier)

def lcg_read(generated_number:int):
    generated_string = str(generated_number).zfill(10)
    return read(generated_string)