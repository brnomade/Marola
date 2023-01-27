"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""


class ObjetoBlob:

    def __init__(self, a_string):
        if a_string:
            self._nome = a_string
        else:
            self._nome = self.__class__.__name__ + '#' + str(hash(self))

    def __str__(self):
        return "{0}".format(self._nome)

    def __repr__(self):
        return "{0}".format(self._nome)

    @property
    def nome(self):
        """ Retorna o nome da objeto
        """
        return self._nome

    def seta_nome(self, a_string):
        """ Define o nome do objeto
        """
        if a_string:
            self._nome = a_string
        else:
            raise SyntaxError("Empty name received")


class Blob(ObjetoBlob):

    def __str__(self):
        return "{0} is {1} and leads to [{2}]".format(self._nome, self._is_initial, self._transicoes)

    def __repr__(self):
        return "{0} is {1} and leads to [{2}]".format(self._nome, self._is_initial, self._transicoes)

    def __init__(self):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__(None)
        self._is_initial = False
        self._transicoes = []
        self._acao = lambda blob: print("{0} -> ".format(blob))

    @property
    def inicial(self):
        """ Retorna o tipo do blob.
        """
        return self._is_initial

    def seta_inicial(self, a_boolean):
        """ Seta o tipo do blob. Se inicial aBoolean é true.
        """
        self._is_initial = a_boolean

    def seta_acao(self, a_block):
        """ Seta a ação do blob.
        A ação é executada quando o blob é ativado. a_block recebe como parâmetro o owner.
        """
        if callable(a_block):
            self._acao = a_block
        else:
            raise AssertionError("Must be a lambda or a function")

    def adiciona_transicao(self, uma_transition):
        """ Adiciona uma transicao ao blob. Nenhuma verificação é realizada.
        """
        self._transicoes.append(uma_transition)

    def ativa(self, an_owner):
        """ Realiza a ativação do receptor. O bloco é avaliado no contexto de an_owner.
        """
        return self._acao(an_owner)

    def sensivel_para(self, a_symbol, an_owner):
        """ Retorna true se alguma transição do blob estiver associada ao evento de nome aSymbol e se esta for
            disparável.
            As condições das transições são verificadas no contexto de anOwner.
        """
        answer = False
        for transicao in self._transicoes:
            answer = answer or transicao.disparavel(a_symbol, an_owner)
        return answer

    def transicoes_para(self, a_symbol, an_owner ):
        """
        " Retorna a transição do receptor associada ao evento de nome aSymbol.
        "
        """
        answer = []
        for transicao in self._transicoes:
            if transicao.disparavel(a_symbol, an_owner):
                answer.append(transicao)
        if len(answer) > 1:
            raise AssertionError('Ambiguidade no blob')
        elif len(answer) == 0:
            return None
        else:
            return answer[0]


class BlobNodo(ObjetoBlob):

    def __repr__(self):
        return "{0} is {1} and leads to [{2}]".format(self._name, self._is_initial, self._transitions)

    def __init__(self, *args, **kwargs):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__(*args, **kwargs)
        self._blob_corrente = None
        self._blobs = []

    def adiciona_blob(self, a_blob):
        """
          " Adiciona um blob ao conjunto de blobs do receptor.
            Nenhuma verificação é realizada.
          "
        """
        if isinstance(a_blob, ObjetoBlob):
            self._blobs.append(a_blob)
        else:
            raise AttributeError("Must be sub-class of ObjectoBlob")

    def blob_corrente(self):
        """
           "  Retorna o blob corrente do blob nodo.
              Retorna nil caso não existam blobs correntes.
           "
        """
        return self._blob_corrente

    def seta_blob_corrent(self, a_blob):
        """
           "  Seta o blob corrente do blob nodo.
           "
        """
        if isinstance(a_blob, ObjetoBlob):
            self._blob_corrente = a_blob
        else:
            raise AttributeError("Must be sub-class of ObjectoBlob")
