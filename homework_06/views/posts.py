from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    url_for,
)
from werkzeug.exceptions import BadRequest, NotFound

posts_app = Blueprint(
    "posts_app",
    __name__,
    url_prefix="/posts",
)


@posts_app.get(
    "/",
    endpoint="list",
)
def get_posts():
    return render_template(
        "posts/list.html",
#        prodposts=storage.get_posts(),
    )


@posts_app.route(
    "/add/",
    endpoint="add",
    methods=["GET", "POST"],
)
def create_post():
    if request.method == "GET":
        return render_template("posts/add.html")

    post_name = request.form.get("post-name", "")
    post_name = post_name.strip()
    if not post_name:
        raise BadRequest("post-name is required!")

    # post = crud.storage.create_post(
    #     name=post_name,
    # # )

    # url = url_for(
    #     "posts_app.details",
    #     post_id=post.id,
    # )
    # return redirect(url)


# @posts_app.get(
#     "/<int:post_id>/",
#     endpoint="details",
# )
# def get_post_details(post_id: int):
#     post: crud.post | None = crud.storage.get_post(
#         post_id=post_id,
#     )
#     if post is None:
#         raise NotFound(
#             description=f"post #{post_id} not found!",
#         )

#     return render_template(
#         "posts/details.html",
#         post=post,
#     )