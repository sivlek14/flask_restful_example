class WelcomeCom():
	def show_message(self,method):
		if isinstance(method,str):
			return "hey you method is "+ method
		else:
			raise TypeError("please, give me arguments type string")