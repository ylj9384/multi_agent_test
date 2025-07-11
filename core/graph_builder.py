from langgraph.graph import StateGraph, START
from .state_types import MessagesState
from agents.flight_assistant import flight_assistant
from agents.hotel_assistant import hotel_assistant
from agents.supervisor_agent import supervisor_agent
from agents.attraction_assistant import attraction_assistant  

def build_multi_agent_graph() -> StateGraph:
    graph = (
        StateGraph(MessagesState)
        .add_node(supervisor_agent)
        .add_node(flight_assistant)
        .add_node(hotel_assistant)
        .add_node(attraction_assistant)  # 新增
        .add_edge(START, supervisor_agent.name)
        .compile()
    )
    return graph