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

} # end config