# agents/base_agent.py
class BaseAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.environment = None  # set by environment on registration

    def receive(self, msg):
        print(f"[{self.name}] received message: {msg}")

    def send_message(self, to_role, msg):
        if self.environment:
            self.environment.protocol_hub.send(to_role, msg)

    def act(self):
        # To be implemented by subclasses
        pass
