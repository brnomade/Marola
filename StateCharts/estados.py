"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from StateCharts.abstract_statecharts import ObjetoStateChart
from StateCharts.transicoes import Transicao


class Estado(ObjetoStateChart):

    @property
    def imagem(self):
        return "blob"

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __str__(self):
        return "({0}){1} : {2} -> {3}".format(self.__class__.__name__,
                                              self._nome,
                                              self._acao,
                                              self._transicoes)

    def __repr__(self):
        return "({0}){1} : {2} -> {3}".format(self.__class__.__name__,
                                              self._nome,
                                              self._acao,
                                              self._transicoes)

    def __init__(self):
        """
            transitions : lista com todas as transições que partem de self.
            recipiente : o nome to estado em que self esta incluido
        """
        super().__init__()
        self._is_initial = False
        self._is_default = False
        self._recipiente = None
        self._transicoes = []
        self._acao = None

    @property
    def inicial(self):
        """ StateChart Project - Retorna o tipo do blob.
        """
        return self._is_initial

    def seta_inicial(self, a_boolean):
        """ StateChart Project - Seta o tipo do blob. Se inicial aBoolean é true.
        """
        if isinstance(a_boolean, bool):
            self._is_initial = a_boolean
        else:
            raise ValueError('Must be a boolean value')

    @property
    def default(self):
        """ StateChart Project - Retorna se o receptor é um estado default.
        """
        return self._is_default

    def seta_default(self, a_boolean):
        """ StateChart Project - Seta o se o receptor é estado default.
        """
        if isinstance(a_boolean, bool):
            self._is_default = a_boolean
        else:
            raise ValueError('Must be a boolean value')

    @property
    def esta_contido(self):
        """
        StateChart Project - retorna True se self esta contido em outro estado.
        """
        return self._recipiente is not None

    @property
    def recipiente(self):
        """ StateChart Project - Retorna o superestado do receptor.
        """
        return self._recipiente

    def seta_recipiente(self, a_symbol):
        """
        StateChart Project - seta o estado aSymbol como superestado do receptor.
        """
        if isinstance(a_symbol, str):
            self._recipiente = a_symbol
        else:
            raise ValueError('Must be a string')

    def reseta_recipiente(self):
        """
        StateChart Project - reseta o recipiente de self para o mesma situacao no momento da criacao de self.
        """
        self._recipiente = None

    @property
    def acao(self):
        """
        Statechart Project -  Retorna a atividade do estado.
        """
        return self._acao

    @property
    def acao_valida(self):
        """
        Statechart Project -  Retorna se a acao de self esta definida.
        """
        return self._acao is not None

    def seta_acao(self, um_symbol):
        """ StateChart Project - Seta o símbolo associado a acao do receptor
                                 O símbolo recebe o statechart como parâmetro.
                                 A atividade é executada quando o estado é alcançado.
        """
        if isinstance(um_symbol, str):
            self._acao = um_symbol
        else:
            raise AssertionError('Must be a string')

    def reseta_acao(self):
        """
        StateChart Project - reseta a acao de self para o mesma situacao no momento da criacao de self.
        """
        self._acao = None

    # def sensivel_para(self, a_symbol, a_statechart):
    #     """ StateChart Project - Retorna true se alguma transição do receptor estiver
    #                                      associada ao evento de nome aSymbol e se esta
    #                                      for disparável.  As condições das transições são
    #                                      verificadas no contexto do aStateChart.
    #     """
    #     answer = False
    #     for transicao in self._transicoes:
    #         answer = answer or transicao.disparavel(a_symbol, a_statechart)
    #     return answer

    @property
    def connectado(self):
        """ StateChart Project - Retorna true se self estado connectado via transicoes.
        """
        return len(self._transicoes) > 0

    def adiciona_transicao(self, uma_transition):
        """ StateChart Project - Adiciona uma transicao ao blob.
        """
        if isinstance(uma_transition, Transicao):
            self._transicoes.append(uma_transition)
        else:
            raise ValueError('must be instance of Transicao')

    # def seleciona_transicoes_em(self, a_symbol, um_diagrama):
    #     """  PRIVADO - Retorna as transições da hierarquia de estados iniciada no
    #                    receptor associada ao evento de nome aSymbol.
    #     """
    #     answer = []
    #     if not self.esta_contido:
    #         for transicao in self._transicoes:
    #             if transicao.disparavel_para(a_symbol, um_diagrama):
    #                 answer.append(transicao)
    #         estado = um_diagrama.o_estado(self.recipiente)
    #         answer.extend(estado.seleciona_transicoes_em(a_symbol, um_diagrama))
    #     return answer

    # def transicao_para(self, a_symbol, um_diagrama):
    #     """
    #     StateChart Project - Retorna a transição do receptor associada ao evento de
    #                                        nome aSymbol.
    #     """
    #     if not isinstance(a_symbol, str):
    #         raise AssertionError('must be string')
    #
    #     answer = self.seleciona_transicoes_em(a_symbol, um_diagrama)
    #
    #     if len(answer) > 1:
    #         raise AssertionError('Ambiguidade no estado {0}'.format(self.nome))
    #     elif len(answer) == 0:
    #         return None
    #     else:
    #         return answer[0]

    @property
    def transicoes(self):
        """ StateChart Project - StateChart Project - Retorna uma colecao com as transicoes
                                                    conectadas ao blob.

        """
        return self._transicoes

    def ativa_estado(self, um_objeto_contexto):
        """
        StateChart Project - Ativa o estado executando sua atividade no contexto de um_objeto_contexto.
        Retorna o resultado da execucao ou None.
        """
        resposta = None
        if self.acao_valida:
            method_to_call = getattr(um_objeto_contexto, self._acao.lower())
            resposta = method_to_call(um_objeto_contexto)
        return resposta


class EstadoSimples(Estado):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def contem_estado(self, a_symbol):
        """
        StateChart Project - Informa se o  receptor contém o estado de nome aSymbol.
        """
        return False

    @property
    def imagem(self):
        """ StateChart Project - Retorna a imagem do estado
        """
        if self._is_initial:
            return "blobi"
        else:
            return "blobd"

    @property
    def superestado(self):
        """ StateChart Project - Retorna se o receptor é ou não um superestado
        """
        return False


class EstadoComposto(Estado):

    def __init__(self):
        """
            PRIVADO - Inicializações do blob nodo.
        """
        super().__init__()
        self._lista_de_estados = []
        self._estado_ativo = None

    def adiciona_estado(self, a_symbol):
        """
          " StateChart Project - Adiciona o blob de nome aSymbol ao blob receptor.
          "
        """
        self._lista_de_estados.append(a_symbol)

    def contem_estado(self, a_symbol):
        """
        StateChart Project - Informa se o receptor contém o estado de nome aSymbol.
        """
        return a_symbol in self._lista_de_estados

    def estados_default_2(self, um_diagrama):
        """
        StateChart Project - Retorna os subestados do receptor que
                                            tem o atributo default setado para true.
        """
        answer = []
        for nome_do_estado in self._lista_de_estados:
            if um_diagrama.o_estado(nome_do_estado).default:
                answer.append(nome_do_estado)
        return answer

    def estados_default(self, um_diagrama):
        """
        StateChart Project - Retorna os subestados do receptor que
                             tem o atributo default setado para true.
        """
        answer = []
        for nome_do_estado in self._lista_de_estados:
            estado = um_diagrama.o_estado(nome_do_estado)
            if estado.default:
                answer.append(nome_do_estado)
                if estado.superestado:
                    answer.append(estado.estados_default(um_diagrama))
        return answer

    @property
    def imagem(self):
        """ StateChart Project - Retorna a imagem do estado
        """
        if self._is_initial:
            return "blobni"
        else:
            return "blobnd"

    def nome_dos_estados(self):
        """
        StateChart Project - Retorna o nome de todos os estados contidos no
                                          receptor.
        """
        return self._lista_de_estados

    def remove_subestado(self, a_symbol):
        """
          " StateChart Project - Remove o subestado de nome aSymbol.
          "
        """
        if a_symbol in self._lista_de_estados:
            self._lista_de_estados.remove(a_symbol)

    @property
    def superestado(self):
        """ StateChart Project - Retorna se o receptor é ou não um superestado
        """
        return True
