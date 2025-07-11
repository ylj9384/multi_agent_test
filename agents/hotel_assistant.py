from langgraph.prebuilt import create_react_agent
from .handoff_tool import transfer_to_flight_assistant, transfer_to_attraction_assistant
from .llm import get_kimi_llm

# 业务工具
def book_hotel(hotel_name: str):
    """Book a hotel stay"""
    return f"Successfully booked stay at {hotel_name}."

hotel_assistant = create_react_agent(
    name="hotel_assistant",
    model=get_kimi_llm(),
    prompt="You are a hotel booking assistant",
    tools=[book_hotel, transfer_to_flight_assistant, transfer_to_attraction_assistant]
)