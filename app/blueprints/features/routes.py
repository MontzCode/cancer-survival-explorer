from flask import render_template
from app.blueprints.features import features_bp
from app.blueprints.features.analysis import feature_importance_chart

@features_bp.route('/features')
def features():
    chart = feature_importance_chart()
    return render_template('features/features.html', chart=chart)