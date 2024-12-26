from flask import Blueprint

lol_bp = Blueprint('base', __name__, template_folder='templates', static_folder='static', static_url_path='/lol/static')

from . import routes