from Lib.Interface import *
from Lib.Fases import *
from time import sleep
cabecalho('Jogo de Adivinhação de Números')
sleep(1)
explicação()
sleep(5)
cabecalho('1° FASE')
n1 = fase(7)
if not n1:
    print('Você \033[31mperdeu\033[m o jogo, infelismente. Mas, volte sempre!')
cabecalho('2° FASE')
sleep(1)
n1 = fase(15)
if not n1:
    print('Você \033[31mperdeu\033[m o jogo, infelismente. Mas, volte sempre!')
cabecalho('3° FASE')
sleep(1)
n1 = fase(25)
if not n1:
    print('Você \033[31mperdeu\033[m o jogo, infelismente. Mas, volte sempre!')
cabecalho('4° FASE')
sleep(1)
n1 = fase(30)
if not n1:
    print('Você \033[31mperdeu\033[m o jogo, infelismente. Mas, volte sempre!')
cabecalho('ÚLTIMA FASE')
sleep(1)
n1 = fase(45, ultima=True)
if not n1:
    print('Você \033[31mperdeu\033[m o jogo, infelismente. Mas, volte sempre!')
print('Finalizando...')
