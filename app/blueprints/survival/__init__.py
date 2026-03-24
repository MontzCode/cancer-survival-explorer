from flask import Blueprint

survival_bp = Blueprint('survival', __name__)

from app.blueprints.survival import routes