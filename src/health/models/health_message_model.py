from datetime import datetime
from pydantic import BaseModel


class HealthMessage(BaseModel):
    status: str
    timestamp: datetime
