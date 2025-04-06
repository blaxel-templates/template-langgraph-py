from typing import AsyncGenerator

from blaxel.models import bl_model
from blaxel.tools import bl_tools
from langchain.tools import tool
from langchain_core.messages import AIMessageChunk
from langgraph.prebuilt import create_react_agent


@tool
def weather(city: str) -> str:
    """Get the weather in a given city"""
    return f"The weather in {city} is sunny"

async def agent(input: str) -> AsyncGenerator[str, None]:
    prompt = "You are a helpful assistant that can answer questions and help with tasks."
    tools = await bl_tools(["blaxel-search"]).to_langchain() + [weather]
    model = await bl_model("sandbox-openai").to_langchain()
    agent = create_react_agent(model=model, tools=tools, prompt=prompt)
    messages = {"messages": [("user", input)]}
    async for chunk in agent.astream(messages, stream_mode=["updates", "messages"]):
        type_, stream_chunk = chunk
        # This is to stream the response from the agent, filtering response from tools
        if type_ == "messages" and len(stream_chunk) > 0 and isinstance(stream_chunk[0], AIMessageChunk):
            msg = stream_chunk[0]
            if msg.content:
                if not msg.tool_calls:
                    yield msg.content
        # This to show a call has been made to a tool, usefull if you want to show the tool call in your interface
        if type_ == "updates":
            if "tools" in stream_chunk:
                for msg in stream_chunk["tools"]["messages"]:
                    yield f"Tool call: {msg.name}\n"
