"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from StateCharts.abstract_statecharts import ObjetoStateChart
from StateCharts.estados import EstadoSimples, EstadoComposto
from StateCharts.transicoes import Transicao


class DiagramaDeEstados(ObjetoStateChart):

    @property
    def imagem(self):
        return "diagrama"

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return False

    def __init__(self):
        super().__init__()
        self._estados = {}
        self._eventos = set()
        self._estados_ativos = []
        self._cliente = None
        self._fila_eventos = []
        self._raiz = 'raiz'
        self._estados.update({self._raiz : EstadoComposto().seta_nome(self._raiz)})

    def adiciona_como_estado(self, a_symbol, a_boolean):
        """
        PRIVADO - Adiciona o estado de nome aSymbol ao dicionario
                         de estados do receptor. aBoolean verdadeiro
                         denota um estado simples. aBoolean falso denota
                         um superestado.
        """
        if not isinstance(a_symbol, str):
            raise AssertionError("Must be a string")

        if self.contem_estado(a_symbol):
            raise AssertionError("Estado {0} ja existente".format(a_symbol))

        if a_boolean:
            novo = EstadoSimples()
        else:
            novo = EstadoComposto()

        novo.seta_nome(a_symbol)
        self._estados.update({novo.nome : novo})

    def adiciona_estado_em(self, a_symbol, outro_symbol):
        """
        Statechart Project - Adiciona o estado de nome aSymbol no superestado
                                          de nome outroSymbol.
                                          Erros são gerados caso:
                                          1. o estado aSymbol já exista.
                                          2. o superestado outroSymbol não exista.
                                          3. outroSymbol não seja um superestado.
        """
        if not isinstance(a_symbol, str):
            raise AssertionError("Must be a string")

        if not isinstance(outro_symbol, str):
            raise AssertionError("Must be a string")

        if not self.contem_estado(outro_symbol):
            raise AssertionError("Estado {0} indefinido".format(outro_symbol))

        if not self.o_estado(outro_symbol).superestado:
            raise AssertionError("Estado {0} nao e superestado".format(outro_symbol))

        self.adiciona_como_estado(a_symbol, True)
        self.o_estado(a_symbol).seta_estado_pai(outro_symbol)
        self.o_estado(outro_symbol).adiciona_estado(a_symbol)

    def adiciona_superestado_em(self, a_symbol, outro_symbol):
        """
        Statechart Project - Adiciona o superestado de nome aSymbol no superestado
                                          de nome outroSymbol.
                                          Erros são gerados caso:
                                          1. o estado aSymbol já exista.
                                          2. o superestado outroSymbol não exista.
                                          3. outroSymbol não seja um superestado.
        """
        if not isinstance(a_symbol, str):
            raise AssertionError("Must be a string")

        if not isinstance(outro_symbol, str):
            raise AssertionError("Must be a string")

        if not self.contem_estado(outro_symbol):
            raise AssertionError("Estado {0} indefinido".format(outro_symbol))

        if not self.o_estado(outro_symbol).superestado:
            raise AssertionError("Estado {0} nao e superestado".format(outro_symbol))

        self.adiciona_como_estado(a_symbol, False)
        self.o_estado(a_symbol).seta_estado_pai(outro_symbol)
        self.o_estado(outro_symbol).adiciona_estado(a_symbol)

    def altera_estado_para(self, old_symbol, new_symbol):
        """
        " Statechart Project - Altera o nome do estado aSymbol para anotherSymbol.

                                       Etapas
                                       1. altero nome do estado.
                                       2. altero referência no dicionário de estados.
                                       3. para cada estado nodo altero referência ao estado.
                                       4. para as transicao de cada estado altero as referências ao estado.

        "
        """

        if not isinstance(old_symbol, str):
            raise AssertionError("Must be a string")

        if not isinstance(new_symbol, str):
            raise AssertionError("Must be a string")

        if self.contem_estado(new_symbol):
            raise AssertionError("O Estado de nome {0} ja existe no diagrama".format(new_symbol))

        estado = self.o_estado(old_symbol)
        # etapa 1
        estado.seta_nome(new_symbol)
        # etapa 2
        for nome_estado in self.todos_os_estados():
            estado = self.o_estado(nome_estado)
            "etapa 3. O erro esta no bloco seguinte..."
            if isinstance(estado, EstadoComposto):
                if estado.contem_estado(old_symbol):
                    estado.remove_subestado(old_symbol)
                    estado.adiciona_estado(new_symbol)
            "etapa 4."
            for transicao in estado.transicoes():
                transicao.altera_estado_para(old_symbol, new_symbol)

    def ativa(self):
        """
        Statechart Project - Ativa o receptor.
                              Os estados iniciais são colocados na lista de estadosAtivos.
                              Suas ações são executadas
        """
        self._estados_ativos = []
        for estado in self._estados.values():
            if estado.inicial:
                self._estados_ativos.append(estado.nome)
                estado.ativa_estado(self)

        if not self._estados_ativos:
            raise AssertionError('Nenhum estado inicial definido no diagrama')

    def atividade_do_estado(self, a_symbol, another_symbol):
        """
        Statechart Project - Associa atividades aos estados.
        """
        self.o_estado(another_symbol).seta_atividade(a_symbol)

    @property
    def cliente(self):
        """ Statechart Project - Retorna o cliente do receptor.
        """
        return self._cliente

    def seta_cliente(self, an_object):
        """ Statechart Project - Seta o cliente do receptor.
        """
        self._cliente = an_object

    def conecta_a_com_e_executando_caso(self, origem_symbol, destino_symbol, evento_symbol, evento_colateral_symbol, acao_symbol, condicao_symbol):
        """
        " Statechart Project - Conecta o estado origem de nome aSymbol com o estado destino
                                            de nome otherSymbol. A Transicao criada é associada ao evento
                                            de nome anotherSymbol. acaoSymbol é definido como a ação
                                            da transição
        "
        """
        self.conecta_a_com_executando_caso(origem_symbol, destino_symbol, evento_symbol, acao_symbol, condicao_symbol)

    def conecta_a_com_executando_caso(self, origem_symbol, destino_symbol, evento_symbol, acao_symbol, condicao_symbol):
        """
        " Statechart Project - Conecta o estado origem de nome aSymbol com o estado destino
                                            de nome otherSymbol. A Transicao criada é associada ao evento
                                            de nome anotherSymbol. acaoSymbol é definido como a ação
                                            da transição
        "
        """
        origem = self.o_estado(origem_symbol)
        destino = self.o_estado(destino_symbol)

        transicao = Transicao()
        transicao.seta_evento(evento_symbol)
        transicao.seta_destino(destino_symbol)
        transicao.seta_origem(origem_symbol)
        transicao.seta_acao(acao_symbol)
        transicao.seta_condicao(condicao_symbol)

        origem.adiciona_transicao(transicao)

        self._eventos.add(evento_symbol)

    def contem_estado(self, a_symbol):
        """ Statechart Project - Retorna true se o estado aSymbol já existe no receptor.
        """
        return a_symbol in self._estados.keys()

    def seta_estado_default(self, a_symbol, a_boolean=True):
        """ Statechart Project - Configura o atributo de estado default para o estado
                                        existente no receptor de nome aSymbol.
        """
        self.o_estado(a_symbol).seta_default(a_boolean)

    def seta_estado_inicial(self, a_symbol, a_boolean=True):
        """ Statechart Project - Configura o atributo de estado inicial para o estado
                                        existente no receptor de nome aSymbol.
        """
        self.o_estado(a_symbol).seta_inicial(a_boolean)

    def estado_ativo(self, a_symbol):
        """ Statechart Project - Retorna true se o estado de nome aSymbol está incluído
                                      no conjunto de estadosAtivos.
                                      Provoca um erro caso o estado não seja definido.
        """
        return a_symbol in self._estados_ativos

    def estados_ativos(self):
        """ Statechart Project - Retorna uma lista com todos os estadosAtivos.
        """
        return self._estados_ativos.copy()

    @property
    def estado_raiz(self):
        """ Statechart Project - Retorna o estado raiz do statechart.
        """
        return self.o_estado(self._raiz)

    def evento(self, a_symbol):
        """
        " Statechart Project - O receptor recebe o evento de nome aSymbol.
                                           Caso o evento ocorrido não seja suportado retorna self.
                                           Todos os estados ativos são testados.
                                           Transições habilitadas são disparadas, e suas ações correspondentes
                                           executadas no contexto do cliente.
                                           Os estados alcançados tem suas atividades executadas.
        "
        """
        if not isinstance(a_symbol, str):
            raise AssertionError('must be string')

        if a_symbol not in self._eventos:
            return False

        disparou = False
        destinos = set()
        #novo_estados_ativos = []

        for i in self._estados_ativos:
            transicao = self.o_estado(i).transicao_para(a_symbol, self)
            if transicao:
                destino = self.o_estado(transicao.dispara(self))
                destinos.add(destino)
                if isinstance(destino, EstadoComposto):
                    for j in destino.estados_default(self):
                        destinos.add(self.o_estado(j))
            else:
                # não houve transição para este estado
                destinos.add(self.o_estado(i))

        for estado in destinos:
            estado.ativa(self)


        self._
        if len(self._fila_eventos) > 0:
            self.seta_evento(self._fila_eventos.pop(0))

        return disparou

    def existe_estado(self, a_symbol):
        """ Statechart Project - Retorna true se o estado já existe no statechart.
        """
        if isinstance(a_symbol, str):
            return a_symbol in self._estados.keys()
        else:
            raise AssertionError('must be a string')

    def existe_superestado(self, a_symbol):
        """ Statechart Project - Retorna true se o estado já existe no statechart.
        """
        if isinstance(a_symbol, str):
            if self.existe_estado(a_symbol):
                return isinstance(self.o_estado(a_symbol), EstadoComposto)
            else:
                return False
        else:
            raise AssertionError('must be a string')

    def inclue_estado(self, a_symbol):
        """  Statechart Project - Retorna true se o estado já existe no statechart.
        """
        # TODO - not sure this code is actually needed
        """
             (estados includesKey: aSymbol)
             ifTrue:[ MessageBox message: ' O Estado de nome ''', aSymbol asString, ''' já existe no diagrama!!'.
                  ^true
               ].
     ^false.!
     """

    def inclue_superestado(self, a_symbol):
        """  Statechart Project - Retorna true se o superestado já existe no statechart.
        """
        # TODO - not sure this code is actually needed
        """
           | estado |

         estado := self oEstado: aSymbol.
        (estado isKindOf: Superestado)
        ifFalse:[ MessageBox message: 'Superestado ', aSymbol asString, ' inexistente'.
                   ^false
                 ].
        ^true.!
        """

    @property
    def raiz(self):
        """
        Statechart Project - Retorna o nome da raiz do statechart.
        """
        return self._raiz

    def seta_nome_raiz(self, a_symbol):
        """
        Statechart Project - Seta o nome do statechart.
        """
        if isinstance(a_symbol, str):
            if a_symbol:
                if self._raiz != a_symbol:
                    if self.contem_estado(a_symbol):
                        raise AssertionError("Estado {0} ja existente no diagrama".format(a_symbol))
                    else:
                        estado = self._estados.pop(self._raiz)
                        estado.seta_nome(a_symbol)
                        self._raiz = a_symbol
                        self._estados.update({estado.nome: estado})
            else:
                raise SyntaxError("Empty name received")
        else:
            raise AssertionError("Must be string")

    def o_estado(self, a_symbol):
        """ Statechart Project - Retorna o estado de nome aSymbol.
                                Caso não exista provoca um erro de execução.
        """
        if isinstance(a_symbol, str):
            if a_symbol in self._estados.keys():
                return self._estados.get(a_symbol)
            else:
                raise AssertionError("Estado {0} inexistente.".format(a_symbol))
        else:
            raise AssertionError('must be a string')

    def todos_os_estados(self):
        """
        " Statechart Project - Retorna uma colecao com o nome de todos os
                                      estados existentes no diagrama.

        "
        """
        return self._estados.keys()

    def todos_os_eventos(self):
        """
        " Statechart Project - Retorna uma colecao com o nome de todos os eventos
                                       utilizados no diagrama.

        "
        """
        return self._eventos.copy()

    def transicao(self, a_symbol):
        pass

