from flask import Blueprint, render_template

views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def home():
    return render_template("index.html")
