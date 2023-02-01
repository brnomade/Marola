"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

import unittest

from StateCharts.transicoes import Transicao


class ContextoParaTeste:

    def _acao_generica(self, um_objeto_contexto):
        print("transicao '{0}' disparada por '{1}'".format('_acao_generica',
                                                      self.__class__.__name__ + str(hash(self)),
                                                      ))
        return "OK"

    def _condicao_generica_true(self, um_objeto_contexto):
        print("condicao '{0}' testada por '{1}'".format('_condicao_true',
                                                      self.__class__.__name__ + str(hash(self)),
                                                      ))
        return True

    def _condicao_generica_false(self, um_objeto_contexto):
        print("condicao '{0}' testada por '{1}'".format('_condicao_false',
                                                    self.__class__.__name__ + str(hash(self)),
                                                    ))
        return False

    def _condicao_generica_nao_booleana(self, um_objeto_contexto):
        print("condicao '{0}' testada por '{1}'".format('_condicao_nao_booleana',
                                                    self.__class__.__name__ + str(hash(self)),
                                                    ))
        return None


class TestTransicao(unittest.TestCase):

    def test_returns_false_to_abstract_class(self):
        self.assertFalse(Transicao.classe_abstrata())

    def test_image_returns_string(self):
        transicao = Transicao()
        self.assertIsInstance(transicao.imagem, str)

    def test_newly_created_transicao(self):
        transicao = Transicao()
        self.assertFalse(transicao.evento_valido)
        self.assertTrue(transicao.incondicional)
        self.assertTrue(transicao.ciclo)
        self.assertFalse(transicao.conectada)
        self.assertFalse(transicao.origem_valida)
        self.assertFalse(transicao.destino_valido)
        self.assertFalse(transicao.acao_valida)
        self.assertTrue(transicao.abilitada)

    def test_seta_evento_with_wrong_type_raises_exception(self):
        transicao = Transicao()
        with self.assertRaises(ValueError):
            transicao.seta_evento(123)

    def test_seta_evento_with_correct_type(self):
        transicao = Transicao()
        transicao.seta_evento("Junk")
        self.assertEqual("Junk", transicao.evento)

    def test_evento_valido(self):
        transicao = Transicao()
        transicao.seta_evento("Junk")
        self.assertTrue(transicao.evento_valido)

    def test_reseta_evento(self):
        transicao = Transicao()
        self.assertFalse(transicao.evento_valido)
        transicao.seta_evento("Junk")
        self.assertTrue(transicao.evento_valido)
        self.assertEqual("Junk", transicao.evento)
        transicao.reseta_evento()
        self.assertFalse(transicao.evento_valido)
        self.assertEqual(None, transicao.evento)

    def test_seta_condicao_with_wrong_type_raises_exception(self):
        transicao = Transicao()
        with self.assertRaises(ValueError):
            transicao.seta_condicao(123)

    def test_seta_condicao_with_correct_type(self):
        transicao = Transicao()
        transicao.seta_condicao("Junk")
        self.assertEqual("Junk", transicao.condicao)

    def test_reseta_condicao(self):
        transicao = Transicao()
        self.assertTrue(transicao.incondicional)
        transicao.seta_condicao("Junk")
        self.assertFalse(transicao.incondicional)
        self.assertEqual("Junk", transicao.condicao)
        transicao.reseta_condicao()
        self.assertTrue(transicao.incondicional)
        self.assertEqual(None, transicao.condicao)

    def test_ciclo(self):
        transicao = Transicao()
        self.assertTrue(transicao.ciclo)
        transicao.seta_origem("Junk")
        self.assertFalse(transicao.ciclo)
        transicao.seta_destino("Junk")
        self.assertTrue(transicao.ciclo)
        transicao.reseta_origem()
        self.assertFalse(transicao.ciclo)
        transicao.reseta_destino()
        self.assertTrue(transicao.ciclo)

    def test_conectada(self):
        transicao = Transicao()
        self.assertFalse(transicao.conectada)
        transicao.seta_origem("Junk")
        self.assertFalse(transicao.conectada)
        transicao.seta_destino("Junk")
        self.assertTrue(transicao.conectada)
        transicao.reseta_origem()
        self.assertFalse(transicao.conectada)
        transicao.reseta_destino()
        self.assertFalse(transicao.conectada)

    def test_seta_origem_with_wrong_type_raises_exception(self):
        transicao = Transicao()
        with self.assertRaises(ValueError):
            transicao.seta_origem(123)

    def test_seta_origem_with_correct_type(self):
        transicao = Transicao()
        transicao.seta_origem("Junk")
        self.assertEqual("Junk", transicao.origem)

    def test_origem_valida_e_reseta_origem(self):
        transicao = Transicao()
        self.assertFalse(transicao.origem_valida)
        transicao.seta_origem("Junk")
        self.assertEqual("Junk", transicao.origem)
        self.assertTrue(transicao.origem_valida)
        transicao.reseta_origem()
        self.assertFalse(transicao.origem_valida)

    def test_seta_destino_with_wrong_type_raises_exception(self):
        transicao = Transicao()
        with self.assertRaises(ValueError):
            transicao.seta_destino(123)

    def test_seta_destino_with_correct_type(self):
        transicao = Transicao()
        transicao.seta_destino("Junk")
        self.assertEqual("Junk", transicao.destino)

    def test_destino_valido_e_reseta_destino(self):
        transicao = Transicao()
        self.assertFalse(transicao.destino_valido)
        transicao.seta_destino("Junk")
        self.assertEqual("Junk", transicao.destino)
        self.assertTrue(transicao.destino_valido)
        transicao.reseta_destino()
        self.assertFalse(transicao.destino_valido)

    def test_seta_acao_with_wrong_type_raises_exception(self):
        transicao = Transicao()
        with self.assertRaises(ValueError):
            transicao.seta_acao(123)

    def test_seta_acao_with_correct_type(self):
        transicao = Transicao()
        transicao.seta_acao("Junk")
        self.assertEqual("Junk", transicao.acao)

    def test_acao_valida_e_reseta_acao(self):
        transicao = Transicao()
        self.assertFalse(transicao.acao_valida)
        transicao.seta_acao("Junk")
        self.assertEqual("Junk", transicao.acao)
        self.assertTrue(transicao.acao_valida)
        transicao.reseta_acao()
        self.assertFalse(transicao.acao_valida)

    def test_abilitada_transicao_incondicional_esta_sempre_abilitada(self):
        transicao = Transicao()
        self.assertTrue(transicao.incondicional)
        self.assertTrue(transicao.abilitada("Junk"))

    def test_abilitada_transicao_com_condicao_true_esta_abilitada(self):
        transicao = Transicao()
        transicao.seta_condicao("_condicao_generica_true")
        self.assertTrue(transicao.abilitada(ContextoParaTeste()))

    def test_abilitada_transicao_com_condicao_false_nao_esta_abilitada(self):
        transicao = Transicao()
        transicao.seta_condicao("_condicao_generica_false")
        self.assertFalse(transicao.abilitada(ContextoParaTeste()))

    def test_abilitada_transicao_com_condicao_nao_boleana_raises_exception(self):
        transicao = Transicao()
        transicao.seta_condicao("_condicao_generica_nao_booleana")
        with self.assertRaises(ValueError):
            transicao.abilitada(ContextoParaTeste())

    def test_dispara_transicao_com_transicao_nao_conectada_raises_exception(self):
        transicao = Transicao()
        self.assertFalse(transicao.conectada)
        with self.assertRaises(ValueError):
            transicao.dispara_transicao("Junk")

    def test_dispara_transicao_com_acao_nao_valida_raises_exception(self):
        transicao = Transicao()
        transicao.seta_origem("Junk")
        transicao.seta_destino("Junk")
        self.assertTrue(transicao.conectada)
        self.assertFalse(transicao.acao_valida)
        with self.assertRaises(ValueError):
            transicao.dispara_transicao("Junk")

    def test_dispara_transicao_com_acao_valida_retorna_destino(self):
        transicao = Transicao()
        transicao.seta_acao("_acao_generica")
        transicao.seta_origem("Junk")
        transicao.seta_destino("Garbage")
        self.assertEqual(transicao.destino, transicao.dispara_transicao(ContextoParaTeste()))


if __name__ == '__main__':
    unittest.main()
