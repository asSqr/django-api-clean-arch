from .base import ABCCreateOrderCartUseCase


class CreateOrderCartUseCase(ABCCreateOrderCartUseCase):
    def execute(self):
        return {"Ola": "Mundo"}
