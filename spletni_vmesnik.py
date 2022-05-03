#first we play a little with the code
import bottle
import kocke

@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('spletna_stran.tpl',
    standardni_set_kock = kocke.standard_set)
    # return """
    # <h1>Opravila</h1>
    # <h2>nekaj opravil</h2>
    # """

bottle.run(debug=True, reloader=True)