from langgraph.prebuilt import create_react_agent
from .handoff_tool import transfer_to_flight_assistant, transfer_to_hotel_assistant
from .llm import get_kimi_llm

# 业务工具
def book_attraction(attraction_name: str):
    """Book an attraction ticket"""
    return f"Successfully booked ticket for {attraction_name}."

attraction_assistant = create_react_agent(
    name="attraction_assistant",
    model=get_kimi_llm(),
    prompt="You are an attraction ticket booking assistant",
    tools=[book_attraction, transfer_to_flight_assistant, transfer_to_hotel_assistant]
)