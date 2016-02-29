import datetime
import os
DEV = os.environ['SERVER_SOFTWARE'].startswith('Development')

config = {

    # webapp2 sessions
    'webapp2_extras.sessions': {'secret_key': '_SDFIOUSOIFUIUODUSFO_'},

    # webapp2 authentication
    'webapp2_extras.auth': {'user_model': 'users',
                            'cookie_name': 'session_name'},

    # jinja2 templates
    'webapp2_extras.jinja2': {'template_path': ['templates']},

    'app_name': 'airlock',

    #oauth
    'oauth_client_id': '',
    'oauth_client_secret': '',

    'club_links': {
        'beer': {
            'home': 'http://beerhbc.org/',
            'join': '',
            'contact': '',
        },
        'hhcbc': {
            'home': 'http://www.hhcbc.org/',
            'join': '',
            'contact': '',
        },
        'libme': {
            'home': 'http://beermalt.org/',
            'join': '',
            'contact': '',
        },
    },

    # site themes (from bootswatch)
    'themes': ['default','divider','cerulean','cosmo','cyborg','darkly',
               'flatly','journal','lumen','paper','readable','sandstone',
               'simplex','slate','spacelab','superhero','united','yeti'],

    'tags': ['session-strength','standard-strength','high-strength',
             'very-high-strength','pale-color','amber-color','dark-color',
             'top-fermented','bottom-fermented','any-fermentation',
             'wild-fermented','lagered','aged','british-isles','western-europe',
             'central-europe','eastern-europe','north-america','pacific',
             'ipa-family','brown-ale-family','pale-ale-family',
             'pale-lager-family','pilsner-family','amber-ale-family',
             'amber-lager-family','dark-lager-family','porter-family',
             'stout-family','bock-family','strong-ale-family',
             'wheat-beer-family','specialty-beer','craft-style',
             'traditional-style','historical-style','malty','bitter','balanced',
             'hoppy','roasty','sweet','smoke','sour','wood','fruit','spice']

} # end config