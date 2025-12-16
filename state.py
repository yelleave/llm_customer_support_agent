from typing import TypedDict, List, Optional, Dict

class SupportState(TypedDict):
    user_input: str
    customer_id: Optional[str]

    chat_history: List[str]
    customer_profile: Optional[Dict]

    retrieved_docs: List[str]
    
    next_action: Optional[str]
    tool_args: Optional[str]

    response: Optional[str]
