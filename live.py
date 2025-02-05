from agents import MeAgent, ThinkAgent, ExperienceAgent
from memory.memory_manager import MemoryManager

# Initialize the system
memory = MemoryManager()
me = MeAgent(memory)
thinking = ThinkAgent(me)
experience = ExperienceAgent()

# Example usage
me.execute(experience, "Quest", "Exploring Consciousness")
