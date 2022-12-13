from flask import Blueprint

bp = Blueprint('core', __name__)

from ors.core import views
