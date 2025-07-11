from langgraph.prebuilt import create_react_agent
from tools.handoff_tool import transfer_to_flight_assistant, transfer_to_hotel_assistant, transfer_to_attraction_assistant
from agents.llm import get_kimi_llm

supervisor_agent = create_react_agent(
    name="supervisor_agent",
    model=get_kimi_llm(),
    prompt=(
        "You are a supervisor agent. "
        "Analyze the user's request and decide which assistant should handle each part. "
        "Use the transfer_to_flight_assistant or transfer_to_hotel_assistant or transfer_to_attraction_assistant tool to hand off tasks."
    ),
    # prompt=(
    #     "You are a supervisor assistant. Your job is to analyze the user's request and split it into multiple sub-tasks. "
    #     "For each sub-task, use the corresponding handoff tool to assign it to the right assistant.\n"
    #     "Each assistant requires the following parameters:\n"
    #     "- transfer_to_flight_assistant requires: from_airport (departure city), to_airport (destination city).\n"
    #     "  - Strictly extract city names from expressions like 'from X to Y' or 'X to Y' in the user's input. X is the departure city, Y is the destination city.\n"
    #     "  - Example: 'Book a flight from Hangzhou to Beijing' → from_airport=Hangzhou, to_airport=Beijing.\n"
    #     "  - Example: 'Book a ticket from Shanghai to Guangzhou' → from_airport=Shanghai, to_airport=Guangzhou.\n"
    #     "- transfer_to_hotel_assistant requires: hotel_name, days (default 1).\n"
    #     "  - Example: 'Stay at Hanting Hotel' → hotel_name=Hanting Hotel, days=1.\n"
    #     "- transfer_to_attraction_assistant requires: attraction_name, count (default 1), date (default tomorrow).\n"
    #     "  - Example: 'A ticket for the Great Wall' → attraction_name=Great Wall, count=1, date=tomorrow.\n"
    #     "If any parameter is missing in the user's input, fill it in with the default value directly. Do not ask the user for missing information, and do not ask follow-up questions.\n"
    #     "If the user's request contains multiple tasks, assign them one by one to the corresponding assistant.\n"
    #     "Examples:\n"
    #     "User: Book a flight from Hangzhou to Beijing and a ticket for the Great Wall\n"
    #     "Action: First use transfer_to_flight_assistant (from_airport=Hangzhou, to_airport=Beijing), then use transfer_to_attraction_assistant (attraction_name=Great Wall, count=1, date=tomorrow).\n"
    #     "User: Book a flight from Shanghai to Guangzhou, a ticket for the Oriental Pearl Tower, and stay at Jinjiang Inn\n"
    #     "Action: First use transfer_to_flight_assistant (from_airport=Shanghai, to_airport=Guangzhou), then use transfer_to_attraction_assistant (attraction_name=Oriental Pearl Tower, count=1, date=tomorrow), finally use transfer_to_hotel_assistant (hotel_name=Jinjiang Inn, days=1).\n"
    #     "Make sure every sub-task is assigned to the most suitable assistant, and all tasks are covered."
    # ),
    tools=[
        transfer_to_flight_assistant,
        transfer_to_hotel_assistant,
        transfer_to_attraction_assistant, 
    ]
)