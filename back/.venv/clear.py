from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitoring.db'
db = SQLAlchemy(app)

class MonitoringData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpu_usage = db.Column(db.Float, nullable=False)
    memory_usage = db.Column(db.Float, nullable=False)
    disk_usage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/clear-data', methods=['POST'])
def clear_data():
    try:
        db.session.query(MonitoringData).delete()
        db.session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        app.logger.error(f"Error clearing data: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
