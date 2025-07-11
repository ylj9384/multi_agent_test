from langgraph.prebuilt import create_react_agent
from .handoff_tool import transfer_to_hotel_assistant, transfer_to_attraction_assistant
from .llm import get_kimi_llm

# 业务工具
def book_flight(from_airport: str, to_airport: str):
    """Book a flight"""
    return f"Successfully booked flight {from_airport} → {to_airport}."

flight_assistant = create_react_agent(
    name="flight_assistant",
    model=get_kimi_llm(),
    prompt="You are a flight booking assistant",
    tools=[book_flight, transfer_to_hotel_assistant, transfer_to_attraction_assistant]
)