# AuctionAgents

## Project Structure

/AuctionAgents
  /.venv
    ...
  /agents
    /accountant_agent.py
    /assistant_agent.py
    /auctioneer_agent.py
    /participant_agent.py
    /base_agent.py
  /protocols
    /message_bus.py
  auction_env.py
  main.py

## Dependencies

For autogen set up see: https://github.com/rcfroomin/sar_project/tree/master 

Simple set up:
  1. pip install autogen
  2. pip install openai

Virtual Environment: 
  python -m venv .venv
  source .venv/bin/activate

## Description

/agents 
1. Auctioneer: Manage the auction process, enforce protocol compliance, and determine winners.
2. Accountant: Oversee financial aspects: track bids, credits, debits, payments, and settlements.
3. Assistant: Provide information, guidance, and technical aid to participants; mediate interactions if needed.
4. Participant: Engage in the auction by submitting bids, forming (if allowed) coalitions, and aiming to maximize utility.

/protocols
- Current communication protocol is using group chat by autogen, where all agents can talk to each other.
- Message_bus.py is there to implement other communication protocols.
- See: https://microsoft.github.io/autogen/stable//user-guide/core-user-guide/framework/message-and-communication.html

auction_env.py
- setup environment including agents and communication protocol

main.py
- setup llm configuration
- start communication
