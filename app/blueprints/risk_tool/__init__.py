from flask import Blueprint

risk_tool_bp = Blueprint('risk_tool', __name__)

from app.blueprints.risk_tool import routes