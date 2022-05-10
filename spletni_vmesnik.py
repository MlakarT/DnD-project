#first we play a little with the code
import bottle
import model
from model import Map

displayed_map = Map(model.generate())
displayed_map.exception_library()
displayed_map.grid_matrix()


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('spletna_stran.tpl',
    standardni_set_kock = model.STANDARDNI_SET,
    current_map = Map((model.generate())),
    seed = displayed_map.seed,
    grid = displayed_map.matrix)
    # return """
    # <h1>Opravila</h1>
    # <h2>nekaj opravil</h2>
    # """

bottle.run(debug=True, reloader=True)