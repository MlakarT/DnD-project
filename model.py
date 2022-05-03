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


#leave this as is for now, will either define other stuff when it comes up but for now i have 3 seperate model files, one for each thing
import map_generator
from map_generator import map
import linear_congruetal_generator as lcg
import kocke


