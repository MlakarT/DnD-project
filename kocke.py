# Code for anything to do with the dice

import random as rd
import time

def random_numbers(num:int, secs:float=1, interval:float=0.1):
    """Shows random numbers in the range of the dice rolled, every @interval seconds for @secs seconds."""
    time_end = time.time() + secs
    while time.time() < time_end:
        print(rd.randint(1,num))
        time.sleep(interval)

def roll(sides:int,num_off_rolls:int =1):
    """Rolls @sides sided dice @num_of_rolls times, with @time_between_rolls seconds passing between each roll. Prints out the numbers."""
    i = 1
    rolls = []
    while i <= num_off_rolls:
        rolled = rd.randint(1,sides)
        rolls.append(rolled)
        i += 1
    return rolls

def simulate_roll(sides:int,rolls:list,time_between_rolls:int=0.5):
    i = 1
    while i <= len(rolls):
        print('Rolling...')
        random_numbers(sides,0.5)
        rolled = rolls[i-1]
        print('Rolled:', rolled)
        if i != len(rolls):
            time.sleep(time_between_rolls)
        i += 1


class Dice():
    """Prejme število in ustvari n-strano kocko."""
    def __init__(self,dice:int):
        self.sides = dice
        self.all_rolls = []

    def __repr__(self) -> str:
        return f'Dice({self.sides})'

    def __str__(self) -> str:
        return f'd{self.sides}'

    def __call__(self,num_of_rolls:int =1, time_between_rolls:int=0.5):
        """Call na kocko vrže kocko @num_of_rolls krat, vmes počaka @time_between_rolls sekund."""
        rolls = roll(self.sides, num_of_rolls)
        self.all_rolls.extend(rolls)
        return simulate_roll(self.sides, rolls, time_between_rolls)

    def fast_roll(self,num_of_rolls:int=1):
        """Naredi podobno, le da samo naprinta vržene vrednosti."""
        i = 1
        rolls = []
        while i <= num_of_rolls:
            rolls.append(rd.randint(1,self.sides))
            i += 1
        self.all_rolls.extend(rolls)
        for i in rolls:
            print('Rolled:', i)

    def roll_history(self):
        return self.all_rolls if self.all_rolls else 'No history'

standard_set = {'d100' : Dice(100),
        'd20': Dice(20),
        'd12': Dice(12),
        'd10': Dice(10),
        'd8': Dice(8),
        'd6': Dice(6),
        'd4': Dice(4),
        'd3': Dice(3),
        'd2': Dice(2)}