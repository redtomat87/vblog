from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)
from werkzeug.exceptions import BadRequest, NotFound
from models import Post, db
from . import crud

posts_app = Blueprint(
    "posts_app",
    __name__,
    url_prefix="/posts",
)


@posts_app.get(
    "/",
    endpoint="list",
)
async def get_posts():
    return await render_template(
        "posts/list.html",
        posts=crud.get_posts(),
    )


@posts_app.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_post():
    if request.method == "GET":
        return render_template("posts/add.html")

    title = request.form.get("post-name", "")
    title = title.strip()
    if not title:
        raise BadRequest("post-name is required!")
    
    body = request.form.get("body-post", "")
    body = body.strip()
    if not body:
        raise BadRequest("body-post is required!")


    post = crud.create_posts(
        title=title,
        body=body,
    )

    flash(f"Created product {title!r}!", category="success")
    # return {"product": product.name, "id": product.id}
    url = url_for(
        "posts_app.details",
        post_id=post.id,
    )
    return redirect(url)


@posts_app.get(
    "/<int:post_id>/",
    endpoint="details",
)
def get_post_details(post_id: int):
    post: Post = Post.query.get_or_404(
        post_id,
        description=f"Post #{post_id} not found!",
    )
    return render_template(
        "posts_app/details.html",
        post=post,
    )


@posts_app.route(
    "/<int:post_id>/confirm-delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_post(post_id: int):
    post: Post = Post.query.get_or_404(
        post_id,
        description=f"Post #{post_id} not found!",
    )
    if request.method == "GET":
        return render_template(
            "posts/delete.html",
            post=post,
        )

    title = title
    body = body
    
    db.session.delete(post)
    db.session.commit()

    flash(f"Deleted {title!r} successfully!", category="warning")
    url = url_for("posts_app.list")
    return redirect(url)