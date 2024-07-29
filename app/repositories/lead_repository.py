from typing import Optional
from app.models.lead import Lead

class LeadRepository:
    def __init__(self):
        self.leads = []  # memoria

    def save(self, lead: Lead) -> Lead:
        lead.id = len(self.leads) + 1
        self.leads.append(lead)
        return lead

    def find_by_email(self, email: str) -> Optional[Lead]:
        for lead in self.leads:
            if lead.email == email:
                return lead
        return None

    def find_all_unresponsive(self) -> list[Lead]:
        return [lead for lead in self.leads if lead.proposal_sent and not lead.response_received]

