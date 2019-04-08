from app import db
import enum

class Gender(enum.Enum):
    male = "Male"
    female = "Female"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True)
    gender = db.Column(db.Enum(Gender))
    trainings = db.relationship('Training',backref='user',lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_type = db.Column(db.String(40), index=True)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime, index=True)
    duration = db.Column(db.Time)
    distance = db.Column(db.Float)

    def __repr__(self):
        return '<Training {}>'.format(self.training_type)
