from flask_restful import Resource, reqparse
from common.welcome import WelcomeCom

parser = reqparse.RequestParser()
class Welcome(Resource):
	def __init__(self):
		pass
	def post(self):
		msg = WelcomeCom()
		try:
			return msg.show_message("post")
		except TypeError as e:
			return str(e)
		except Exception as e:
			return str(e)
	def get(self):
		msg = WelcomeCom()
		try:
			return msg.show_message("get")
		except TypeError as e:
			return str(e)
		except Exception as e:
			return str(e)
	def put(self):
		msg = WelcomeCom()
		try:
			return msg.show_message('put')
		except TypeError as e:
			return str(e)
		except Exception as e:
			return str(e)
	def delete(self):
		msg = WelcomeCom()
		try:
			return msg.show_message('delete')
		except TypeError as e:
			return str(e)
		except Exception as e:
			return str(e)