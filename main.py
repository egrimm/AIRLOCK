#-------------------------------------------------------------------------------
# Name:        main
# Purpose:
#
# Author:      egrimm
#
# Created:     2016-02-26
# Copyright:   (c) egrimm 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import webapp2
import handlers
import config
import routes
import logging
webapp2_config = config.config

def handle_404(request, response, exception):
    logging.exception(exception)
    response.write('Opps! I could swear this page was here a minute ago...')
    response.set_status(404)

def handle_500(request, response, exception):
    logging.exception(exception)
    response.write('Opps! Something went awry!')
    response.set_status(500)

app = webapp2.WSGIApplication(config=webapp2_config)
routes.add_routes(app)
app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500