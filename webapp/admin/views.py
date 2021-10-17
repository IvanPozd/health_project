from flask import Blueprint, flash, redirect, url_for, render_template
from flask_login import current_user

from webapp.admin.forms import RedactorForm

from webapp.db import db

from webapp.news.forms import NewsForm
from webapp.news.models import BDConnector

from webapp.user.decorators import admin_required

from datetime import datetime

blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@blueprint.route("/")
@admin_required
def admin():
    page_title = "Панель управления"
    text = "Контент админки"
    title = "Редактирование"
    form = RedactorForm()
    return render_template(
        "admin/index.html", page_title=page_title, text=text, user=current_user, form=form, title=title,
    )


@blueprint.route("/process_creating_news", methods=["POST"])
@admin_required
def process_creating_news():
    form = NewsForm()
    if form.validate_on_submit():
        news_exists = BDConnector.query.filter(
            BDConnector.title == form.news_title.data
        ).count()
        if news_exists:
            flash("Данная новость уже существует в базе")
            return redirect(url_for("admin.create_news"))
        else:
            new_news = BDConnector(
                title=form.news_title.data,
                category=form.news_category.data,
                text=form.news_text.data,
                published=datetime.now(),
            )
            db.session.add(new_news)
            db.session.commit()
            flash("Вы успешно добавили новость в базу")
            return redirect(url_for("news.index"))

    flash("Заполните все поля")
    return redirect(url_for("admin.create_news"))


@blueprint.route("/create_news")
@admin_required
def create_news():
    title = "Добавление новостей"
    form = NewsForm()
    return render_template(
        "admin/create_news.html", page_title=title, form=form, user=current_user
    )

@blueprint.route("/redactoring", methods=["POST"])
@admin_required
def redactor():
    form = RedactorForm()
    if form.validate_on_submit():
        redactor_news = BDConnector.query.filter(
            BDConnector.title == form.redactor_title.data
        )
        redactor_news.delete()
        redactor_news = BDConnector(
            title=form.redactor_title.data,
            category=form.redactor_category.data,
            text=form.redactor_text.data,
            published=datetime.now(),
                )
        db.session.add(redactor_news)
        db.session.commit()
        flash("Вы успешно отредактировали новость в базе")
        return redirect(url_for("news.index"))
