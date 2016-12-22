from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#instance Flask Restful
api = Api(app)

app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#decorator to load page when url not found
@app.errorhandler(404)
def page_not_found(e):
	#returning message in json format
	return jsonify({"error":True,"message":"Sorry, URL Not Found"}),404

#importing class with different method http 
from resource.welcome import Welcome
from resource.users import Users

#adding endpoints to resources 
api.add_resource(Welcome, '/')
api.add_resource(Users,'/users','/user/<int:id_user>')