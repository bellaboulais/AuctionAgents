# auction_env.py
from autogen import GroupChat, GroupChatManager
from agents.auctioneer_agent import AuctioneerAgent
from autogen import UserProxyAgent

def setup_environment(num_participants, llm_config):
    # Create Auctioneer
    auctioneer = AuctioneerAgent(
        name="Auctioneer",
        system_message=(
            "You are the auctioneer for an English auction. "
            "Announce the item and starting price, accept higher bids, "
            "After every bid, wait a moment and if no one bets, confirm"
            "the bid and ask for a higher one. If no one answers, "
            "declare the winner after all participants say 'Done Bidding'."
        ),
        llm_config=llm_config,
    )

    # Create UserProxy participants
    participants = []
    for i in range(num_participants):
        participants.append(
            UserProxyAgent(
                name=f"Participant{i+1}",
                human_input_mode="ALWAYS",
                default_auto_reply="skip me",
                system_message=(
                    "You are a bidder. Enter your bid as an integer number (or say 'Done Bidding' when finished)."
                )
            )
        )

    agents = [auctioneer] + participants

    # Initial message starts the auction

    chat = GroupChat(agents=agents, messages=[], max_round=20)
    manager = GroupChatManager(
        groupchat=chat,
        name="AuctionManager",
        llm_config=llm_config,
    )

    print("Starting auction...\n")

    auctioneer.initiate_chat(
        manager,
        message="Ladies and gentlemen, welcome to our auction. The starting bid is $100. Who would like to start?"
    )

    return manager
