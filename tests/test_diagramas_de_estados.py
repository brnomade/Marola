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

    def test_basic_diagram(self):
        state = DiagramaDeEstados()

        state.seta_raiz("main")

        state.adiciona_estado_em("chime", "main")
        state.adiciona_estado_em("silence", "main")
        state.adiciona_estado_em("time", "main")

        state.seta_estado_default("time")

        state.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "_acao_emite_beep", "true")
        state.conecta_a_com_e_executando_caso("time", "silence", "b", "nil", "_acao_emite_beep", "true")
        state.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "_acao_em_chime", "true")

        state.seta_estado_inicial("time")

        state.seta_cliente(ContextoParaTeste())

        state.ativa()

        state.processa_evento("a")
        state.processa_evento("a")
        state.processa_evento("d")
        state.processa_evento("a")
        state.processa_evento("d")
        state.processa_evento("t_hits_hr")
        state.processa_evento("d")

        print(state)

    def test_chapter_6_listagem_61(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")
        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")
        print(state)

    def test_chapter_6_listagem_62(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")

        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")

        state.adiciona_estado_em("c_disab", "chime_st")
        state.adiciona_estado_em("quiet", "c_enab")
        state.adiciona_estado_em("c_beep", "c_enab")
        state.adiciona_estado_em("chime", "displays")
        state.adiciona_estado_em("time", "displays")

        print(state)

    def test_chapter_6_listagem_63(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")

        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")

        state.adiciona_estado_em("c_disab", "chime_st")
        state.adiciona_estado_em("quiet", "c_enab")
        state.adiciona_estado_em("c_beep", "c_enab")
        state.adiciona_estado_em("chime", "displays")
        state.adiciona_estado_em("time", "displays")

        state.seta_estado_default("c_disab")
        state.seta_estado_default("time")
        state.seta_estado_default("quiet")

        print(state)

    def test_chapter_6_listagem_64(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")

        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")

        state.adiciona_estado_em("c_disab", "chime_st")
        state.adiciona_estado_em("quiet", "c_enab")
        state.adiciona_estado_em("c_beep", "c_enab")
        state.adiciona_estado_em("chime", "displays")
        state.adiciona_estado_em("time", "displays")

        state.seta_estado_default("c_disab")
        state.seta_estado_default("time")
        state.seta_estado_default("quiet")

        state.seta_estado_inicial("chime_st")
        state.seta_estado_default("displays")

        print(state)

    def test_chapter_6_listagem_65(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")

        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")

        state.adiciona_estado_em("c_disab", "chime_st")
        state.adiciona_estado_em("quiet", "c_enab")
        state.adiciona_estado_em("c_beep", "c_enab")
        state.adiciona_estado_em("chime", "displays")
        state.adiciona_estado_em("time", "displays")

        state.seta_estado_default("c_disab")
        state.seta_estado_default("time")
        state.seta_estado_default("quiet")

        state.seta_estado_inicial("chime_st")
        state.seta_estado_default("displays")

        state.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emite_beep", "true")
        state.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emite_beep", "true")

        state.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        state.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        state.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "in_chime")
        state.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "in_chime")

        print(state)

    def test_chapter_6_listagem_66(self):
        state = DiagramaDeEstados()
        state.seta_nome_raiz("main")

        state.adiciona_superestado_em("chime_st", "main")
        state.adiciona_superestado_em("displays", "main")
        state.adiciona_superestado_em("c_enab", "chime_st")

        state.adiciona_estado_em("c_disab", "chime_st")
        state.adiciona_estado_em("quiet", "c_enab")
        state.adiciona_estado_em("c_beep", "c_enab")
        state.adiciona_estado_em("chime", "displays")
        state.adiciona_estado_em("time", "displays")

        state.seta_estado_default("c_disab")
        state.seta_estado_default("time")
        state.seta_estado_default("quiet")

        state.seta_estado_inicial("chime_st")
        state.seta_estado_inicial("displays")

        state.conecta_a_com_e_executando_caso("time", "chime", "a", "nil", "emiteBeep", "true")
        state.conecta_a_com_e_executando_caso("chime", "time", "a", "nil", "emiteBeep", "true")

        state.conecta_a_com_e_executando_caso("quiet", "c_beep", "t_hits_hr", "nil", "nil", "true")
        state.conecta_a_com_e_executando_caso("c_beep", "quiet", "beep_st", "nil", "nil", "true")
        state.conecta_a_com_e_executando_caso("c_disab", "quiet", "d", "nil", "nil", "inChime")
        state.conecta_a_com_e_executando_caso("c_enab", "c_disab", "d", "nil", "nil", "inChime")

        state.ativa()
        state.seta_cliente(self)
        state.processa_evento("a")
        state.processa_evento("a")
        #state.evento("d")
        #state.evento("a")
        #state.evento("d")
        #state.evento("t_hits_hr")
        #state.evento("d")


if __name__ == '__main__':
    unittest.main()
