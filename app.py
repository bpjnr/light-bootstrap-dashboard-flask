# -*- encoding: utf-8 -*-
"""
Flask Web App - Generated by www.AppSeed.us
AppSeed - developed by RoSoft | www.RoSoftware.ro
Licence: MIT
"""

import os
from app     import app #import flask app
from app     import db  #import db
from app.cli import create_user  #import cli functions

#----------------------------------------
# launch
#----------------------------------------

# This Code will be executed if app is started using python:
# python ./app.py 
if __name__ == "__main__":
	
	# schema it's created based on classes defined in models.py 
	db.create_all()

	# create a test user using 
	# create_user( email, username, password)
	create_user( 'test@appseed.us', 'appseed', 'pass')

	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
	
