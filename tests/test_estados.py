"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

import unittest

from StateCharts.estados import Estado
from StateCharts.transicoes import Transicao


class ContextoParaTeste:

    def _acao_generica(self, um_objeto_contexto):
        print("acao '{0}' disparada por '{1}'".format('_acao_generica',
                                                      self.__class__.__name__ + str(hash(self)),
                                                      ))
        return "OK"


class TestEstado(unittest.TestCase):

    def test_returns_false_to_abstract_class(self):
        self.assertFalse(Estado.classe_abstrata())

    def test_newly_created_estado(self):
        estado = Estado()
        self.assertFalse(estado.inicial)
        self.assertFalse(estado.default)
        self.assertFalse(estado.esta_contido)
        self.assertFalse(estado.connectado)
        self.assertFalse(estado.acao_valida)

    def test_seta_inicial_with_wrong_type_raises_exception(self):
        estado = Estado()
        with self.assertRaises(ValueError):
            estado.seta_inicial("junk")

    def test_seta_inicial_with_correct_type(self):
        estado = Estado()
        estado.seta_inicial(True)
        self.assertEqual(True, estado.inicial)

    def test_seta_default_with_wrong_type_raises_exception(self):
        estado = Estado()
        with self.assertRaises(ValueError):
            estado.seta_default("junk")

    def test_seta_default_with_correct_type(self):
        estado = Estado()
        estado.seta_default(True)
        self.assertEqual(True, estado.default)

    def test_seta_recipiente_with_wrong_type_raises_exception(self):
        estado = Estado()
        with self.assertRaises(ValueError):
            estado.seta_recipiente(True)

    def test_seta_recipiente_with_correct_type(self):
        estado = Estado()
        estado.seta_recipiente("Junk")
        self.assertEqual("Junk", estado.recipiente)

    def test_reseta_recipiente(self):
        estado = Estado()
        self.assertFalse(estado.esta_contido)
        estado.seta_recipiente("Junk")
        self.assertTrue(estado.esta_contido)
        self.assertEqual("Junk", estado.recipiente)
        estado.reseta_recipiente()
        self.assertFalse(estado.esta_contido)

    def test_newly_created_estado_nao_tem_conexoes(self):
        estado = Estado()
        self.assertFalse(estado.connectado)
        self.assertTrue(len(estado.transicoes) == 0)

    def test_transicoes_retorna_uma_lista(self):
        estado = Estado()
        self.assertTrue(isinstance(estado.transicoes, list))

    def test_adiciona_transicao_with_wrong_type_raises_exception(self):
        estado = Estado()
        with self.assertRaises(ValueError):
            estado.adiciona_transicao("Junk")

    def test_adiciona_transicao_with_correct_type(self):
        estado = Estado()
        junk = Transicao()
        estado.adiciona_transicao(junk)
        estado.seta_recipiente("Junk")
        self.assertEqual("Junk", estado.recipiente)

    def test_ativa_estado_em_context_valido(self):
        estado = Estado()
        estado.seta_acao("_acao_generica")
        resposta = estado.ativa_estado(ContextoParaTeste())
        self.assertEqual(resposta, "OK")

    def test_ativa_estado_em_context_invalido(self):
        estado = Estado()
        estado.seta_acao("_acao_inexistente")
        with self.assertRaises(AttributeError):
            resposta = estado.ativa_estado(ContextoParaTeste())

    def test_reseta_acao(self):
        estado = Estado()
        self.assertFalse(estado.acao_valida)
        estado.seta_acao("Junk")
        self.assertTrue(estado.acao_valida)
        self.assertEqual("Junk", estado.acao)
        estado.reseta_acao()
        self.assertFalse(estado.acao_valida)


if __name__ == '__main__':
    unittest.main()
