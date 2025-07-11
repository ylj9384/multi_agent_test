from langgraph.prebuilt import create_react_agent
from tools.flight_tools import book_flight
from tools.handoff_tool import transfer_to_hotel_assistant, transfer_to_attraction_assistant
from agents.llm import get_kimi_llm


flight_assistant = create_react_agent(
    name="flight_assistant",
    model=get_kimi_llm(),
    prompt="You are a flight booking assistant",
    tools=[book_flight, transfer_to_hotel_assistant, transfer_to_attraction_assistant]
)