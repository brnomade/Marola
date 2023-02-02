"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

from abc import ABC, abstractmethod
from datetime import datetime
import random


class ObjetoStateChart(ABC):

    @classmethod
    @abstractmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata, false caso-contrario.
        """
        pass

    def __str__(self):
        return "{0}".format(self._nome)

    def __repr__(self):
        return "{0}".format(self._nome)

    def __init__(self):
        self._nome = "{0}#{1}.{2}".format(self.__class__.__name__,
                                          datetime.timestamp(datetime.now()),
                                          random.randint(0, 65535))

    @property
    @abstractmethod
    def imagem(self):
        """ StateChart Project - Retorna o nome da imagem do blob
        """
        pass

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

    def seta_nome(self, a_symbol):
        """ Define o nome do objeto
        """
        if isinstance(a_symbol, str):
            if a_symbol:
                self._nome = a_symbol
            else:
                raise SyntaxError("Empty name received")
        else:
            raise AssertionError("Must be string")
        return self
