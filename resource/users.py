from flask_restful import Resource, reqparse
from flask import request, jsonify
from common.users import UsersCom

parser = reqparse.RequestParser()
class Users(Resource):
	def post(self):
		userController = UsersCom()
		user_create = userController.create_new_user(request.get_json())
		response = []
		response.append({"message":"user_created"})
		response.append({"response":user_create})
		return jsonify(response)
	
	def get(self, id_user = None):
		if id_user is None:
			users = UsersCom()
			users = users.get_all_users()
			response = []
			response.append({"message":"list_users"})
			response.append({"response":users})
			return jsonify(response)
		else:
			users = UsersCom()
			users = users.get_just_user(id_user)
			response = []
			response.append({"message":"user_details"})
			response.append({"response":users})
			return jsonify(response)
			
	def delete(self, id_user = None):
		if id_user is None:
			userController = UsersCom()
			users_deleted = userController.delete_user(request.get_json())
			response = []
			response.append({"message":"users_deleted"})
			response.append({"response":users_deleted})
			return jsonify(response)
		else:
			userController = UsersCom()
			user_deleted = userController.delete_user({"id_user":id_user})
			response = []
			response.append({"message":"user_deleted"})
			response.append({"response":user_deleted})
			return jsonify(response)
			
	def put(self):
		return "Sorry, this method not implemented",200