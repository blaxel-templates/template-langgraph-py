from blaxel.telemetry.span import SpanManager
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from ..agent import agent

router = APIRouter()


class RequestInput(BaseModel):
    inputs: str


@router.post("/")
async def handle_request(request: RequestInput):
    with SpanManager("blaxel-langgraph").create_active_span("agent-request", {}):
        return StreamingResponse(agent(request.inputs), media_type="text/event-stream")
