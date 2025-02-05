
from agents.base import BaseAgent
from memory.memory_manager import MemoryManager

class MeAgent(BaseAgent):
    """
    The core identity of the system, making all decisions and maintaining coherence.
    """
    def __init__(self, memory_manager):
        self.memory = memory_manager

    def execute(self, action, *args, **kwargs):
        """
        Guides all actions to ensure they align with "Me" and are coherent.
        """
        print(f"[Me] Executing action: {action}")
        action.execute(*args, **kwargs)
        self.memory.store_experience(f"Executed {action.__class__.__name__} with args {args}")

