import random as rd

class Dice():
    """Creates n-sided die."""
    def __init__(self,dice:int):
        self.sides = dice
        self.all_rolls = []

    def __repr__(self) -> str:
        return f'Dice({self.sides})'

    def __str__(self) -> str:
        return f'd{self.sides}'
    
    @staticmethod
    def roll(sides:int, num_of_rolls:int =1):
        """Rolls @sides sided dice @num_of_rolls times."""
        i = 1
        rolls = []
        while i <= num_of_rolls:
            rolled = rd.randint(1,sides)
            rolls.append(rolled)
            i += 1
        return rolls
    
    def __call__(self, num_of_rolls:int =1):
        rolls = Dice.roll(self.sides, num_of_rolls)
        self.all_rolls.extend(rolls)
        return rolls
    
    def roll_history(self):
        return self.all_rolls if self.all_rolls else 'No history'

STANDARD_SET = {'d100' : Dice(100),
        'd20': Dice(20),
        'd12': Dice(12),
        'd10': Dice(10),
        'd8': Dice(8),
        'd6': Dice(6),
        'd4': Dice(4),
        'd3': Dice(3),
        'd2': Dice(2)}