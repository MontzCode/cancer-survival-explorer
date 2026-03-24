from flask import render_template
from app.blueprints.survival import survival_bp
from app.blueprints.survival.analysis import survival_by_stage

@survival_bp.route('/survival')
def survival():
    chart = survival_by_stage()
    return render_template('survival/survival.html', chart=chart)