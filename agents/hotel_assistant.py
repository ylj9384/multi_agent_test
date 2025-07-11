from langgraph.prebuilt import create_react_agent
from tools.hotel_tools import book_hotel
from tools.handoff_tool import transfer_to_flight_assistant, transfer_to_attraction_assistant
from agents.llm import get_kimi_llm

hotel_assistant = create_react_agent(
    name="hotel_assistant",
    model=get_kimi_llm(),
    prompt="You are a hotel booking assistant",
    tools=[book_hotel, transfer_to_flight_assistant, transfer_to_attraction_assistant]
)