import unittest
from graphlib import TopologicalSorter

from dungeon_matematica.aluno import Dificuldade, Dominio, ModeloAluno
from dungeon_matematica.catalogo import CONCEITOS, MODULOS
from dungeon_matematica.progressao import Desempenho, chefao_aprovado, fase_aprovada


class CatalogoTest(unittest.TestCase):
    def test_grafo_e_modulos_cobrem_os_15_conceitos(self):
        grafo = {codigo: conceito.pre_requisitos for codigo, conceito in CONCEITOS.items()}
        ordem = tuple(TopologicalSorter(grafo).static_order())
        campanha = tuple(codigo for modulo in MODULOS for codigo in modulo.conceitos)

        self.assertEqual(campanha, tuple(f"C{numero}" for numero in range(1, 16)))
        self.assertCountEqual(ordem, campanha)
        self.assertEqual(grafo["C7"], ("C1",))


class ModeloAlunoTest(unittest.TestCase):
    def test_inicia_sem_evidencias_para_todos_os_conceitos(self):
        aluno = ModeloAluno()
        for codigo in CONCEITOS:
            self.assertEqual(aluno.dominio(codigo), Dominio())

    def test_acertos_e_erros_respeitam_os_limites(self):
        casos = (
            (Dificuldade.FACIL, 10, 3),
            (Dificuldade.MEDIA, 15, 5),
            (Dificuldade.DIFICIL, 20, 7),
            (Dificuldade.MUITO_DIFICIL, 25, 10),
        )
        for dificuldade, ganho, perda in casos:
            with self.subTest(dificuldade=dificuldade):
                base = Dominio(pontos=50)
                self.assertEqual(base.avaliar_resposta(dificuldade, True).pontos, 50 + ganho)
                self.assertEqual(base.avaliar_resposta(dificuldade, False).pontos, 50 - perda)
                self.assertEqual(Dominio().avaliar_resposta(dificuldade, False).pontos, 0)
                cheio = Dominio(pontos=100)
                self.assertEqual(cheio.avaliar_resposta(dificuldade, True).pontos, 100)

    def test_dominio_exige_pontuacao_e_acertos_medio_e_dificil(self):
        aluno = ModeloAluno()
        for _ in range(7):
            aluno.registrar_resposta("C4", Dificuldade.FACIL, True)
        self.assertFalse(aluno.dominio("C4").dominado)
        aluno.registrar_resposta("C4", Dificuldade.MUITO_DIFICIL, True)
        aluno.registrar_resposta("C4", Dificuldade.MEDIA, True)
        self.assertFalse(aluno.dominio("C4").dominado)
        aluno.registrar_resposta("C4", Dificuldade.DIFICIL, True)
        self.assertTrue(aluno.dominio("C4").dominado)
        for _ in range(4):
            aluno.registrar_resposta("C4", Dificuldade.MUITO_DIFICIL, False)
        self.assertEqual(aluno.dominio("C4").pontos, 60)
        self.assertFalse(aluno.dominio("C4").dominado)
        self.assertEqual(aluno.dominio("C5"), Dominio())


class ProgressaoTest(unittest.TestCase):
    def test_fase_requer_70_por_cento(self):
        self.assertTrue(fase_aprovada(Desempenho(7, 10)))
        self.assertFalse(fase_aprovada(Desempenho(6, 10)))

    def test_chefao_requer_70_geral_e_60_por_conceito(self):
        modulo = MODULOS[0]
        resultados = dict.fromkeys(modulo.conceitos, Desempenho(3, 5))
        self.assertFalse(chefao_aprovado(modulo, resultados))
        for codigo in ("C1", "C2", "C3"):
            resultados[codigo] = Desempenho(4, 5)
        self.assertTrue(chefao_aprovado(modulo, resultados))
        resultados["C1"] = Desempenho(2, 4)
        resultados["C2"] = Desempenho(5, 5)
        self.assertFalse(chefao_aprovado(modulo, resultados))

    def test_chefao_exige_cobertura_e_arredonda_o_minimo_para_cima(self):
        modulo = MODULOS[0]
        resultados = dict.fromkeys(modulo.conceitos, Desempenho(4, 4))
        resultados["C5"] = Desempenho(2, 4)
        self.assertFalse(chefao_aprovado(modulo, resultados))
        resultados["C5"] = Desempenho(3, 4)
        self.assertTrue(chefao_aprovado(modulo, resultados))
        del resultados["C5"]
        with self.assertRaises(ValueError):
            chefao_aprovado(modulo, resultados)

    def test_desempenho_invalido(self):
        for acertos, total in ((0, 0), (3, 2), (-1, 2)):
            with self.subTest(acertos=acertos, total=total):
                with self.assertRaises(ValueError):
                    Desempenho(acertos, total)
