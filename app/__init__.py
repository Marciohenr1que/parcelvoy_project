from flask import Flask
from celery import Celery

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Configuração do Celery
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)

    # Registrar Blueprints
    from app.routes.lead_routes import lead_routes
    app.register_blueprint(lead_routes)

    return app, celery
