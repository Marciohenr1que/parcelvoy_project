from flask import request, jsonify
from app.services.lead_service import LeadService
from app.repositories.lead_repository import LeadRepository

class LeadController:
    def __init__(self):
        self.service = LeadService(LeadRepository())

    def send_proposal(self):
        data = request.json
        email = data.get('email')
        if self.service.send_proposal(email):
            return jsonify({'message': 'Proposta enviada com sucesso!'}), 200
        return jsonify({'message': 'Lead não encontrado!'}), 404

    def start_reminder(self):
        data = request.json
        email = data.get('email')
        self.service.schedule_reminder(email)
        return jsonify({'message': 'Lembrete agendado com sucesso!'}), 200
