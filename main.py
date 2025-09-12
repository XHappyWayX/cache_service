import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from database import crud, Payloads, session, tools

app = FastAPI()

class PayloadRequest(BaseModel):
    list_1: list[str]
    list_2: list[str]

def create_input_string(list1: list, list2: list) -> str:
    return f"{':'.join(list1)}|{':'.join(list2)}"

@app.post("/payload/")
def create_payload(data: PayloadRequest):
    if len(data.list_1) != len(data.list_2):
            return {"error": "Lists must have the same length"}
    input_str = create_input_string(data.list_1, data.list_2)
    payload = session.query(Payloads).filter_by(input_text=input_str).first()
    if payload:
        return {"output": payload.id}
    else:
        output_str = tools().transformer(data)
        id = crud().create_payloads(input_str, output_str)
        return {"output": id}

@app.get("/payload/{payload_id}")
def get_payload(payload_id: int):
        payload = session.query(Payloads).filter_by(id=payload_id).first()
        if payload:
            return {"output": payload.output_text}
        else: return {"error": "no records with this id"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)