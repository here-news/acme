from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all agents in the AcMe system.
    """
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
