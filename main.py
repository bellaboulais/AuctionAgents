from autogen import AssistantAgent, GroupChat, GroupChatManager
from agents.auctioneer_agent import AuctioneerAgent
import os
from dotenv import load_dotenv
from auction_env import setup_environment
load_dotenv()

NUM_PARTICIPANTS = 3

llm_config = {
    "config_list": [{
        "model": "gpt-4",
        "api_key": os.getenv("OPENAI_API_KEY"),
    }],
    "temperature": 0.7,
}

manager = setup_environment(NUM_PARTICIPANTS, llm_config)
print(f"Launching English Auction with {NUM_PARTICIPANTS} participants.")

manager.run()
