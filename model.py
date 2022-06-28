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
import main_generator as generator
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

    def __str__(self):
        return f'{self.username}'

    def add_rolls(self, rolled:list):
        self.rolls.extend(rolled)

    def to_dict(self):
        return {
            "username" : self.username,
            "password" : self.password,
            "nickname" : self.display_name,
            "current_displayed_map" : self.displayed_map,
            "maps" : self.maps,
            "roll_history" : self.rolls
        }

    @classmethod
    def from_dict(cls,slovar:dict):
        return cls(
            username=slovar["username"],
            password=slovar["password"],
            display_name=slovar["nickname"],
            displayed_map=slovar["current_displayed_map"],
            maps=slovar["maps"],
            rolls=slovar["roll_history"]
        )

@dataclass
class Control:
    #temporarily copying this to see what i can do with it
    #because im kinda stuck
    users: List[User]

    def __repr__(self) -> str:
        return f'users={[user for user in self.users]}'

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
            users=[User.from_dict(d) for d in slovar['users']]
        )

    def to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.to_dict(), file, ensure_ascii=False, indent=4)

    @classmethod
    def from_file(cls, filename):
        with open(filename) as file:
            return cls.from_dict(json.load(file))

mlakar = User(
                "mlakar",
                "pass",
                "mlakar", 
                1208112345, 
                [],
                [1,1,1,1]
            )
test = Control(
        users=[
            User(
                "mlakar",
                "pass",
                "mlakar", 
                1208112345, 
                [],
                [1,1,1,1]
            )
        ]
    )

# @dataclass
# class Uporabnik:
#     uporabnisko_ime: str
#     zasifrirano_geslo: str

#     @staticmethod
#     def zasifriraj_geslo(geslo_v_cistopisu):
#         return "XXX" + geslo_v_cistopisu[::-1] + "XXX"

#     def ima_geslo(self, geslo_v_cistopisu):
#         return self.zasifriraj_geslo(geslo_v_cistopisu) == self.zasifrirano_geslo
    
#     def nastavi_novo_geslo(self, geslo_v_cistopisu):
#         self.zasifrirano_geslo = self.zasifriraj_geslo(geslo_v_cistopisu)

#     def v_slovar(self):
#         return {
#             "uporabnisko_ime": self.uporabnisko_ime,
#             "zasifrirano_geslo": self.zasifrirano_geslo,
#         }

#     @classmethod
#     def iz_slovarja(cls, slovar):
#         return cls(
#             uporabnisko_ime=slovar["uporabnisko_ime"],
#             zasifrirano_geslo=slovar["zasifrirano_geslo"],
#         )


# @dataclass
# class VseSkupaj:
#     uporabniki: List[Uporabnik]

#     def poisci_uporabnika(self, uporabnisko_ime, geslo_v_cistopisu=None):
#         for uporabnik in self.uporabniki:
#             if uporabnik.uporabnisko_ime == uporabnisko_ime:
#                 if geslo_v_cistopisu is None or uporabnik.ima_geslo(geslo_v_cistopisu):
#                     return uporabnik

#     def v_slovar(self):
#         return {
#             "uporabniki": [uporabnik.v_slovar() for uporabnik in self.uporabniki],
#         }

#     @classmethod
#     def iz_slovarja(cls, slovar):
#         return cls(
#             uporabniki=[Uporabnik.iz_slovarja(sl) for sl in slovar.keys()]
#         )

#     def v_datoteko(self, ime_datoteke):
#         with open(ime_datoteke, "w") as f:
#             json.dump(self.v_slovar(), f, ensure_ascii=False, indent=4)

#     @classmethod
#     def iz_datoteke(cls, ime_datoteke):
#         with open(ime_datoteke) as f:
#             return cls.iz_slovarja(json.load(f))