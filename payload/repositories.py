from typing import Optional
from models import Payloads
from database import session


def create_payloads(input_text: str, output_text: str) -> int:
    payload = Payloads(input_text = input_text, output_text = output_text)
    session.add(payload)
    session.commit()
    id = payload.id
    session.close()
    return id

def get_payload_by_id(payload_id: int) -> Optional[Payloads]:
    return session.query(Payloads).filter_by(id=payload_id).first()

def get_payload_by_input(input_text: str) -> Optional[Payloads]:
    return session.query(Payloads).filter_by(input_text=input_text).first()
