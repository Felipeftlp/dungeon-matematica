from dataclasses import dataclass, replace
from enum import StrEnum

from dungeon_matematica.catalogo import CONCEITOS


class Dificuldade(StrEnum):
    FACIL = "fácil"
    MEDIA = "média"
    DIFICIL = "difícil"
    MUITO_DIFICIL = "muito difícil"


VARIACOES = {
    Dificuldade.FACIL: (10, -3),
    Dificuldade.MEDIA: (15, -5),
    Dificuldade.DIFICIL: (20, -7),
    Dificuldade.MUITO_DIFICIL: (25, -10),
}


@dataclass(frozen=True)
class Dominio:
    pontos: int = 0
    acertos_por_dificuldade: frozenset[Dificuldade] = frozenset()

    @property
    def dominado(self) -> bool:
        return self.pontos >= 70 and {
            Dificuldade.MEDIA,
            Dificuldade.DIFICIL,
        }.issubset(self.acertos_por_dificuldade)

    def avaliar_resposta(self, dificuldade: Dificuldade, correta: bool) -> "Dominio":
        ganho, perda = VARIACOES[dificuldade]
        pontos = min(100, max(0, self.pontos + (ganho if correta else perda)))
        acertos = self.acertos_por_dificuldade
        if correta:
            acertos = acertos | {dificuldade}
        return replace(self, pontos=pontos, acertos_por_dificuldade=acertos)


class ModeloAluno:
    def __init__(self) -> None:
        self._dominios = {codigo: Dominio() for codigo in CONCEITOS}

    def dominio(self, codigo: str) -> Dominio:
        return self._dominios[codigo]

    def registrar_resposta(
        self, codigo: str, dificuldade: Dificuldade, correta: bool
    ) -> Dominio:
        dominio = self.dominio(codigo).avaliar_resposta(dificuldade, correta)
        self._dominios[codigo] = dominio
        return dominio
