from flask.helpers import flash
from webapp.db import db
from webapp.user.models import User

def create_and_add_user(username, email, password):
    user = User.query.filter(User.username == username).count()
    if user:
        flash(f"Пользователь с именем {username} уже существует!!!")
    if not user:
        flash(f"Создан пользователь {username}")
        new_user = User(username=username, email=email, password=password)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        