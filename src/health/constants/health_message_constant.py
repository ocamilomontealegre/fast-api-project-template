from datetime import datetime
from health.models.health_message_model import HealthMessage

HEALTH_MESSAGE = HealthMessage(
    status="🚀 Service up and running", timestamp=datetime.now()
)
