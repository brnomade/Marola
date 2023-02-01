"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from StateCharts.blobs import Blob
from StateCharts.transicoes import Transicao


class ObjetoStateChart:

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return True

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
    def imagem(self):
        """ StateChart Project - Retorna a imagem do blob
        """
        raise NotImplementedError('Must be implemented by subclass')

    @property
    def image_padrao(self):
        """
            " StateChart Project - Retorna a imagem do blob
            "
        """
        # ^MarolaIcons bitmapNamed: self.image()
        return self.imagem

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


class StateChart(ObjetoStateChart):

    def __init__(self):
        super().__init__(self.__class__.__name__ + '#' + str(hash(self)))
        self._blobs = {}
        self._eventos = []
        self._blob_ativos = []
        self._dono = None

    @property
    def owner(self):
        """
        " Retorna o dono do receptor.
        "
        """
        return self._dono

    def seta_owner(self, an_object):
        """
        " Seta o dono do receptor.
        "
        """
        self._dono = an_object

    def seta_estado_inicial(self, a_symbol):
        """
        " Define os blobs iniciais
        "
        """
        if a_symbol not in self._blobs.keys():
            raise AssertionError('Estado inexistente')
        self._blobs.get(a_symbol).seta_inicial(True)

    def adiciona_blob(self, a_symbol):
        """
        " Se aSymbol não existe no dicionário de blobs significa que devo criar um
        novo blob do tipo simples (estado).
        "
        """
        if a_symbol not in self._blobs.keys():
            blob = Blob()
            blob.seta_nome(a_symbol)
            self._blobs.update({a_symbol: blob})
        else:
            raise AssertionError('Blob already exists.')

    def conecta_a_com(self, a_symbol, other_symbol, another_symbol):
        """
        " Conecta o blob origem de nome aSymbol com o blob destino
           de nome otherSymbol. A Transicao criada é associada ao evento
           de nome anotherSymbol
        "
        """
        if a_symbol not in self._blobs.keys():
            raise AssertionError('Blob origem inexistente')

        if other_symbol not in self._blobs.keys():
            raise AssertionError('Blob destino inexistente')

        blob = self._blobs.get(a_symbol)
        transicao = Transicao()
        transicao.seta_evento(another_symbol)
        transicao.seta_destino(other_symbol)
        blob.adiciona_transicao(transicao)
        self._eventos.append(another_symbol)

    def conecta_a_com_e(self, a_symbol, other_symbol, another_symbol, a_block):
        """
        " Conecta o blob origem de nome aSymbol com o blob destino
        de nome otherSymbol. A Transicao criada é associada ao evento
        de nome anotherSymbol. O bloco aBlock é definido como a ação
        da transição.
        "
        """
        if a_symbol not in self._blobs.keys():
            raise AssertionError('Blob origem inexistente')

        if other_symbol not in self._blobs.keys():
            raise AssertionError('Blob destino inexistente')

        blob = self._blobs.get(a_symbol)
        transicao = Transicao()
        transicao.seta_evento(another_symbol)
        transicao.seta_destino(other_symbol)
        transicao.seta_acao(a_block)
        blob.adiciona_transicao(transicao)
        self._eventos.append(another_symbol)

    def acao_do_blob(self, a_block, a_symbol):
        """
        """
        if a_symbol not in self._blobs.keys():
            raise AssertionError('Blob inexistente')
        blob = self._blobs.get(a_symbol)
        blob.seta_acao(a_block)

    def ativa(self):
        """
        " Ativa o receptor. Os estados iniciais são colocados na
           lista de blobsAtivos. Suas ações são executadas
        "
        """
        self._blob_ativos = []
        for blob in self._blobs.values():
            if blob.inicial:
                blob.ativa_estado(self)
                self._blob_ativos.append(blob)
        if not self._blob_ativos:
            raise AssertionError('Nenhum estado inicial definido')

    def ativa2(self, a_symbol):
        """
           " Ativa o receptor com o evento de nome aSymbol.
             Caso o evento ocorrido não seja suportado pelo receptor simplesmente
             retorna self.
             Todos os estados ativos são testados. Transições habilitadas são
             disparadas, e suas ações correspondentes executadas no contexto do
             dono. Os estados alcançados tem suas ações executadas.
           "
        """
        # TODO: Como implementar Symbol mustBeSymbol: aSymbol.
        if a_symbol not in self._eventos:
            return self

        novos_ativos = []
        for blob in self._blob_ativos:
            transicao = blob.transicoes_para(a_symbol, self)
            if not transicao:
                novos_ativos.append(blob)
            else:
                destino = self._blobs.get(transicao.dispara(self))
                destino.ativa(self)
                novos_ativos.append(destino)
        self._blob_ativos = novos_ativos

    def ativa_com(self, a_symbol):
        """
         " Ativa o receptor com o evento de nome aSymbol.
         Caso o evento ocorrido não seja suportado pelo receptor simplesmente
         retorna self.
         Todos os estados ativos são testados. Transições habilitadas são
         disparadas, e suas ações correspondentes executadas no contexto do
         dono. Os estados alcançados tem suas ações executadas.
         "
        """
        # TODO: Como implementar Symbol mustBeSymbol: aSymbol.
        if a_symbol not in self._eventos:
            return self

        novo_blobs_ativo = []
        for blob in self._blob_ativos:
            # this is not required: blob := blobsAtivos removeFirst.
            transicao = blob.transicoes_para(a_symbol, self)
            if not transicao:
                novo_blobs_ativo.append(blob)
            else:
                destino = self._blobs.get(transicao.dispara(self))
                novo_blobs_ativo.append(destino)
                destino.ativa(self)
        self._blob_ativos = novo_blobs_ativo



