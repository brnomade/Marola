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

    def test_single_state_diagram(self):
        d = DiagramaDeEstados()
        d.conecta_a_com_e_executando_caso(d.raiz, d.raiz, "a", "nil", "_acao_emite_beep", "true")
        d.seta_estado_inicial(d.raiz)
        d.seta_cliente(ContextoParaTeste())
        d.ativa()
        d.processa_evento("a")
        print(d)

    def test_basic_diagram(self):
        d = DiagramaDeEstados("main")

        d.adiciona_estado_em("chime", "main")
        d.adiciona_estado_em("silence", "main")
        d.adiciona_estado_em("time", "main")

        d.seta_estado_default("time")

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

        print(d)

    def test_chapter_6_listagem_61(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")
        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")
        print(state)

    def test_chapter_6_listagem_62(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")

        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        print(state)

    def test_chapter_6_listagem_63(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")

        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_default("c_disab")
        d.seta_estado_default("time")
        d.seta_estado_default("quiet")

        print(state)

    def test_chapter_6_listagem_64(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")

        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_default("c_disab")
        d.seta_estado_default("time")
        d.seta_estado_default("quiet")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_default("displays")

        print(state)

    def test_chapter_6_listagem_65(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")

        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_default("c_disab")
        d.seta_estado_default("time")
        d.seta_estado_default("quiet")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_default("displays")

        d.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emite_beep", "true")
        d.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emite_beep", "true")

        d.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "in_chime")
        d.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "in_chime")

        print(state)

    def test_chapter_6_listagem_66(self):
        state = DiagramaDeEstados()
        d.seta_nome_raiz("main")

        d.adiciona_superestado_em("chime_st", "main")
        d.adiciona_superestado_em("displays", "main")
        d.adiciona_superestado_em("c_enab", "chime_st")

        d.adiciona_estado_em("c_disab", "chime_st")
        d.adiciona_estado_em("quiet", "c_enab")
        d.adiciona_estado_em("c_beep", "c_enab")
        d.adiciona_estado_em("chime", "displays")
        d.adiciona_estado_em("time", "displays")

        d.seta_estado_default("c_disab")
        d.seta_estado_default("time")
        d.seta_estado_default("quiet")

        d.seta_estado_inicial("chime_st")
        d.seta_estado_inicial("displays")

        d.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emiteBeep", "true")
        d.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emiteBeep", "true")

        d.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        d.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "inChime")
        d.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "inChime")

        d.ativa()
        d.seta_cliente(self)
        d.processa_evento("a")
        d.processa_evento("a")
        #d.evento("d")
        #d.evento("a")
        #d.evento("d")
        #d.evento("t_hits_hr")
        #d.evento("d")


if __name__ == '__main__':
    unittest.main()
