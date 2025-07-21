# agents/auctioneer_agent.py
from autogen import AssistantAgent

class AuctioneerAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)