"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from statecharts import ObjetoStateChart


class Blob(ObjetoStateChart):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __str__(self):
        return "({0}){1}:{2} > [{3}]".format( self.__class__.__name__, self._nome, self._is_initial, self._transicoes)

    def __repr__(self):
        return "({0}){1}:{2} > [{3}]".format( self.__class__.__name__, self._nome, self._is_initial, self._transicoes)

    def __init__(self):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__(None)
        self._is_initial = False
        self._is_default = False
        self._transicoes = []

    @property
    def inicial(self):
        """ StateChart Project - Retorna o tipo do blob.
        """
        return self._is_initial

    @property
    def default(self):
        """ StateChart Project - Retorna se o receptor é um estado default.
        """
        return self._is_default

    @property
    def superestado(self):
        """ StateChart Project - Retorna verdadeiro se o receptor é um superestado.
        """
        return False

    def superestado_de(self, um_blob):
        """ StateChart Project - Retorna verdadeiro se o receptor é um superestado de umBlob.
        """
        return False

    def seta_inicial(self, a_boolean):
        """ StateChart Project - Seta o tipo do blob. Se inicial aBoolean é true.
        """
        self._is_initial = a_boolean

    def seta_default(self, a_boolean):
        """ StateChart Project - Seta o se o receptor é estado default.
        """
        self._is_default = a_boolean

    def adiciona_transicao(self, uma_transition):
        """ StateChart Project - Adiciona uma transicao ao blob. Nenhuma verificação é realizada.
        """
        self._transicoes.append(uma_transition)

    def remove_transicao(self, uma_transition):
        """ StateChart Project - Remove a transicao do blob.
        """
        self._transicoes.remove(uma_transition)

    def transicoes(self):
        """ StateChart Project - Retorna uma colecao com as transicoes conectadas ao blob.
        """
        return self._transicoes


class BlobNodo(Blob):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __init__(self, *args, **kwargs):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__(*args, **kwargs)
        # self._blob_corrente = None
        self._blobs = []
        self._blob_ativo = None

    @property
    def imagem(self):
        """ StateChart Project - Retorna a imagem do blob
        """
        return "blobnodo"

    def adiciona_blob(self, a_symbol):
        """
          " StateChart Project - Adiciona o blob de nome aSymbol ao blob receptor.
          "
        """
        self._blobs.append(a_symbol)

    def remove_blob(self, a_symbol):
        """
          " StateChart Project - Remove o blob de nome aSymbol.
          "
        """
        if a_symbol in self._blobs:
            self._blobs.remove(a_symbol)

    def ativa(self, a_statechart):
        """ StateChart Project - Ativa o receptor.
                                 Devo ativar meu sub estado inicial. Somente um sub estado
                                 ativo pode existir a cada instante.
        """
        blobs_ativos = []
        for nome_blob in self._blobs:
            if a_statechart.blob(nome_blob).is_default:
                blobs_ativos.append(nome_blob)

        if not blobs_ativos:
            raise AssertionError('Nenhum sub-estado default definido')
        elif len(blobs_ativos) > 1:
            raise AssertionError('Ambiguidade nos sub-estados')

        self._blob_ativo = blobs_ativos.pop(0)
        a_statechart.seta_blob(self._blob_ativo)
        self._blob_ativo.ativa(a_statechart) # TODO - esta linha esta provavelmente incorreta - original     (aStatechart blob: blobAtivo) ativa: aStatechart.

    def ativa_blob_em(self, a_symbol, a_statechart):
        """ StateChart Project - Define o blob de nome aSymbol como o blob
        ativo no superestado receptor
        """
        if a_symbol in self._blobs:
            # o blob de nome aSymbol está contido no receptor "
            self._blob_ativo = a_symbol
        else:
            # o blobAtivo do receptor é um superestado que pode conter o blob de nome aSymbol "
            # TODO - needs checking -> (aStatechart blob: blobAtivo) ativaBlob: aSymbol em: aStatechart.
            a_statechart.blob(self._blob_ativo).ativa_blob_em(a_symbol, a_statechart)

    def contem_blob(self, a_symbol):
        """
        StateChart Project - Informa se o blob receptor contém o blob de nome aSymbol.
        """
        return a_symbol in self._blobs

    def nome_dos_blobs(self):
        """
        StateChart Project - Retorna o nome de todos os blobs contidos no
                                          blob nodo.
        """
        return self._blobs

    @property
    def superestado(self):
        """ StateChart Project - Retorna verdadeiro se o receptor é um superestado.
        """
        return True

    def superestado_de(self, um_blob):
        """ StateChart Project - Retorna verdadeiro se o receptor é um superestado de umBlob.
        """
        return False

    def transicao_para(self, a_symbol, a_statechart):
        """
        StateChart Project - Retorna as transições do blobAtivo junto com as
                           transições do receptor associadas ao evento de
                           nome aSymbol.
        """
        answer = []
        sub_blobs = []

        for transicao in self._transicoes:
            if transicao.disparavel_para(a_symbol, a_statechart):
                answer.append(transicao)

        sub_blobs = a_statechart.blob(self._blob_ativo).transicao_para(a_symbol, a_statechart)
        if sub_blobs:
            answer.append(sub_blobs)

        if len(answer) > 1:
            raise AssertionError('Ambiguidade no blob')
        elif len(answer) == 0:
            return None
        else:
            return answer[0]

    # def blob_corrente(self):
    #     """
    #        "  Retorna o blob corrente do blob nodo.
    #           Retorna nil caso não existam blobs correntes.
    #        "
    #     """
    #     return self._blob_corrente
    #
    # def seta_blob_corrent(self, a_blob):
    #     """
    #        "  Seta o blob corrente do blob nodo.
    #        "
    #     """
    #     if isinstance(a_blob, ObjetoBlob):
    #         self._blob_corrente = a_blob
    #     else:
    #         raise AttributeError("Must be sub-class of ObjectoBlob")


class BlobSimples(Blob):

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __init__(self, *args, **kwargs):
        """
            transitions : lista que contém todas as transições que partem de self.
        """
        super().__init__(*args, **kwargs)
        self.nome("#nil")
        self._acao = None

    @property
    def imagem(self):
        """ StateChart Project - Retorna a imagem do blob
        """
        if self._is_initial:
            return "blobi"
        else:
            return "blob"

    @property
    def acao(self):
        """ StateChart Project - Retorna o símbolo associado a acao do blob.
        """
        return self._acao

    def seta_acao(self, a_symbol):
        """ StateChart Project - Seta o símbolo associado a acao do blob.
                                O símbolo recebe o statechart como parâmetro.
                                A ação é executada quando o estado é alcançado.
        """
        if isinstance(a_symbol, str):
            self._acao = a_symbol
        else:
            raise AssertionError('Must be a string')

    @property
    def acao_ativa(self):
        """
            " StateChart Project - Statechart Project -  Retorna se a acao é valida.
            "
        """
        return self._acao != "#nil"

    def ativa(self, a_statechart):
        """  StateChart Project - Ativa o receptor.
                                  O bloco é avaliado no contexto do StateChart.

        """
        print("B.{0}".format(self._nome))
        if self.acao_ativa:
            a_statechart.client.perform_with_arguments(self._acao, [a_statechart])

    def sensivel_para(self, a_symbol, a_statechart):
        """ StateChart Project - Retorna true se alguma transição do blob estiver
                                         associada ao evento de nome aSymbol e se esta
                                         for disparável.  As condições das transições são
                                         verificadas no contexto do aStateChart.
        """
        answer = False
        for transicao in self._transicoes:
            answer = answer or transicao.disparavel(a_symbol, a_statechart)
        return answer

    def transicao_para(self, a_symbol, a_statechart):
        """
        " StateChart Project - Retorna a transição do receptor associada ao evento de
                                           nome aSymbol.
        "
        """
        answer = []
        for transicao in self._transicoes:
            if transicao.disparavel(a_symbol, a_statechart):
                answer.append(transicao)
        if len(answer) > 1:
            raise AssertionError('Ambiguidade no blob')
        elif len(answer) == 0:
            return None
        else:
            return answer[0]

