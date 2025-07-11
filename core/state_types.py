from langgraph.graph import START
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict

# 使用 Annotated 定义状态消息队列的更新策略
# 状态更新逻辑​：
# 工具调用后自动追加tool_message到状态（含tool_call_id和结果）
# 切换时传递完整消息历史，保障上下文连贯性
class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]