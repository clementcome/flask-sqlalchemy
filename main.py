from app import app, db
from app.models import Gender, User, Training

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Gender':Gender, 'User':User, 'Training':Training}