from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_normal(self, normal):
        pass

    @abstractmethod
    def visit_descuento(self, reducido):
        pass