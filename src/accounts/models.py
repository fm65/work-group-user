from datetime import datetime

from flask_login import UserMixin

from src import bcrypt, db


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='group', lazy='dynamic')


    def __repr__(self):
        return f"<Group {self.name}>"


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'))

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    @staticmethod
    def generate_fake(count=50, **kwargs):
        """Generate a number of fake users for testing."""
        from sqlalchemy.exc import IntegrityError
        from random import seed, choice

        groups = ['', 'Group1', 'Group2', 'Group3', 'Group4']

        seed()
        for i in range(count):
            u = User(
                username="user" + str(i+1),
                password="user" + str(i+1))
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

    def __repr__(self):
        return f"<username {self.username}>"
