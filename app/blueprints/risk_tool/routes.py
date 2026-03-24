from flask import render_template, request
from app.blueprints.risk_tool import risk_tool_bp
from app.blueprints.risk_tool.model import predict_survival

@risk_tool_bp.route('/risk', methods=['GET', 'POST'])
def risk():
    result = None
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            tumor_size = float(request.form['tumor_size'])
            tumor_stage = float(request.form['tumor_stage'])
            grade = float(request.form['grade'])
            npi = float(request.form['npi'])
            lymph_nodes = float(request.form['lymph_nodes'])
            mutation_count = float(request.form['mutation_count'])

            survival_prob, deceased_prob = predict_survival(
                age, tumor_size, tumor_stage, grade, npi, lymph_nodes, mutation_count
            )
            result = {
                'survival': survival_prob,
                'deceased': deceased_prob
            }
        except Exception as e:
            result = {'error': str(e)}

    return render_template('risk_tool/risk_tool.html', result=result)