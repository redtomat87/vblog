"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, request, render_template
from flask_migrate import Migrate

#from asgiref.wsgi import WsgiToAsgi

from homework_06.app.views.posts import items_app
from homework_06.app.views.posts import products_app
from homework_06.app.views.posts import posts_app
#import psycopg
# print(psycopg)

import config
from models import db


app = Flask(__name__)

#asgi_app = WsgiToAsgi(app)

app.register_blueprint(
    items_app,
    # url_prefix="/items",
)

app.config.update(
    SECRET_KEY="6fc01f2db60feff0f53537060",
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO=config.SQLALCHEMY_ECHO,
)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(
    products_app,
)

app.register_blueprint(
    posts_app,
)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")



# @app.get("/posts/", endpoint="posts")
# def about():
#     return render_template("posts/list.html")


@app.route("/hello/")
@app.get("/hello/<name>/")
def hello_path_view(name: str | None = None):
    print(request)
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
