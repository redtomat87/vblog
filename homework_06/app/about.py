from flask import Blueprint, render_template

about = Blueprint(
    "about",
    __name__,
    url_prefix="/about",
)


@about.get(
    "/",
    endpoint="get_about",
)
def get_about():
    return render_template(                
        "about.html",
    )



# @about.get("/")
# def get_item_str(item_id: str):
#     return {
#         "string item id": item_id,
#     }

