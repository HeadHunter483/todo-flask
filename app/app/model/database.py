from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()


def init_manager(app):
    Migrate(app, db, render_as_batch=True)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    manager.run()


def init_database(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
