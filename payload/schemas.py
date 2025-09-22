from pydantic import BaseModel

class PayloadRequest(BaseModel):
    list_1: list[str]
    list_2: list[str]
