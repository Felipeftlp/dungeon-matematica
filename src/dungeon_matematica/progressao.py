from collections.abc import Mapping
from dataclasses import dataclass

from dungeon_matematica.catalogo import Modulo


@dataclass(frozen=True)
class Desempenho:
    acertos: int
    total: int

    def __post_init__(self) -> None:
        if not 0 <= self.acertos <= self.total or self.total == 0:
            raise ValueError("Informe um total positivo e um número válido de acertos.")

    def atinge(self, percentual: int) -> bool:
        return self.acertos * 100 >= self.total * percentual


def fase_aprovada(desempenho: Desempenho) -> bool:
    return desempenho.atinge(70)


def chefao_aprovado(modulo: Modulo, por_conceito: Mapping[str, Desempenho]) -> bool:
    if por_conceito.keys() != set(modulo.conceitos):
        raise ValueError("O resultado deve cobrir cada conceito do módulo.")

    total = Desempenho(
        acertos=sum(resultado.acertos for resultado in por_conceito.values()),
        total=sum(resultado.total for resultado in por_conceito.values()),
    )
    return total.atinge(70) and all(
        resultado.atinge(60) for resultado in por_conceito.values()
    )
