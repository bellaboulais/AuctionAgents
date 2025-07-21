from autogen import AssistantAgent

class AssistAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
