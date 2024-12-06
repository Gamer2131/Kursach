from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MonitoringData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpu_usage = db.Column(db.Float, nullable=False)
    memory_usage = db.Column(db.Float, nullable=False)
    disk_usage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
