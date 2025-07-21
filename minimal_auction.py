import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from agents.auctioneer_agent import AuctioneerAgent
from agents.assistant_agent import AssistAgent
from agents.accountant_agent import AccountantAgent
from agents.participant_agent import ParticipantAgent
from dotenv import load_dotenv
load_dotenv()

# Replace this with your real key or set the OPENAI_API_KEY env variable
llm_config = {
    "config_list": [
        {
            "model": "gpt-4o",  # or "gpt-4" or "gpt-3.5-turbo"
            "api_key": os.environ.get("OPENAI_API_KEY"),
        }
    ],
    "temperature": 0,
    "timeout": 600,
}

# --- Define core agents ---

auctioneer = AuctioneerAgent(
    name="Auctioneer",
    system_message=(
        "You are the auctioneer for an English auction with two participants. "
        "Announce the item and starting bid, accept legitimate bids, update the "
        "current price, and announce the winner when bidding ends. Only accept "
        "higher bids. Confirm settlement with the Accountant at the end."
    ),
    llm_config=llm_config,
)

accountant = AccountantAgent(
    name="Accountant",
    system_message=(
        "You are the Accountant. Keep track of all bids, participant balances, "
        "and notify when payments are complete. Reply 'OK' when a valid payment occurs."
    ),
    llm_config=llm_config,
)

assistant = AssistAgent(
    name="Assistant",
    system_message=(
        "You are the Auction Assistant. Answer participant questions about auction rules, "
        "bidding format, or auction procedure. Do NOT give bidding advice."
    ),
    llm_config=llm_config,
)

participant1 = ParticipantAgent(
    name="Participant1",
    system_message=(
        "You are a participant in the auction (Alice). Try to win the auctioned item "
        "while not overpaying. Only bid higher than the current price. "
        "Ask the assistant if unsure how to bid."
    ),
    llm_config=llm_config,
)

participant2 = ParticipantAgent(
    name="Participant2",
    system_message=(
        "You are a participant in the auction (Bob). Try to win the auctioned item "
        "without going over your budget. Only bid higher than the current price. "
        "Ask the assistant if unsure how to bid."
    ),
    llm_config=llm_config,
)

# --- Set up the group chat for orchestration ---

agents = [auctioneer, accountant, assistant, participant1, participant2]
groupchat = GroupChat(
    agents=agents,
    messages=[
        {
            "role": "system",
            "content": (
                "This is a single-item English auction for a 'Rare Painting'. "
                "The auctioneer initiates the auction. Participants take turns raising bids. "
                "When no more bids come in, auctioneer declares the winner. "
                "Accountant checks the payment at the end. "
                "Assistant is available for any participant questions."
            ),
        }
    ],
    max_round=10,
)
manager = GroupChatManager(groupchat, name="AuctionManager")

# --- Run the auction ---

if __name__ == "__main__":
    manager.run()
