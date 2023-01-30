"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""


class ObjetoStateChart:

    @classmethod
    def classe_abstrata(cls):
        """
        " Marola Framework - Código automático de consulta ao tipo da classe.
        Retorna true se a classe for abstrata.
        """
        return True

    def __init__(self):
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
