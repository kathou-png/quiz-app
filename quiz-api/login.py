import flask
import jwt_utils as jwtU

def PostLogin(req):
	payload = req.get_json()
	password = payload['password']
	#si password ok
	if (password == "rookees"):
		token = jwtU.build_token()
		return  {"token" : token}, 200
	#sinon
	else:
		return '', 401