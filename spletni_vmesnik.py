#first we play a little with the code
import bottle
import model
from model import generate
from model import Map

def url_mape(seed:int):
    """Turn seed into map url of the form '/map/xxxxxxxxxx'"""
    return f"/map/{seed}"

@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = 'static/'
  return bottle.static_file(ime_dat, root=pot)

@bottle.get('/')
def osnovni_zaslon():
    bottle.redirect('/welcome_page/')

@bottle.get('/welcome_page/')
def display_welcome():
    return bottle.template('views\welcome.html')

@bottle.get('/map/<map_seed:int>')
def display_map(map_seed:int):
    if map_seed == 0:
        grid = [[]]
        return bottle.template('views/stran_mapa', grid = grid)
    else:
        map = Map(str(map_seed))
        map.exception_library()
        map.grid_matrix()
        return bottle.template('views/stran_mapa', map_seed = map.seed, grid = map.matrix)

@bottle.post('/display-map/')
def display_requested():
    seed = bottle.request.forms.getunicode("seed")
    url = url_mape(seed)
    bottle.redirect(url)

@bottle.post('/display-random/')
def display_random():
    seed = int(model.generate())
    url = url_mape(seed)
    bottle.redirect(url)

@bottle.error(404)
def error404(error):
    return "Whoops, looks like this page doesn't exist yet..."

bottle.run(debug=True, reloader=True)