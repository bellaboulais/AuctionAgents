from autogen import AssistantAgent

class ParticipantAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
