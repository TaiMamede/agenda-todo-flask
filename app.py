from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

app = Flask(__name__)
# Get configuration environment crom config file
app.config.from_object(config.get('dev'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    app.run()
