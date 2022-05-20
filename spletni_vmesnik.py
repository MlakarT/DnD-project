#first we play a little with the code
import bottle
import model
from model import generate
from model import Map

displayed_map = Map(model.generate())
displayed_map.exception_library()
displayed_map.grid_matrix()
width, heigth = displayed_map.x, displayed_map.y

@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = 'static/'
  return bottle.static_file(ime_dat, root=pot)

@bottle.get('/')
def osnovni_zaslon():
    bottle.redirect('/welcome_page/')

@bottle.get('/welcome_page/')
def display_map():
    return bottle.template('views\welcome.html')
    
@bottle.get('/map/<map_seed:int>')
def display_map(map_seed:int):
    return bottle.template('views\stran_mapa', grid=[[1,1],[1,1]])
    # standardni_set_kock = model.STANDARD_SET,
    # current_map = displayed_map,
    # seed = displayed_map.seed,
    # x = width, y = heigth,
    # grid = displayed_map.matrix)

# @bottle.route('/static/spletna_stran_css.css')
# def server_static(datoteka):
#     return static_file(datoteka, root='spletna_stran_css.css')

# @bottle.get('/map/<map_seed:int>')
# def zaslon_mapa(map_seed):
#     return bottle.template('views\stran_mapa.html')

@bottle.error(404)
def error404(error):
    return "Whoops, looks like this page doesn't exist yet..."

bottle.run(debug=True, reloader=True)