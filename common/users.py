from models.models import User
from app import db
class UsersCom():
	def get_all_users(self):
		list_user = []
		for user in User.query.all():
			list_user.append(user.as_dict())
		return list_user
	def create_new_user(self,info_user = None):
		if info_user is None:
			return
		user = User(info_user)
		db.session.add(user)
		db.session.commit()
		return user.as_dict()
	def delete_user(self,filter):
		users = User().query
		for key in filter:
			if hasattr(User(), key):
				users = users.filter(getattr(User,key) == filter[key])
		list_user = []
		for user in users.all():
			list_user.append(user.as_dict())
		row_affected = users.delete()
		db.session.commit()
		return list_user
	def get_just_user(self,id_user):
		user = User().query.filter(User.id_user == id_user)
		if user.count() > 0:
			return user.one().as_dict()
		return []
