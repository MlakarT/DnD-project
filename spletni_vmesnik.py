#first we play a little with the code
import bottle
import model
from model import Control
#from model import VseSkupaj

with open('secret.txt') as tf:
    SECRET = tf.read()
vse_skupaj = Control.from_file('state.json')
#vse_skupaj = VseSkupaj.iz_datoteke('state.json')

def save_all():
    vse_skupaj.to_file('state.json')

@bottle.post('/user_login/')
def login():
    username = bottle.request.forms.getunicode("username")
    password = bottle.request.forms.getunicode("pass")
    user = vse_skupaj.find_user(username, password)
    if user:
        bottle.response.set_cookie("username", username, path='/', secret=SECRET)
        bottle.redirect('/')
    else:
        return "Incorrect username/password! Please try again."


def url_mape(seed:int):
    """Turn seed into map url of the form '/map/xxxxxxxxxx'"""
    return f"/map/{seed}"

def save_state():
    Control.to_file("state.json")

@bottle.get('/')
def osnovni_zaslon():
    bottle.redirect('/welcome_page/')

@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = 'static/'
  return bottle.static_file(ime_dat, root=pot)
  
@bottle.get('/welcome_page/')
def display_welcome():
    return bottle.template('views/welcome.html',
    )

@bottle.get('/map/<map_seed:int>')
def display_map(map_seed:int):
    if map_seed == 0:
        grid = [[]]
        return bottle.template('views/stran_mapa',
        grid = grid,
        )
    else:
        map = model.Map(str(map_seed))
        map.exception_library()
        map.grid_matrix()
        return bottle.template('views/stran_mapa',
        map_seed = map.seed, grid = map.matrix,
        )


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

@bottle.route('/roll-dice/', method='POST')
def roll_dice():
    dice = bottle.request.forms.getunicode("Die")
    bottle.redirect('/')

@bottle.error(404)
def error404(error):
    return "Whoops, looks like this page doesn't exist yet..."

bottle.run(debug=True, reloader=True)