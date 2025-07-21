from autogen import AssistantAgent

class AccountantAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_message(self, messages, sender, group_chat):
        content = messages[-1]["content"]
        if "process payment" in content.lower():
            print("[Accountant] Processing payment...")
            return "OK. Payment has been processed."
