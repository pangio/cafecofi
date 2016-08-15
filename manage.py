from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from cafecofi import db, app

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    """
    Creates a database with all of the tables defined in
    your Alchemy models
    """
    print 'Creating db...'
    db.create_all()
    print 'Done'


@manager.command
def drop_db():
    """
    Drops a database with all of the tables defined in
    your Alchemy models
    """
    db.drop_all()


@manager.command
def setup_nomad():
    create_db()


if __name__ == "__main__":
    # app.run(host='0.0.0.0', threaded=True)
    manager.run()
