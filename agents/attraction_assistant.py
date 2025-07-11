from langgraph.prebuilt import create_react_agent
from tools.attraction_tools import book_attraction
from tools.handoff_tool import transfer_to_flight_assistant, transfer_to_hotel_assistant
from agents.llm import get_kimi_llm

attraction_assistant = create_react_agent(
    name="attraction_assistant",
    model=get_kimi_llm(),
    prompt="You are an attraction ticket booking assistant",
    tools=[book_attraction, transfer_to_flight_assistant, transfer_to_hotel_assistant]
)