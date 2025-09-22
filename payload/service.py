from schemas import PayloadRequest
from repositories import create_payloads, get_payload_by_input
from typing import Any

def transformer(data: PayloadRequest) -> str:
    combined = []
    for a, b in zip(data.list_1, data.list_2):
        combined.append(a.upper())
        combined.append(b.upper())
    output_str = ' '.join(combined)
    return output_str

def create_input_string(list1: list[str], list2: list[str]) -> str:
    return f"{':'.join(list1)}|{':'.join(list2)}"

def create_payload(data: PayloadRequest) -> Any:
    if len(data.list_1) != len(data.list_2):
        return {"error": "Lists must have the same length"}
    input_str = create_input_string(data.list_1, data.list_2)
    payload = get_payload_by_input(input_str)
    if payload:
        return {"output": payload.id}
    output_str = transformer(data)
    payload_id = create_payloads(input_str, output_str)
    return {"output": payload_id}
