"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from StateCharts.abstract_statechart import ObjetoStateChart


class Estado(ObjetoStateChart):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __str__(self):
        return "({0}){1}-(I-{2},D-{3})-(A-{4},S{5}) > [{6}]".format(self.__class__.__name__,
                                                                    self._nome,
                                                                    self._is_initial,
                                                                    self._is_default,
                                                                    self._atividade,
                                                                    self._superestado,
                                                                    self._transicoes)

    def __repr__(self):
        return "({0}){1}-(I-{2},D-{3})-(A-{4},S{5}) > [{6}]".format(self.__class__.__name__,
                                                                    self._nome,
                                                                    self._is_initial,
                                                                    self._is_default,
                                                                    self._atividade,
                                                                    self._superestado,
                                                                    self._transicoes)

    def __init__(self):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__()
        self.seta_nome("#nil")
        self._atividade = "#nil"
        self._is_initial = False
        self._is_default = False
        self._transicoes = []
        self._superestado = "#nil"

    def adiciona_transicao(self, uma_transition):
        """ StateChart Project - Adiciona uma transicao ao blob. Nenhuma verificação é realizada.
        """
        self._transicoes.append(uma_transition)

    def ativa(self, um_diagrama):
        """
        StateChart Project - Ativa o receptor.
        """
        print("{0} !! |".format(self.nome))

        if self._atividade != "#nil":
            um_diagrama.client().perform_with_arguments(self._atividade, [um_diagrama])

    @property
    def atividate(self):
        return self._atividade

    def seta_atividade(self, um_symbol):
        """ StateChart Project - Seta o símbolo associado a atividade do receptor
                                 O símbolo recebe o statechart como parâmetro.
                                 A atividade é executada quando o estado é alcançado.
        """
        if isinstance(um_symbol, str):
            self._atividade = um_symbol
        else:
            raise AssertionError('Must be a string')

    def atividade_valida(self):
        """
        Statechart Project -  Retorna se a atividade é valida.
        """
        return self._atividade != "#nil"

    def contem_estado(self, a_symbol):
        """
        StateChart Project - Informa se o  receptor contém o estado de nome aSymbol.
        """
        raise AssertionError("must be implemented by sybclass")

    @property
    def default(self):
        """ StateChart Project - Retorna se o receptor é um estado default.
        """
        return self._is_default

    def seta_default(self, a_boolean):
        """ StateChart Project - Seta o se o receptor é estado default.
        """
        self._is_default = a_boolean

    @property
    def estado_pai(self):
        """ StateChart Project - Retorna  o superestado do receptor.
        """
        return self._superestado

    def seta_estado_pai(self, a_symbol):
        """
        StateChart Project - seta o estado aSymbol como superestado do receptor.
        """
        if isinstance(a_symbol, str):
            self._superestado = a_symbol
        else:
            raise AssertionError('Must be a string')

    @property
    def inicial(self):
        """ StateChart Project - Retorna o tipo do blob.
        """
        return self._is_initial

    def seta_inicial(self, a_boolean):
        """ StateChart Project - Seta o tipo do blob. Se inicial aBoolean é true.
        """
        self._is_initial = a_boolean

    @property
    def orfao(self):
        """
        StateChart Project - seta o estado aSymbol como superestado do receptor.
        """
        return self._superestado == "#nil"

    def selection_transicoes_em(self, a_symbol, um_diagrama):
        """  PRIVADO - Retorna as transições da hierarquia de estados iniciada no
                       receptor associada ao evento de nome aSymbol.
        """
        answer = []
        if not self.orfao:
            for transicao in self._transicoes:
                if transicao.disparavel(a_symbol, um_diagrama):
                    answer.append(transicao)
            estado = um_diagrama.o_estado(self.estado_pai)
            answer.append(estado.selection_transicoes_em(a_symbol, um_diagrama))
        return answer

    def sensivel_para(self, a_symbol, a_statechart):
        """ StateChart Project - Retorna true se alguma transição do receptor estiver
                                         associada ao evento de nome aSymbol e se esta
                                         for disparável.  As condições das transições são
                                         verificadas no contexto do aStateChart.
        """
        answer = False
        for transicao in self._transicoes:
            answer = answer or transicao.disparavel(a_symbol, a_statechart)
        return answer

    @property
    def superestado(self):
        """ StateChart Project - Retorna se o receptor é ou não um superestado
        """
        raise AssertionError('must be implemented by subclass')

    def transicao_para(self, a_symbol, um_diagrama):
        """
        StateChart Project - Retorna a transição do receptor associada ao evento de
                                           nome aSymbol.
        """
        if not isinstance(a_symbol, str):
            raise AssertionError('must be string')
        answer = self.selection_transicoes_em(a_symbol, um_diagrama)
        if len(answer) > 1:
            raise AssertionError('Ambiguidade no estado {0}'.format(self.nome))
        elif len(answer) == 0:
            return None
        else:
            return answer[0]

    def transicoes(self):
        """ StateChart Project - StateChart Project - Retorna uma colecao com as transicoes
                                                    conectadas ao blob.

        """
        return self._transicoes


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


class Superestado(Estado):

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
