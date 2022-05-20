#first we play a little with the code
import bottle
from bottle import static_file
from bottle import error
import model
from model import Map

displayed_map = Map(model.generate())
displayed_map.exception_library()
displayed_map.grid_matrix()
width, heigth = displayed_map.x, displayed_map.y



@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('spletna_stran.html',
    standardni_set_kock = model.STANDARD_SET,
    current_map = displayed_map,
    seed = displayed_map.seed,
    x = width, y = heigth,
    grid = displayed_map.matrix)

# @bottle.route('/static/spletna_stran_css.css')
# def server_static(datoteka):
#     return static_file(datoteka, root='spletna_stran_css.css')

@bottle.error(404)
def error404(error):
    return "Whoops, looks like this page doesn't exist yet..."

bottle.run(debug=True, reloader=True)