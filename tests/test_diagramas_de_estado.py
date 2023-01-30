"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""
import unittest

from StateCharts.diagramas_de_estado import DiagramaDeEstados


class TestDiagramaDeEstados(unittest.TestCase):

    def test_chapter_6_listagem_61(self):
        state = DiagramaDeEstados()
        state.seta_raiz_nome("main")
        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")
        print(state)


if __name__ == '__main__':
    unittest.main()
