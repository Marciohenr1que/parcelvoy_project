from dataclasses import dataclass
from typing import Optional

@dataclass
class Lead:
    id: Optional[int]
    email: str
    name: str
    proposal_sent: bool
    response_received: bool
