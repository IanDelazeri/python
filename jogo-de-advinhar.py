from random import randint
from time import sleep
print('='*20)
computador =randint(0, 1)
print('Vou pensar em um numero entre 0 e 1. tente advinhar...')
jogador = int(input('Em que numero estou pensando? '))
print('='*20)
print('PROCESSANDO....')
print('='*20)
sleep(2)
if computador == jogador:
    print('Parabens!!!, Você me venceu. ')
else:
    print(f'Ganhei!!! pensei no numero {computador} e não no numero {jogador}')

