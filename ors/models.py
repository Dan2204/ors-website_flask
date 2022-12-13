from datetime import datetime
from ors import db, login_manager
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash


class EnquiryShort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, index=True)
    company_name = db.Column(db.String(64))
    email = db.Column(db.String(64), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    comments = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"name: {self.name}, email: {self.email}, phone: {self.phone}"

class EnquiryLong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(64), nullable=False, index=True)
    number_of_staff = db.Column(db.String(5))
    move_date = db.Column(db.String(20))
    address = db.Column(db.String(140), nullable=False)
    name = db.Column(db.String(64), nullable=False, index=True)
    phone = db.Column(db.String(20), nullable=False)
    mobile = db.Column(db.String(20))
    email = db.Column(db.String(64), nullable=False, index=True)
    comments = db.Column(db.String(140))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"name: {self.name}, email: {self.email}, phone: {self.phone}"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    editor = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"user: {self.username}, email: {self.email}, isAdmin: " \
                "{self.admin}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def is_admin(self):
        return self.admin
