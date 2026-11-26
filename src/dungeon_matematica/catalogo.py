from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True)
class Conceito:
    nome: str
    pre_requisitos: tuple[str, ...] = ()


@dataclass(frozen=True)
class Modulo:
    nome: str
    conceitos: tuple[str, ...]


CONCEITOS = MappingProxyType({
    "C1": Conceito("Números naturais e valor posicional"),
    "C2": Conceito("Adição", ("C1",)),
    "C3": Conceito("Subtração", ("C2",)),
    "C4": Conceito("Multiplicação", ("C2",)),
    "C5": Conceito("Divisão", ("C4",)),
    "C6": Conceito("Expressões numéricas", ("C3", "C5")),
    "C7": Conceito("Conceito e representação de frações", ("C1",)),
    "C8": Conceito("Frações equivalentes e simplificação", ("C7", "C5")),
    "C9": Conceito("Comparação e ordenação de frações", ("C8",)),
    "C10": Conceito("Fração de uma quantidade", ("C7", "C5")),
    "C11": Conceito("Representação decimal de frações", ("C7", "C5")),
    "C12": Conceito("Porcentagem como parte de 100", ("C8",)),
    "C13": Conceito("Conversão entre frações, decimais e porcentagens", ("C11", "C12")),
    "C14": Conceito("Cálculo de porcentagem de quantidades", ("C10", "C13")),
    "C15": Conceito("Descontos e acréscimos simples", ("C14", "C3")),
})

MODULOS = (
    Modulo("Operações fundamentais", ("C1", "C2", "C3", "C4", "C5", "C6")),
    Modulo("Frações", ("C7", "C8", "C9", "C10", "C11")),
    Modulo("Porcentagens", ("C12", "C13", "C14", "C15")),
)
