from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    edit_title = StringField(
        "Заголовок статьи",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    edit_text = TextAreaField(
        "Текст статьи", validators=[DataRequired()], render_kw={"class": "form-control"}
    )
    edit_category = StringField(
        "Категория новости",
        validators=[DataRequired()],
        render_kw={"class": "form-control"},
    )
    submit = SubmitField("Редактировать", render_kw={"class": "btn btn-primary"})
