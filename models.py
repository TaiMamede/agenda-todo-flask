from app import db


class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120))
	user_id = db.Column(db.Integer)  # Link para a tabela user
	guest = db.Column(db.String(120))
	deadline = db.Column(db.DateTime)
	obs = db.Column(db.String(500))
	created = db.Column(db.DateTime)  # Colocar para autogerar a data de criação
	status = db.Column(db.String(120))

	# construtor
	def __init__(self, title, user_id, guest=None, deadline=None):
		self.title = title,
		self.user_id = user_id,
		self.guest = guest,
		self.deadline = deadline

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	email = db.Column(db.String(120))
	created = db.Column(db.DateTime)
	bio = db.Column(db.String(500))

	def __init__(self, name, email, created=None, bio=None):
		self.name = name,
		self.email = email,
		self.created = created,
		self.bio = bio,

class event(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120))
	user_id = db.Column(db.Integer)
	guest = db.Column(db.String(120))
	date = db.Column(db.DateTime)
	obs = db.Column(db.String(500))
	created = db.Column(db.DateTime(120))

	def __init__(self, id, title, user_id, guest=None, date=None, obs=None, created=None):
		self.id = id,
		self.title = title
		self.user_id =	user_id
		self.guest = guest
		self.date = date
		self.obs = obs
		self.created = created


