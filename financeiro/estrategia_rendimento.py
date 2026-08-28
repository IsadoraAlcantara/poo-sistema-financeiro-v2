
from abc import ABC, abstractmethod


class EstrategiaRendimento(ABC):

    @abstractmethod
    def calcular(self, total: float) -> float:
        return total

class Poupanca(EstrategiaRendimento):

    def __init__(self, percentual: float) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("Percentual deve estar entre 0 e 100")
        self._percentual = percentual

    def calcular(self, total: float) -> float:
        pass
        