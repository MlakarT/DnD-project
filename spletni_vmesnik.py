#first we play a little with the code
import bottle
import model
from model import Control
from model import generator
#from model import VseSkupaj

with open('secret.txt') as tf:
    SECRET = tf.read()
vse_skupaj = Control.from_file('user_example.json')
#vse_skupaj = VseSkupaj.iz_datoteke('state.json')

def save_all():
    vse_skupaj.to_file('user_example.json')

def url_request():
    return bottle.request.path
    
def seed_to_map(seed:str) -> generator.Map:
    w,h,c,ui = int(seed[0:2]), int(seed[2:4]), int(seed[4]), int(seed[5:])
    return generator.Map(w,h,c,ui)

def url_mape(seed:str):
    """Turn seed into map url of the form '/map/xxxxxxxxxx'"""
    return f"/map/{seed}"


@bottle.post('/user_login/')
def login():
    username = bottle.request.forms.getunicode("username")
    password = bottle.request.forms.getunicode("pass")
    if not password:
        password = None
    user = vse_skupaj.find_user(username, password)
    print(username, password,'user=', user)
    if user:
        bottle.response.set_cookie("username", username, path='/', secret=SECRET)
        bottle.redirect(URL)
    else:
        return "Incorrect username/password! Please try again."



# def save_state():
#     Control.to_file("state.json")

@bottle.get('/')
def osnovni_zaslon():
    bottle.redirect('/welcome_page/')

@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
  pot = 'static/'
  return bottle.static_file(ime_dat, root=pot)
  
@bottle.get('/welcome_page/')
def display_welcome():
    global URL
    URL = url_request()
    return bottle.template('views/welcome.html',)

@bottle.get('/map/<map_seed>')
def display_map(map_seed:str):
    global URL
    URL = url_request()
    if not map_seed:
        grid = [[]]
        return bottle.template('views/stran_mapa',
        grid = grid,
        )
    else:
        map = seed_to_map(map_seed)
        map.make_seed()
        map.calc_start()
        map.calc_length()
        map.prefered_steps()
        map.make_path()
        grid = generator.make_map(map)
        return bottle.template('views/stran_mapa',
        map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
        )

@bottle.post('/display-map/')
def display_requested():
    seed = bottle.request.forms.getunicode("seed")
    url = url_mape(seed)
    bottle.redirect(url)

@bottle.post('/display-random/')
def display_random():
    x,y,c,ui = generator.generate_seed()
    map = generator.Map(x,y,c,ui)
    map.make_seed()
    seed = map.seed
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