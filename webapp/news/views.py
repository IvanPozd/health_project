from flask import abort, Blueprint, render_template, Response, flash, request
from flask_login import current_user
from webapp.news.forms import SearchForm
from webapp.news.models import News
from PIL import Image
from io import BytesIO
from fuzzywuzzy import fuzz
from webapp.food.views import graph_maker
from random import random, choice

blueprint = Blueprint("news", __name__)


@blueprint.route("/")
@blueprint.route("/index")
def index():
    page_title = "Главная страница"
    text = """Мы рады Вас приветствовать на нашем сайте """
    text2 = """Здесь будет интересный блок """
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.id.desc()).limit(5)
    if current_user.is_authenticated:
        script, div, data_check = graph_maker(3)
        return render_template(
            "news/index.html",
            page_title=page_title,
            text=text,
            text2=text2,
            user=current_user,
            news_list=news_list,
            the_script=script,
            the_div=div,
            data_check=data_check,
        )
    return render_template(
        "news/index.html",
        page_title=page_title,
        text=text,
        text2=text2,
        user=current_user,
        news_list=news_list,
    )


@blueprint.route("/about")
def about():
    page_title = "Наш проект"
    return render_template("news/about.html", page_title=page_title, user=current_user)


@blueprint.route("/news")
def display_news():
    form = SearchForm()
    title = "Новости"
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.id.desc()).all()
    return render_template(
        "news/news.html",
        page_title=title,
        form=form,
        news_list=news_list,
        user=current_user,
    )


@blueprint.route("/process_searching_news", methods=["GET"])
def process_searching_news():
    form = SearchForm()
    title = "Новости Python"
    search_title = request.values[form.search_news.name]
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.id.desc()).all()
    news_exists = []
    if form.validate_on_submit:
        for news in news_list:
            Ratio = fuzz.token_sort_ratio(news.title, search_title)
            if Ratio >= 50:
                news_exists += News.query.filter(
                    News.title == news.title
                ).all()
        if news_exists:
            return render_template(
                "news/news.html",
                page_title=title,
                form=form,
                news_list=news_exists,
                user=current_user,
            )
        flash("Новость не найдена, попробуйте изменить запрос")
        return render_template(
            "news/news.html",
            page_title=title,
            form=form,
            news_list=news_list,
            user=current_user,
        )


@blueprint.route("/news/<int:news_id>", methods=["GET"])
def news(news_id):
    news_context = News.query.filter(News.id == news_id).first()
    if not news_context:
        abort(404)
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.id.desc()).limit(5)

    return render_template(
        "news/news_id.html",
        page_title=news_context.title,
        news_context=news_context,
        news_list=news_list,
        user=current_user,
    )


@blueprint.route("/img/<int:img_id>")
def get_image(img_id):
    news_img = News.query.filter(News.id == img_id).first()
    if news_img.image:

        image = Image.open(BytesIO(news_img.image))
        output = BytesIO()
        image.save(output, "PNG")
        contents = output.getvalue()
        output.close()

        return Response(contents, mimetype="image/png")


@blueprint.route("/category/<url>", methods=["GET"])
def category(url):
    if url == "meal":
        category_list = News.query.filter(
            News.category == "Питание"
        ).all()
        page_title = "Новости про питание"
    elif url == "train":
        category_list = News.query.filter(
            News.category == "Тренировки"
        ).all()
        page_title = "Новости про тренировки"

    return render_template(
        "news/category.html",
        category_list=category_list,
        page_title=page_title,
        user=current_user,
    )
