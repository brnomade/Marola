"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""
import unittest

from StateCharts.diagramas_de_estado import DiagramaDeEstados


class ContextoParaTeste:

    def _acao_generica(self, um_label, um_objeto_contexto):
        print("acao '{0}' disparada por '{1}'".format(um_label,
                                                      self.__class__.__name__ + str(hash(self)),
                                                      ))
        return "OK"

    def _acao_em_time(self, um_objeto_contexto):
        self._acao_generica("_acao_em_time", um_objeto_contexto)

    def _acao_em_chime(self, um_objeto_contexto):
        self._acao_generica("_acao_em_chime", um_objeto_contexto)

    def _acao_emite_beep(self, um_objeto_contexto):
        self._acao_generica("_acao_emite_beep", um_objeto_contexto)


class TestDiagramaDeEstados(unittest.TestCase):

    def test_classe_abstrata(self):
        self.assertFalse(DiagramaDeEstados.classe_abstrata())

    def test_imagem(self):
        self.assertEqual("diagrama", DiagramaDeEstados().imagem)

    def test_novo_diagrama_sem_nome(self):
        d = DiagramaDeEstados()
        self.assertEqual(d.raiz, d.o_estado(d.raiz).nome)

    def test_novo_diagrama_com_nome(self):
        d = DiagramaDeEstados("junk")
        self.assertEqual(d.raiz, d.o_estado(d.raiz).nome)

    def test_o_estado_invalid_input_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.o_estado(123)

    def test_o_estado_simbolo_inexistente_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(KeyError):
            d.o_estado("junk")

    def test_a_transicao_invalid_input_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.a_transicao(123)

    def test_a_transicao_simbolo_inexistente_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(KeyError):
            d.a_transicao("junk")

    def test_conecta_com_invalid_origem_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.conecta_a_com_e_executando_caso(123, d.raiz, "a", "nil", "_acao_emite_beep", "true")

    def test_conecta_com_invalid_destino_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.conecta_a_com_e_executando_caso(d.raiz, 123, "a", "nil", "_acao_emite_beep", "true")

    def test_conecta_com_invalid_evento_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, 123, "nil", "_acao_emite_beep", "true")

    def test_conecta_com_invalid_evento_colateral_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(KeyError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", 123, "_acao_emite_beep", "true")

    def test_conecta_com_invalid_acao_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", 123, "true")

    def test_conecta_com_invalid_condicao_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(ValueError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", 123)

    def test_o_estado_simbolo_existente_passes(self):
        d = DiagramaDeEstados()
        self.assertEqual(d.raiz, d.o_estado(d.raiz).nome)

    def test_ativa_sem_estados_definidos_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(AssertionError):
            d.ativa()

    def test_ativa_sem_estados_iniciais_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(AssertionError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", "true")
            d.ativa()

    def test_ativa_sem_cliente_valido_raises_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(AssertionError):
            d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", "true")
            d.seta_estado_inicial(d.raiz)
            d.ativa()

    def test_ativa_scenario_diagrama_minimo_sem_nome_passes(self):
        d = DiagramaDeEstados()
        d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", "true")
        d.seta_estado_inicial(d.raiz)
        d.seta_cliente(ContextoParaTeste())
        d.ativa()

    def test_ativa_scenario_diagrama_minimo_com_nome_passes(self):
        d = DiagramaDeEstados("junk")
        d.conecta_a_com_e_executando_caso("junk", "junk", "a", "nil", "_acao_emite_beep", "true")
        d.seta_estado_inicial("junk")
        d.seta_cliente(ContextoParaTeste())
        d.ativa()

    def test_client_indefinido_raise_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(KeyError):
            d.cliente

    def test_seta_cliente(self):
        d = DiagramaDeEstados()
        d.seta_cliente("junk")
        self.assertEqual("junk", d.cliente)

    def test_cliente_after_reseta_client_raise_exception(self):
        d = DiagramaDeEstados()
        with self.assertRaises(KeyError):
            d.seta_cliente("junk")
            self.assertEqual("junk", d.cliente)
            d.reseta_cliente()
            d.cliente

    def test_cliente_valido_for_new_instances_results_false(self):
        d = DiagramaDeEstados()
        self.assertFalse(d.cliente_valido)

    def test_cliente_valido_after_seta_cliente_results_true(self):
        d = DiagramaDeEstados()
        self.assertFalse(d.cliente_valido)
        d.seta_cliente("junk")
        self.assertTrue(d.cliente_valido)

    def test_processa_scenario_diagrama_minimo_sem_nome_passes(self):
        d = DiagramaDeEstados()
        d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", "true")
        d.seta_estado_inicial(d.raiz)
        d.seta_cliente(ContextoParaTeste())
        d.ativa()
        d.processa_evento("a")

    def test_processa_scenario_diagrama_minimo_com_nome_passes(self):
        d = DiagramaDeEstados("junk")
        d.conecta_a_com_e_executando_caso("junk", "junk", "a", "nil", "_acao_emite_beep", "true")
        d.seta_estado_inicial("junk")
        d.seta_cliente(ContextoParaTeste())
        d.ativa()
        d.processa_evento("a")

    def test_basic_diagram(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime", "main")
        d.adiciona_estado_em("silence", "main")
        d.adiciona_estado_em("time", "main")

        d.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "_acao_emite_beep", "true")
        d.conecta_a_com_e_executando_caso("time", "silence", "b", "nil", "_acao_emite_beep", "true")
        d.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "_acao_em_chime", "true")

        d.seta_estado_inicial("time")

        d.seta_cliente(ContextoParaTeste())

        d.ativa()

        d.processa_evento("a")
        d.processa_evento("a")
        d.processa_evento("d")
        d.processa_evento("a")
        d.processa_evento("d")
        d.processa_evento("t_hits_hr")
        d.processa_evento("d")

    def test_chapter_6_listagem_61(self):
        d = DiagramaDeEstados("main")
        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

    def test_chapter_6_listagem_62(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

    def test_chapter_6_listagem_63(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

    def test_chapter_6_listagem_64(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_inicial("displays")

    def test_chapter_6_listagem_65(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_inicial("displays")

        d.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emite_beep", "true")
        d.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emite_beep", "true")

        d.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "in_chime")
        d.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "in_chime")

    def test_chapter_6_listagem_66(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime_st", "main")
        d.adiciona_estado_em("displays", "main")
        d.adiciona_estado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_inicial("displays")

        d.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emite_beep", "true")
        d.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emite_beep", "true")

        d.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "in_chime")
        d.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "in_chime")

        d.seta_cliente(ContextoParaTeste())
        d.ativa()

        d.processa_evento("a")
        d.processa_evento("a")
        d.processa_evento("d")
        d.processa_evento("a")
        d.processa_evento("d")
        d.processa_evento("t_hits_hr")
        d.processa_evento("d")


if __name__ == '__main__':
    unittest.main()
