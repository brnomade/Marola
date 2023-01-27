"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

import unittest
from StateCharts.statecharts import StateChart


class TDDStatecharts(unittest.TestCase):

    def test_case_1(self):
        s = StateChart()
        s.adiciona_blob("#Zero")
        s.adiciona_blob("#One")
        s.adiciona_blob("#Two")
        s.adiciona_blob("#Three")
        s.adiciona_blob("#Four")
        s.conecta_a_com("#Zero", "#One", "#top")
        s.conecta_a_com("#One", "#Two", "#top")
        s.conecta_a_com("#Two", "#Three", "#top")
        s.conecta_a_com("#Three", "#Four", "#top")
        s.seta_estado_inicial("#Zero")
        s.ativa()
        s.ativa_com("#rst")
        print(s)

    def test_case_2(self):
        self.assertEqual(True, False)  # add assertion here
        """
            s := StateChart new.
            s adicionaBlob: #Zero;
            adicionaBlob: #One;
            adicionaBlob: #Two;
            adicionaBlob: #Three;
            adicionaBlob: #Four.
         s conecta: #Zero a: #One com: #top;
            conecta: #One a: #Two com: #top;
            conecta: #Two a: #Three com: #top;
            conecta: #Three a: #Four com: #top.
         s estadoInicial: #Zero.
    
         s adicionaBlob: #None;
            adicionaBlob: #Single;
            adicionaBlob: #Many.
         s conecta: #None a: #None com: #rst;
            conecta: #None a: #Single com: #click;
            conecta: #Single a: #None com: #rst;
            conecta: #Single a: #Many com: #click;
            conecta: #Many a: #None com: #rst.
        s estadoInicial: #None.

         s ativa.
         s ativa: #top!
        """

    def test_case_3(self):
        self.assertEqual(True, False)  # add assertion here
        """
         s := StateChart new.
         s adicionaBlob: #Zero;
            adicionaBlob: #One;
            adicionaBlob: #Two;
            adicionaBlob: #Three;
            adicionaBlob: #Four.
         s conecta: #Zero a: #One com: #top;
            conecta: #One a: #Two com: #top;
            conecta: #Two a: #Three com: #top;
            conecta: #Three a: #Four com: #top;
            conecta: #Four a: #Zero com: #top e: [ : owner | owner ativa: #rst ].
         s estadoInicial: #Zero.
    
         s adicionaBlob: #None;
            adicionaBlob: #Single;
            adicionaBlob: #Many.
         s conecta: #None a: #None com: #rst e: [ : owner | owner ativa: #none ];
            conecta: #None a: #Single com: #click;
            conecta: #Single a: #None com: #rst e: [ : owner | owner ativa: #single ];
            conecta: #Single a: #Many com: #click;
            conecta: #Many a: #None com: #rst e: [ : owner | owner ativa: #many ].
        s estadoInicial: #None.
    
         s ativa.
         #( top click top top top top  ) do: [ : i | s ativa: i ].!
        """

    def test_case_4(self):
        self.assertEqual(True, False)  # add assertion here
        """
        statechart adicionaBlob: #portaAberta;
                      adicionaBlob: #portaFechada;
                      adicionaBlob: #normal;
                      adicionaBlob: #emergencia;
                      adicionaBlob: #esperando;

                      conecta: #portaAberta a: #portaFechada com: #fecha;
                      conecta: #portaFechada a: #portaAberta com: #abre;
                      conecta: #normal a: #emergencia com: #trimOn;
                      conecta: #emergencia a: #normal com: #trimOff;
                      conecta: #esperando a: #esperando com: #andar;

                      estadoInicial: #portaAberta;
                      estadoInicial: #normal;
                      estadoInicial: #esperando.!  !
        """

    def test_case_5(self):
        self.assertEqual(True, False)  # add assertion here
        """
        | s |
    
         s := StateChart new.
         s adicionaBlob: #Zero;
            adicionaBlob: #One;
            adicionaBlob: #Two;
            adicionaBlob: #Three;
            adicionaBlob: #Four.
         s conecta: #Zero a: #One com: #top;
            conecta: #One a: #Two com: #top;
            conecta: #Two a: #Three com: #top;
            conecta: #Three a: #Four com: #top;
            conecta: #Four a: #Zero com: #top e: [ : owner | owner ativa: #rst ].
         s estadoInicial: #Zero.
    
         s adicionaBlob: #None;
            adicionaBlob: #Single;
            adicionaBlob: #Many.
         s conecta: #None a: #None com: #rst e: [ : owner | owner ativa: #none ];
            conecta: #None a: #Single com: #click;
            conecta: #Single a: #None com: #rst e: [ : owner | owner ativa: #single ];
            conecta: #Single a: #Many com: #click;
            conecta: #Many a: #None com: #rst e: [ : owner | owner ativa: #many ].
        s estadoInicial: #None.
    
        s adicionaBlob: #Receive;
           adicionaBlob: #Rnone;
           adicionaBlob: #Rsingle;
           adicionaBlob: #Rmany.
        s conecta: #Receive a: #Rnone com: #none;
           conecta: #Receive a: #Rsingle com: #single;
           conecta: #Receive a: #Rmany com: #many;
           conecta: #Rnone a: #Receive com: #top;
           conecta: #Rsingle a: #Receive com: #top;
           conecta: #Rmany a: #Receive com: #top.
        s estadoInicial: #Receive.
            
        """


if __name__ == '__main__':
    unittest.main()
