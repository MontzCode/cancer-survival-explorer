from flask import render_template
from app.blueprints.survival import survival_bp
from app.blueprints.survival.analysis import survival_by_stage, survival_by_subtype

@survival_bp.route('/survival')
def survival():
    stage_chart = survival_by_stage()
    subtype_chart = survival_by_subtype()
    return render_template('survival/survival.html', stage_chart=stage_chart, subtype_chart=subtype_chart)