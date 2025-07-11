# from core.graph_builder import build_multi_agent_graph
# from utils.printer import pretty_print_messages

# if __name__ == '__main__':
#     graph = build_multi_agent_graph()
#     init_state = {
#         "messages": [
#             {"role": "user", "content":
#              "book a flight from BOS to JFK and a stay at McKittrick Hotel"}
#         ]
#     }

#     for chunk in graph.stream(init_state, subgraphs=True):
#         pretty_print_messages(chunk)
#         # print(chunk)

from core.graph_builder import build_multi_agent_graph
from utils.printer import pretty_print_messages


if __name__ == '__main__':
    # 提示用户输入，并说明格式
    print("请输入您的需求，例如：Book a flight from Hangzhou to Beijing and a ticket for the Great Wall")
    print("请输入您的需求，例如：book a flight from BOS to JFK and a stay at McKittrick Hotel")
    graph = build_multi_agent_graph()
    # 新增：初始化消息历史
    messages = []

    while True:
        user_input = input("请输入：")
        if user_input.lower() in ["exit", "quit"]:
            print("已退出。"); break

        # 累加历史消息
        messages.append({"role": "user", "content": user_input})

        init_state = {
            "messages": messages
        }

        for chunk in graph.stream(init_state, subgraphs=True):
            pretty_print_messages(chunk)
            # 兼容 chunk 既可能是 dict 也可能是 (ns, dict) 的情况
            if isinstance(chunk, tuple):
                _, update = chunk
            else:
                update = chunk
            for node_update in update.values():
                for msg in node_update["messages"]:
                    if msg not in messages:
                        messages.append(msg)
            