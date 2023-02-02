"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""
from StateCharts.abstract_statecharts import ObjetoStateChart


class Transicao(ObjetoStateChart):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __str__(self):
        return "({0}){1} : {2} [ {3} ] / {4} -> {5}".format(self.__class__.__name__,
                                                            self._nome,
                                                            self._evento,
                                                            self._condicao,
                                                            self._acao,
                                                            self._destino)

    def __repr__(self):
        return "({0}){1} : {2} [ {3} ] / {4} -> {5}".format(self.__class__.__name__,
                                                            self._nome,
                                                            self._evento,
                                                            self._condicao,
                                                            self._acao,
                                                            self._destino)

    def __eq__(self, other):
        if not isinstance(other, Transicao):
            return False
        else:
            return (self._acao == other._acao) and (self._evento == other._evento) and \
                (self._condicao == other._condicao) and (self._origem == other._origem) and \
                (self._destino == other._destino)

    def __init__(self):
        super().__init__()
        self._evento = None
        self._condicao = None
        self._origem = None
        self._destino = None
        self._acao = None

        self.reseta_evento()
        self.reseta_condicao()
        self.reseta_origem()
        self.reseta_destino()
        self.reseta_acao()

    @property
    def imagem(self):
        """ StateChart Project - Retorna a imagem da transicao
        """
        if self.conectada:
            return "transicao_connectada"
        else:
            return "transicao_invalida"

    @property
    def evento(self):
        """
        Statechart Project -  Retorna o evento do transicao.
        """
        return self._evento

    @property
    def evento_valido(self):
        """
        Statechart Project -  Retorna se a evento de self esta definido.
        """
        return self._evento is not None

    def seta_evento(self, um_symbol):
        """ StateChart Project - Seta o evento associado a transicao
        """
        if isinstance(um_symbol, str):
            self._evento = um_symbol
        else:
            raise ValueError('Must be a string')

    def reseta_evento(self):
        """
        StateChart Project - reseta o evento de self para o mesma situacao no momento da criacao de self.
        """
        self._evento = None

    @property
    def condicao(self):
        """
        StateChart Project - Retorna o símbolo associado a condicao da transicao.
        """
        return self._condicao

    def seta_condicao(self, um_symbol):
        """ StateChart Project - Seta o símbolo associado a condicao de self
                                 O símbolo recebe o statechart como parâmetro.
                                 A atividade é executada quando o estado é alcançado.
        """
        if isinstance(um_symbol, str):
            self._condicao = um_symbol
        else:
            raise ValueError('Must be a string')

    def reseta_condicao(self):
        """
        StateChart Project - reseta a acao de self para o mesma situacao no momento da criacao de self.
        """
        self._condicao = None

    @property
    def incondicional(self):
        """
        Statechart Project - Informa se a condicao da transicao é sempre verdadeira.
        """
        return self._condicao is None

    @property
    def ciclo(self):
        """
        StateChart Project - Retorna true se a transicao tem origem e destino iguais
        """
        return self._origem == self._destino

    @property
    def conectada(self):
        """ StateChart Project - Retorna true se a transicao tem origem e
        destino definidos.
        """
        return self.origem_valida and self.destino_valido

    @property
    def origem(self):
        """
        StateChart Project - Retorna a origem da transição
        """
        return self._origem

    @property
    def origem_valida(self):
        """
        Statechart Project -  Retorna se a origem de self esta definida.
        """
        return self._origem is not None

    def seta_origem(self, a_symbol):
        """ Statechart Project - Seta o nome da origem da transição
        """
        if isinstance(a_symbol, str):
            self._origem = a_symbol
        else:
            raise ValueError('must be string')

    def reseta_origem(self):
        """
        StateChart Project - reseta a origem de self para o mesma situacao no momento da criacao de self.
        """
        self._origem = None

    @property
    def destino(self):
        """
        StateChart Project - Retorna o destino da transição
        """
        return self._destino

    @property
    def destino_valido(self):
        """
        Statechart Project -  Retorna se o destino de self esta definido.
        """
        return self._destino is not None

    def seta_destino(self, a_symbol):
        """ Statechart Project - Seta o nome do destino da transição
        """
        if isinstance(a_symbol, str):
            self._destino = a_symbol
        else:
            raise ValueError('must be string')

    def reseta_destino(self):
        """
        StateChart Project - reseta o destino de self para o mesma situacao no momento da criacao de self.
        """
        self._destino = None

    @property
    def acao(self):
        """
        Statechart Project -  Retorna a atividade do transicao.
        """
        return self._acao

    @property
    def acao_valida(self):
        """
        Statechart Project -  Retorna se a acao de self esta definida.
        """
        return self._acao is not None

    def seta_acao(self, um_symbol):
        """ StateChart Project - Seta o símbolo associado a acao de self
                                 O símbolo recebe o statechart como parâmetro.
                                 A atividade é executada quando o estado é alcançado.
        """
        if isinstance(um_symbol, str):
            self._acao = um_symbol
        else:
            raise ValueError('Must be a string')

    def reseta_acao(self):
        """
        StateChart Project - reseta a acao de self para o mesma situacao no momento da criacao de self.
        """
        self._acao = None

    # def altera_estado_para(self, old_symbol, new_symbol):
    #     """
    #     StateChart Project - Altera o nome do estado conectado a transição
    #                                      de oldSymbol para newSymbol.
    #     """
    #
    #     if not isinstance(old_symbol, str):
    #         raise AssertionError("Must be a string")
    #
    #     if not isinstance(new_symbol, str):
    #         raise AssertionError("Must be a string")
    #
    #     if self._origem == old_symbol:
    #         self._origem = new_symbol
    #
    #     if self._destino == old_symbol:
    #         self._destino = new_symbol

    def dispara_transicao(self, um_objeto_contexto):
        """
        StateChart Project - Dispara a transição no contexto de um_objeto_contexto
                               Retorna o estado destino da transição.
        """
        if self.conectada:
            if self.acao_valida:
                method_to_call = getattr(um_objeto_contexto, self.acao.lower())
                method_to_call(um_objeto_contexto)
                return self.destino
            else:
                raise ValueError("A acao nao e' valida")
        else:
            raise ValueError("A transição não está conectada")

    def abilitada(self, um_objeto_contexto):
        """
        StateChart Project - Testa se a transição esta abilitada.
                             a condicao e avaliada no contexto de um_objeto_contexto.
        """
        if self.incondicional:
            return True
        else:
            method_to_call = getattr(um_objeto_contexto, self.condicao.lower())
            resposta = method_to_call(um_objeto_contexto)
            if isinstance(resposta, bool):
                return resposta
            else:
                raise ValueError('Condicao nao retornou um valor boleano.')
