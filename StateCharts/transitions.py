"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""


class ObjetoTransicao:

    def __init__(self, a_name):
        if a_name:
            self._nome = a_name
        else:
            self._nome = self.__class__.__name__ + '#' + str(hash(self))

    def __str__(self):
        return "{0}".format(self._nome)

    def __repr__(self):
        return "{0}".format(self._nome)

    @property
    def nome(self):
        """ Retorna o nome do objeto
        """
        return self._nome

    def seta_nome(self, a_string):
        """ Define o nome do objeto
        """
        if a_string:
            self._nome = a_string
        else:
            raise SyntaxError("Empty name received")


class Transicao(ObjetoTransicao):

    def __init__(self):
        super().__init__(self.__class__.__name__ + '#' + str(hash(self)))
        self._evento = None
        self._condicao = lambda statechart: True
        self._blob_destino = None
        self._acao = lambda statechart: print("{0} -> ".format(statechart))

    @property
    def evento(self):
        """
        " Retorna o evento associado a transicao
        "
        """
        return self._evento

    def seta_evento(self, a_symbol):
        """
        " Seta o evento associado a transicao
        "
        """
        # TODO: How to check this -> Symbol mustBeSymbol: aSymbol.
        self._evento = a_symbol

    @property
    def condicao(self):
        """
        return the condicao
        """
        return self._condicao

    def seta_condicao(self, a_lamda):
        """
        Seta o bloco condicao da transicao.
        Antes do disparo o bloco é avaliado. Se o resultado da
        avaliação for true, a transicao pode ser disparada.
        O bloco recebe o statechart como parâmetro, e deve retornar
        true ou false como resultado do teste.
        """
        # if callable(mylambda) and mylambda.__name__ == "<lambda>"
        if callable(a_lamda):
            self._condicao = a_lamda
        else:
            raise AssertionError("Must be a lambda or a function")

    @property
    def destino(self):
        """
        " Retorna o blob destino da transição
        "
        """
        return self._blob_destino

    def seta_destino(self, a_symbol):
        """
        " Seta o nome do blob destino da transição
        "
        """
        # TODO: How to check this -> Symbol mustBeSymbol: aSymbol.
        self._blob_destino = a_symbol

    @property
    def acao(self):
        """
        " Retorna o blob destino da transição
        "
        """
        return self._acao

    def seta_acao(self, a_lamda):
        """
        " Seta o bloco acao da transicao.
        A ação é executada antes do estado ser alcançado.
        O bloco recebe o statechart como parametro.
        "
        """
        if callable(a_lamda):
            self._acao = a_lamda
        else:
            raise AssertionError("Must be a lambda or a function")

    def dispara(self, an_owner):
        """
        " Dispara a transição usando anOwner como contexto da
        ação. Retorna o blob destino da transição.
        "
        """
        if self._blob_destino:
            self._acao(an_owner)
        else:
            raise AssertionError("A transição não está conectada")
        return self._blob_destino

    def disparavel(self, an_event, an_owner):
        """
        " Testa se a transição é disparável com o evento de nome
        aSymbol e com dono anOwner.
        A transição é disparável se o evento aSymbol for o mesmo
        evento da transição e se a condição avaliada no contexto
        de anOwner for verdadeira.
        "
        """
        if self._evento == an_event:
            return self._condicao(an_owner)
        else:
            return False
