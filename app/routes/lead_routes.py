from flask import Blueprint, jsonify
from app.controllers.lead_controller import LeadController

lead_routes = Blueprint('lead_routes', __name__)
controller = LeadController()

@lead_routes.route('/send_proposal', methods=['POST'])
def send_proposal():
    return controller.send_proposal()

@lead_routes.route('/start_reminder', methods=['POST'])
def start_reminder():
    return controller.start_reminder()

@lead_routes.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Olá, essa API foi construída para entrar na empresa https://martechdm.com.'})
