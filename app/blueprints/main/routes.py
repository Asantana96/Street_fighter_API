from flask import render_template
from . import bp 

@bp.route('/')
def home():
    return render_template('index.jinja',title ='Home')

@bp.route('/characters')
def characters():
    char = ['Ken','Ryu','Chun-Li','Zangief','Blanka','E.Honda','Balrog','Sagat','Dee Jay','Guile','Vega','Akuma','T.Hawk','Dhalsim','R.Mika']

    return render_template('characters.jinja',title='Characters',characters = char)

@bp.route('/games')
def games():
    GAMES=['Street Fighter','Street Fighter ll Turbo','Street Fighter lll Alpha','Street Fighter lV','Street Fight V','Street Fighter 6']

    return render_template('games.jinja',title ='Games',Games=GAMES)