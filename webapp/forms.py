from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    email = StringField(
        "Email", validators=[DataRequired()], render_kw={"class": "form-control"}
    )

    password = PasswordField(
        "Пароль", validators=[DataRequired()], render_kw={"class": "form-control"}
    )

    remember_me = BooleanField("Remember Me")

    submit = SubmitField("Отправить", render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField(
        "Имя пользователя",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )

    email = StringField(
        "Email", validators=[DataRequired()], render_kw={"class": "form-control"}
    )

    password1 = PasswordField(
        "Пароль", validators=[DataRequired()], render_kw={"class": "form-control"}
    )

    password2 = PasswordField(
        "Повторите Пароль",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
