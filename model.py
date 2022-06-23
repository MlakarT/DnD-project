#osrednja backend koda za randomizer
#avtor: Timotej Mlakar, MAT-1, Fakulteta za matematiko in fiziko, Univerza v Ljubljani
#Te komentarje sem ze miljonkrat napisal, tako da jih samo kopiram:
#       This is the beginning of the D&D map project. Author: Timotej Mlakar
#       This code will be based first on a current map im working on, later to be expanded (like use input) and submitted as school work.
#       If i choose to add anything, more at https://github.com/MlakarT/DnD-project
#       For any issues or questions please contact me at timo.mlakar@gmail.com or at my university email tm2012@student.uni-lj.si
#       The program will use Pygame for drawing purposes
#Github page bo isti, samo repozitorij bo nov, ta v trenutnem linku bo bodisi preimenovan in arhiviran ali pa odstranjen.
#Z gitom se pocaka do naslednjega tedna, ko bomo imeli le tega na predavanju
# https://www.delftstack.com/howto/python/read-pdf-in-python/ za kasnejso implementacijo branja character sheetov
#more info on this at https://en.wikipedia.org/wiki/Linear_congruential_generator
#aswell as for the two generators used specifically:
#Numerical Recipies generator: https://en.wikipedia.org/wiki/Numerical_Recipes
#Virtual Pascal generator: https://en.wikipedia.org/wiki/Virtual_Pascal
#for the purposes of the matrix generation, the Numerical Recipies generator was used. 
import json
from dataclasses import dataclass
from typing import List
import test_generator
import lcg
import dice


#Gonna probably split the code into three files for easier manipulation
#model file remains for studd like user interface, saving writing data, etc etc
class Game:
    pass #To be implemented later
@dataclass
class User:
    username: str
    password: str
    display_name: str
    #user_character: None
    #user_role: None
    displayed_map: int
    maps: list
    rolls: list

    def add_rolls(self, rolled:list):
        self.rolls.extend(rolled)

    def to_dict(self):
        return {
            "username" : self.username,
            "password" : self.password,
            "nickname" : self.display_name,
            "current_displayed_map" : self.displayed_map,
            "saved_maps" : self.maps,
            "roll_history" : self.rolls
        }

    @classmethod
    def from_dict(cls,slovar):
        return cls(
            username = slovar["username"],
            password = slovar["password"],
            display_name = slovar["nickname"],
            displayed_map = slovar["current_displayed_map"],
            maps = slovar["saved_maps"],
            rolls = slovar["roll_history"]
        )

@dataclass
class Control:
    #temporarily copying this to see what i can do with it
    #because im kinda stuck
    users: List[User]

    def find_user(self, username, password=None):
        for user in self.users:
            if user.username == username:
                if password is None or user.password:
                    return user
    
    def to_dict(self):
        return {
            "users" : [user.to_dict() for user in self.users]
        }

    @classmethod
    def from_dict(cls, slovar):
        return cls(
            users=[User.from_dict(d) for d in slovar["users"]]
        )

    def to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    @classmethod
    def from_file(cls, filename):
        with open(filename) as file:
            return cls.from_dict(json.load(file))

test_user = User("mlakar", "pass", "mlakar", 1208112345, [],[1,1,1,1])
test_control = Control(users=[test_user])