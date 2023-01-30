"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from StateCharts.abstract_statechart import ObjetoStateChart


class Transicao(ObjetoStateChart):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __init__(self):
        super().__init__(self.__class__.__name__ + '#' + str(hash(self)))
        self._evento = "#nil"
        self._condicao = "#true"    # indica que a condicao é sempre verdadeira
        self._origem = "#nil"
        self._destino = "#nil"
        self._acao = "#nil"

    def __eq__(self, other):
        if not isinstance(other,Transicao):
            return False
        else:
            return self._acao == other._acao and \
                self._evento == other._evento and \
                self._condicao == other._condicao and \
                self._origem == other._origem and \
                self._destino == other._destino

    @property
    def acao(self):
        """
        " Retorna o blob destino da transição
        "
        """
        return self._acao

    def seta_acao(self, a_symbol):
        """
        StateChart Project - Seta o símbolo associado a transicao.
                                        O símbolo recebe o statechart como parâmetro.
                                        A ação é executada antes do estado ser alcançado.
        """
        if isinstance(a_symbol, str):
            self._acao = a_symbol
        else:
            raise AssertionError("Must be a string")

    def acao_valida(self):
        """
        Statechart Project -  Retorna se a acao é valida.
        """
        return self._acao != "#nil"

    def altera_estado_para(self, old_symbol, new_symbol):
        """
        StateChart Project - Altera o nome do estado conectado a transição
                                         de oldSymbol para newSymbol.
        """

        if not isinstance(old_symbol, str):
            raise AssertionError("Must be a string")

        if not isinstance(new_symbol, str):
            raise AssertionError("Must be a string")

        if self._origem == old_symbol:
            self._origem = new_symbol

        if self._destino == old_symbol:
            self._destino = new_symbol

    @property
    def auto_transicao(self):
        """
        StateChart Project - Retorna true se a transicao conecta um estado a si mesmo.
        """
        return self._origem == self._destino

    @property
    def condicao(self):
        """
        StateChart Project - Retorna o símbolo associado a condicao da transicao.
        """
        return self._condicao

    def seta_condicao(self, a_symbol):
        """
        StateChart Project - Seta o símbolo associado a condicao da transicao.
                                          O símbolo recebe o statechart como parâmetro, e deve
                                           retornar true ou false como resultado do teste da condição.
                                           Antes do disparo a condição é avaliada. Se o resultado for
                                          true a transição pode ser disparada.
        """
        if not isinstance(a_symbol, str):
            raise AssertionError("Must be a string")
        self._condicao = a_symbol

    @property
    def evento(self):
        """
        " StateChart Project - Retorna o evento associado a transicao
        "
        """
        return self._evento

    def seta_evento(self, a_symbol):
        """
        " StateChart Project - Seta o evento associado a transicao
        "
        """
        if isinstance(a_symbol, str):
            self._evento = a_symbol
        else:
            raise AssertionError('must be string')

    @property
    def connectada(self):
        """ StateChart Project - Retorna true se a transicao tem o esatdo origem e o
        estado destino definidos.
        """
        return (self._origem != "#nil") and (self._destino != "#nil")

    @property
    def destino(self):
        """
        " StateChart Project - Retorna o estado destino da transição
        "
        """
        return self._destino

    def seta_destino(self, a_symbol):
        """
        " Statechart Project - Seta o nome do estado destino da transição
        "
        """
        if not isinstance(a_symbol, str):
            raise AssertionError('must be a string')
        self._destino = a_symbol

    def dispara(self, a_statechart):
        """
        " StateChart Project - Dispara a transição usando o owner do statechart
                                       passado como parâmetro como contexto da ação.
                                       Retorna o estado destino da transição.
        "
        """
        if self._destino == "#nil":
            raise AssertionError("A transição não está conectada")

        if self._acao != "#nil":
            a_statechart.cliente().perform_with_arguments(self._acao, [a_statechart])

        return self._destino

    def disparavel_para(self, a_symbol, a_statechart):
        """
        " StateChart Project - Testa se a transição é disparável com o evento de nome
                                        aSymbol e no contexto de aStateChart.
                                        A transição é disparável se o evento aSymbol for o mesmo
                                        evento da transição e se a condição avaliada no contexto
                                       de aStateChart for verdadeira.
        "
        """
        if self._evento != a_symbol:
            return False

        if self._condicao == "#true":
            return True

        return a_statechart.cliente().perform_with_arguments(self._condicao, [a_statechart])

    def imagem_padrao(self, a_boolean):
        """ StateChart Project - Retorna a imagem da transicao
        """
        if self._destino == "#nil" or self._origem == "#nil":
            return "transiko"
        elif a_boolean:
            return 'transiok'
        else:
            return "transokl"

    @property
    def incondicional(self):
        """
        " Statechart Project - Informa se a condicao da transicao é sempre
                                           verdadeira.

         "
        """
        return self._condicao == "#true"

    @property
    def origem(self):
        """
        " StateChart Project - Retorna o estado origem da transição

         "
        """
        return self._origem

    def seta_origem(self, a_symbol):
        """ Statechart Project - Seta o nome do estado origem da transição
        """
        if not isinstance(a_symbol, str):
            raise AssertionError('must be string')
        else:
            self._origem = a_symbol

