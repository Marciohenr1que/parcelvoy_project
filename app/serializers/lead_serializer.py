from app.models.lead import Lead

class LeadSerializer:
    @staticmethod
    def serialize(lead: Lead) -> dict:
        return {
            'id': lead.id,
            'email': lead.email,
            'name': lead.name,
            'proposal_sent': lead.proposal_sent,
            'response_received': lead.response_received
        }
