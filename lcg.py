#auxilary file
class Linear_congruetal_generator():
    @staticmethod   
    def lcg(modulus: int, a: int, c: int, seed: int): # Main generator, different miltupliers and increments used below
        while True:
            seed = (a * seed + c) % modulus
            yield seed
    
    @staticmethod   
    def num_rec_lcg(seed:int):
        return Linear_congruetal_generator.lcg(2 ** 32, 1664525,1013904223, seed)

    @staticmethod   
    def virt_pascal_lcg(seed:int):
        return Linear_congruetal_generator.lcg( 2 ** 32, 134775813, 1, seed)

    @staticmethod   
    def read(strg): #code copied from map.py
        x = int(strg[:2])
        y = int(strg[2:4])
        c1 = int(strg[4])
        unique_identifier = int(strg[5:])
        return (x,y,c1, unique_identifier)

    @staticmethod   
    def lcg_read(generated_number:int):
        generated_string = str(generated_number).zfill(10)
        return Linear_congruetal_generator.read(generated_string)