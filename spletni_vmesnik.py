#first we play a little with the code
import bottle
from dice import Dice
import model
from model import Control
from model import generator
from model import User

with open('secret.txt') as tf:
    SECRET = tf.read()
vse_skupaj = Control.from_file('state.json')

#tole je potrebn da lahko na welcome pagu nastimas zadn met
global LAST_ROLLED
LAST_ROLLED = None

def save_all():
    vse_skupaj.to_file('state.json')

def url_request():
    return bottle.request.path


def current_user():
    username = bottle.request.get_cookie('username', secret=SECRET)
    # if username:
    #     return Control.from_file('state.json')
    if username is None:
        return 'no_user'
    return username

def seed_to_map(seed:str) -> generator.Map:
    w,h,c,ui = int(seed[0:2]), int(seed[2:4]), int(seed[4]), int(seed[5:])
    return generator.Map(w,h,c,ui)

def url_mape(seed:str):
    """Turn seed into map url of the form '/map/xxxxxxxxxx'"""
    return f"/map/{seed}"



@bottle.post('/user-login/')
def login():
    username = bottle.request.forms.getunicode("username")
    password = bottle.request.forms.getunicode("pass")
    if not password:
        password = None
    user = vse_skupaj.find_user(username, password)
    print(username, password,'user=', user)
    if user:
        bottle.response.set_cookie("username", username, httponly=True, path='/', secret=SECRET,)
        bottle.redirect(URL)
    else:
        return "Incorrect username/password! Please try again."

@bottle.post('/user-logout/')
def logout():
    bottle.response.delete_cookie('username', path='/', secret=SECRET)
    if URL == '/saved_maps/' or URL == '/display_rolls/':
        bottle.redirect('/')
    bottle.redirect(URL)

@bottle.post('/user-register/')
def new_user_register():
    username = bottle.request.forms.getunicode("new_username")
    password = bottle.request.forms.getunicode("new_pass")
    password2 = bottle.request.forms.getunicode("confirmpass")
    if username in [user.username for user in vse_skupaj.users]:
        return 'Account already exists or username is already taken. Please try again.'
    if password == password2:
        new_user = User.from_dict({
            'username' : username,
            'password' : password,
            'maps' : [],
            'roll_history' : {}
        })
        vse_skupaj.users.append(new_user)
        save_all()
        bottle.response.set_cookie("username", new_user.username, httponly=True, path='/', secret=SECRET,)
        bottle.redirect(URL)
    else:
        return "Passwords do not match! Please try again."

# def save_state():
#     Control.to_file("state.json")

@bottle.get('/')
def osnovni_zaslon():
    global LAST_ROLLED
    LAST_ROLLED = None
    bottle.redirect('/welcome_page/')

@bottle.get('/static/<ime_dat:path>')
def server_static(ime_dat):
    #tale ne nastaula sprot globalnga urlja
    pot = 'static/'
    return bottle.static_file(ime_dat, root=pot)
  
@bottle.get('/welcome_page/')
def display_welcome():
    global URL
    URL = url_request()
    user = vse_skupaj.active_user(current_user())
    if not user:
        if not LAST_ROLLED:
            return bottle.template('views/welcome.html', user='no_user',)
        return bottle.template('views/welcome.html', user='no_user', roll=LAST_ROLLED[0],)
    else:
        if not LAST_ROLLED:
            return bottle.template('views/welcome.html',user=user.username,)
    return bottle.template('views/welcome.html',user=user.username, roll=LAST_ROLLED[0],)

@bottle.get('/map/<map_seed>')
def display_map(map_seed:str):
    global URL
    URL = url_request()
    user = vse_skupaj.active_user(current_user())
    map = seed_to_map(map_seed)
    map.make_seed()
    map.calc_start()
    map.calc_length()
    map.prefered_steps()
    map.make_path()
    grid = generator.make_map(map)
    if not user:
        if not LAST_ROLLED:
            return bottle.template('views/stran_mapa',
            map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
            user='no_user',)
        return bottle.template('views/stran_mapa',
        map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
        user='no_user',
        roll=LAST_ROLLED[0],
        )
    else:
        if not LAST_ROLLED:
            return bottle.template('views/stran_mapa',
            map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
            user=user.username,
            )
        return bottle.template('views/stran_mapa',
        map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
        user=user.username,
        roll=LAST_ROLLED[0],
        )
        # if not map_seed:
        #     grid = [[]]
        #     return bottle.template('views/stran_mapa',
        #     grid = grid,
        #     user='no_user',
        #     roll=LAST_ROLLED[0],
        #     )
        # else:
        #     map = seed_to_map(map_seed)
        #     map.make_seed()
        #     map.calc_start()
        #     map.calc_length()
        #     map.prefered_steps()
        #     map.make_path()
        #     grid = generator.make_map(map)
        #     return bottle.template('views/stran_mapa',
        #     map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
        #     user='no_user',
        #     roll=LAST_ROLLED[0],
        #     )
        # else:
        #     if not map_seed:
        #         grid = [[]]
        #         return bottle.template('views/stran_mapa',
        #         grid = grid,
        #         user=user.username,
        #         roll=LAST_ROLLED[0],
        #         )
        #     else:
        #         map = seed_to_map(map_seed)
        #         map.make_seed()
        #         map.calc_start()
        #         map.calc_length()
        #         map.prefered_steps()
        #         map.make_path()
        #         grid = generator.make_map(map)
        #         return bottle.template('views/stran_mapa',
        #         map_seed = map.seed, grid = grid, x=map.width, y= map.height, c=map.complexity,
        #         user=user.username,
        #         roll=LAST_ROLLED[0],
        #         )

@bottle.get('/saved_maps/')
def display_saves():
    global URL
    URL = url_request()
    user = vse_skupaj.active_user(current_user())
    return bottle.template('views/saves', user=user.username, maps=user.maps,)

@bottle.get('/display_rolls/')
def display_roll_history():
    global URL
    URL = url_request()
    user = vse_skupaj.active_user(current_user())
    return bottle.template('views/history', user=user.username, rolls = user.rolls,)
    

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

@bottle.post('/save-map/')
def save_displayed():
    user = vse_skupaj.active_user(current_user())
    current_map = URL.split('/')[2]
    if current_map in user.maps:
        bottle.redirect(URL)
    user.maps.append(current_map)
    save_all()
    bottle.redirect(URL)

@bottle.post('/roll/')
def roll_dice():
    user = vse_skupaj.active_user(current_user())
    sides = int(bottle.request.forms.getunicode("dice"))
    d = Dice(sides)
    global LAST_ROLLED
    LAST_ROLLED = d() #makes the actual roll
    if not user:
        bottle.redirect(URL)
    user.add_rolls(d,LAST_ROLLED)
    save_all()
    bottle.redirect(URL)

@bottle.error(404)
def error404(error):
    return "Whoops, looks like this page doesn't exist yet..."

bottle.run(debug=True, reloader=True)