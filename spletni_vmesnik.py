#first we play a little with the code
import bottle
from numpy import matrix
import kocke
import linear_congruetal_generator as lcg
from map_generator import Map
from map_generator import generate

displayed_map = Map(generate())
displayed_map.exception_library()
displayed_map.grid_matrix()


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('spletna_stran.tpl',
    standardni_set_kock = kocke.standard_set,
    current_map = Map((generate())),
    seed = displayed_map.seed,
    grid = displayed_map.matrix)
    # return """
    # <h1>Opravila</h1>
    # <h2>nekaj opravil</h2>
    # """

bottle.run(debug=True, reloader=True)