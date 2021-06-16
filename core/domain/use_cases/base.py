from abc import ABC, abstractmethod


class ABCCreateOrderCartUseCase(ABC):
    @abstractmethod
    def execute(self):
        pass
