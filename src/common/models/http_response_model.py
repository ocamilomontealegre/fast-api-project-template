from typing import Optional, Any
from pydantic import BaseModel
from common.types.data_type import DataType


class ResponseModel(BaseModel):
    status: int
    success: bool
    message: str
    data: Optional[Any] = None
    timestamp: str
