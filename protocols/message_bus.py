# protocols/message_bus.py
class MessageBus:
    def __init__(self):
        self.listeners = {}

    def register(self, role, agent):
        if role not in self.listeners:
            self.listeners[role] = []
        self.listeners[role].append(agent)

    def send(self, to_role, msg):
        if to_role not in self.listeners:
            print(f"No listeners for role {to_role}")
            return
        for agent in self.listeners[to_role]:
            agent.receive(msg)
