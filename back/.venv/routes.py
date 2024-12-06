from flask import request, jsonify
from models import db, MonitoringData

def init_routes(app):
    @app.route('/api/monitoring', methods=['POST'])
    def monitoring():
        data = request.json
        new_data = MonitoringData(
            cpu_usage=data['cpu_usage'],
            memory_usage=data['memory_usage'],
            disk_usage=data['disk_usage']
        )
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'status': 'success'}), 200

    @app.route('/api/monitoring', methods=['GET'])
    def get_monitoring_data():
        data = MonitoringData.query.all()
        return jsonify([{
            'cpu_usage': d.cpu_usage,
            'memory_usage': d.memory_usage,
            'disk_usage': d.disk_usage,
            'timestamp': d.timestamp
        } for d in data])
