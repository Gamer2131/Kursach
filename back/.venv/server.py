# server.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import psutil
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitoring.db'
db = SQLAlchemy(app)
CORS(app)

class MonitoringData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpu_usage = db.Column(db.Float, nullable=False)
    memory_usage = db.Column(db.Float, nullable=False)
    disk_usage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

@app.route('/api/monitoring', methods=['POST'])
def monitoring():
    try:
        data = request.json
        new_data = MonitoringData(
            cpu_usage=data['cpu_usage'],
            memory_usage=data['memory_usage'],
            disk_usage=data['disk_usage']
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        app.logger.error(f"Error processing monitoring data: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/monitoring', methods=['GET'])
def get_monitoring_data():
    try:
        data = MonitoringData.query.all()
        return jsonify([{
            'cpu_usage': d.cpu_usage,
            'memory_usage': d.memory_usage,
            'disk_usage': d.disk_usage,
            'timestamp': d.timestamp
        } for d in data])
    except Exception as e:
        app.logger.error(f"Error fetching monitoring data: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/system-status', methods=['GET'])
def get_system_status():
    try:
        uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
        status = {
            'uptime': str(uptime),
            'cpu_count': psutil.cpu_count(),
            'memory_total': psutil.virtual_memory().total,
            'disk_total': psutil.disk_usage('/').total
        }
        return jsonify(status)
    except Exception as e:
        app.logger.error(f"Error fetching system status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        # Удаляем все записи в таблице перед созданием новой базы данных
        db.drop_all()
        db.create_all()
    app.run(debug=True)
