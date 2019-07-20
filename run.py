import os
from app import create_app, db
from app.models import *
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

def main():
    db.create_all()

@app.cli.command()
def test():
    '''run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

if __name__ == "__main__":
    with app.app_context():
        main()