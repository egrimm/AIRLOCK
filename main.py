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
webapp2_config = config.config

app = webapp2.WSGIApplication(config=webapp2_config)
routes.add_routes(app)