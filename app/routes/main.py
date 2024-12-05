from flask import Blueprint, render_template, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html',
                         total_transactions=525461,
                         total_fraud=26228,
                         fraud_rate=4.99)

@main.route('/analysis-report', methods=['GET'])
def analysis_report():
    try:
        country = request.args.get('country', '')
        date_range = request.args.get('date_range', '')
        
        return render_template('analysis_report.html',
                             selected_country=country,
                             selected_date_range=date_range)
    except Exception as e:
        print(f"Error in analysis report: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Export the Blueprint instance
__all__ = ['main'] 