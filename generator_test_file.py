
from main_generator import generate_seed, draw_map, Map
"""Sample code for testing purposes"""
while True:
    ans = input("new map?")
    if ans == "y":
        x,y,c,ui = generate_seed()
        # #x,y,c,ui = 49, 42, 20, 45542
        # #x,y,c,ui = 39,11,6,76935
        SAMPLE_MAP_1 = Map(x,y,c,ui)
        SAMPLE_MAP_1.make_seed()
        SAMPLE_MAP_1.calc_start()
        SAMPLE_MAP_1.calc_length()
        SAMPLE_MAP_1.prefered_steps()
        SAMPLE_MAP_1.make_path()
        draw_map(SAMPLE_MAP_1)
        print(SAMPLE_MAP_1,'seed:', SAMPLE_MAP_1.seed, 'start:', SAMPLE_MAP_1.starting_x, SAMPLE_MAP_1.starting_y,'length:', SAMPLE_MAP_1.length,)
    elif ans.isalnum():
        x,y,c,ui = int(ans[:2]), int(ans[2:4]), int(ans[4]), int(ans[5:])
        SAMPLE_MAP_1 = Map(x,y,c,ui)
        SAMPLE_MAP_1.make_seed()
        print(SAMPLE_MAP_1.seed)
        SAMPLE_MAP_1.calc_start()
        SAMPLE_MAP_1.calc_length()
        SAMPLE_MAP_1.prefered_steps()
        SAMPLE_MAP_1.make_path()
        draw_map(SAMPLE_MAP_1)
        print(SAMPLE_MAP_1,'seed:', SAMPLE_MAP_1.seed, 'start:', SAMPLE_MAP_1.starting_x, SAMPLE_MAP_1.starting_y,'length:', SAMPLE_MAP_1.length,)
    else:
        quit()