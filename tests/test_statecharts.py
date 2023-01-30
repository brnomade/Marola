"""
PROJECT.......: Marola
COPYRIGHT.....: Copyright (C) 2023- Andre L Ballista
DESCRIPTION...: A Python based reimplementation of the original Smalltalk Marola framework
HOME PAGE.....: https://github.com/brnomade/Marola
"""

import unittest
from StateCharts.statecharts import StateChart


class TDDStatecharts(unittest.TestCase):

    @staticmethod
    def test_case_1():
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

        s.adiciona_blob("#None")
        s.adiciona_blob("#Single")
        s.adiciona_blob("#Many")
        s.conecta_a_com("#None", "#None", "#rst")
        s.conecta_a_com("#None", "#Single", "#click")
        s.conecta_a_com("#Single", "#None", "#rst")
        s.conecta_a_com("#Single", "#Many", "#click")
        s.conecta_a_com("#Many", "#None", "#rst")
        s.seta_estado_inicial("#None")

        s.ativa()
        s.ativa_com("#top")
        print(s)

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

    def test_case_6(self):
        self.assertEqual(True, False)  # add assertion here
        """
               | s |

       s := Statechart new.           
       s adicionaBlobNodo: #n1 em: #raiz;
          adicionaBlob: #e1 em: #n1;
          adicionaBlob: #e2 em: #n1;
          adicionaBlobNodo: #n2 em: #raiz;
          adicionaBlob: #e3 em: #n2;
          adicionaBlob: #e4 em: #n2;
          estadoDefault: #e1;    
          estadoDefault: #e3; 
          conecta: #e1 a: #e2 com: #clic executando: #nil caso: #true;
          conecta: #e2 a: #e1 com: #clac executando: #nil caso: #true;
          conecta: #e3 a: #e4 com: #clic executando: #nil caso: #true;
          conecta: #e4 a: #e3 com: #clac executando: #nil caso: #true;
          conecta: #n1 a: #n2 com: #vai executando: #nil caso: #true;
          conecta: #n2 a: #n1 com: #vem executando: #nil caso: #true;
         estadoInicial: #n1.
       s inspect.
        """

    def test_case_7(self):
        self.assertEqual(True, False)  # add assertion here
        """
       | s |

       s := DiagramaDeEstados new.           
       s adicionaSuperestado: #n1 em: #raiz;
          adicionaEstado: #e1 em: #n1;
          adicionaEstado: #e2 em: #n1;
          adicionaSuperestado: #n2 em: #raiz;
          adicionaEstado: #e3 em: #n2;
          adicionaEstado: #e4 em: #n2;
          estado: #e1 default: true;    
          estado: #e3 default: true; 
          conecta: #e1 a: #e2 com: #clic executando: #nil caso: #true;
          conecta: #e2 a: #e1 com: #clac executando: #nil caso: #true;
          conecta: #e3 a: #e4 com: #clic executando: #nil caso: #true;
          conecta: #e4 a: #e3 com: #clac executando: #nil caso: #true;
          conecta: #n1 a: #n2 com: #vai executando: #nil caso: #true;
          conecta: #n2 a: #n1 com: #vem executando: #nil caso: #true;
         estado: #n1 inicial: true.
       s inspect.

        """

    def test_case_8(self):
        self.assertEqual(True, False)  # add assertion here
        """
           | s |

       s := DiagramaDeEstados new.
       s adicionaEstado: #A em: #raiz;
          adicionaSuperestado: #B em: #raiz;
          adicionaSuperestado: #C em: #B;
          adicionaEstado: #D em: #B;
          adicionaEstado: #E em: #C;
          adicionaEstado: #F em: #C;
          adicionaEstado: #G em: #C;
          estado: #A default: true;
          estado: #B default: true;
          estado: #C default: true;
          estado: #F default: true;
          estado: #G default: true;
          conecta: #A a: #B com: #t1 executando: #nil caso: #true;
          conecta: #B a: #A com: #t2 executando: #nil caso: #true;
          conecta: #C a: #D com: #t3 executando: #nil caso: #true;
          conecta: #D a: #C com: #t4 executando: #nil caso: #true;
          conecta: #E a: #F com: #t5 executando: #nil caso: #true;
          conecta: #F a: #E com: #t6 executando: #nil caso: #true;
          conecta: #G a: #G com: #t7 executando: #nil caso: #true;
          estado: #A inicial: true.
         s inspect.

        """

    def test_case_9(self):
        self.assertEqual(True, False)  # add assertion here
        """
     | d |

     d := DiagramaDeEstados new.
     d adicionaEstado: #A em: #raiz;
        adicionaSuperestado: #E em: #raiz;  
        adicionaSuperestado: #B em: #E;
        adicionaEstado: #C em: #B;
        adicionaEstado: #D em: #B.
     d conecta: #A a: #E com: #x executando: #nil caso: #true;
        conecta: #E a: #A com: #x executando: #nil caso: #true;
        conecta: #C a: #D com: #y executando: #nil caso: #true;    
        conecta: #D a: #C com: #z executando: #nil caso: #true.
     d estado: #A default: true;
        estado: #A inicial: true;
        estado: #C default: true;
        estado: #B default: true.
   
     

        """


if __name__ == '__main__':
    unittest.main()
