from app.repositories.lead_repository import LeadRepository
from app.models.lead import Lead
from app.tasks import send_reminder_email

class LeadService:
    def __init__(self, repository: LeadRepository):
        self.repository = repository

    def add_lead(self, email: str, name: str) -> Lead:
        lead = Lead(id=None, email=email, name=name, proposal_sent=False, response_received=False)
        return self.repository.save(lead)

    def send_proposal(self, email: str) -> bool:
        lead = self.repository.find_by_email(email)
        if lead:
            lead.proposal_sent = True
            self.repository.save(lead)
            return True
        return False

    def schedule_reminder(self, email: str):
        lead = self.repository.find_by_email(email)
        if lead and lead.proposal_sent and not lead.response_received:
            send_reminder_email.apply_async(args=[email, 'Lembrete: Proposta de Seguro Automotivo', 'Olá, notamos que você ainda não respondeu à nossa proposta '], countdown=86400)

