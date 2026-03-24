from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    from app.blueprints.home import home_bp
    from app.blueprints.survival import survival_bp
    from app.blueprints.features import features_bp
    from app.blueprints.risk_tool import risk_tool_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(survival_bp)
    app.register_blueprint(features_bp)
    app.register_blueprint(risk_tool_bp)

    return app