from typing import Any
import uvicorn
from fastapi import FastAPI, HTTPException
from service import create_payload
from schemas import PayloadRequest
from repositories import get_payload_by_id

app = FastAPI()

@app.post("/payload/")
def create_payload_endpoint(data: PayloadRequest) -> Any:
    return create_payload(data)

@app.get("/payload/{payload_id}")
def get_payload(payload_id: int) -> Any:
        payload = get_payload_by_id(payload_id)
        if payload:
            return {"output": payload.output_text}
        else:
            raise HTTPException(status_code=404, detail="no records with this id")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
