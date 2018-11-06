from app.model import *
from app.controller import *
import yaml

with app.open_resource('config.yaml', 'r') as stream:
    config = yaml.load(stream)
app.config['SECRET_KEY'] = config['server']['secret']
app.config['DATABASE_FILE'] = config['database']['name']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
db.init_app(app)
