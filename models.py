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


# TODO: classe user e event
