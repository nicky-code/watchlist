from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
from flask_login import login_required


