import random

def inicializar():
    print('Cara (1) - Coroa (2) - Sair (0)')
    return input('Escolha: ')

def testar_lancar(cara_ou_coroa, escolha):
    if escolha == "0":
        print('Jogo encerrado.')
        return False

    resultado = 'Cara' if cara_ou_coroa == 1 else 'Coroa'
    escolha_texto = 'Cara' if escolha == '1' else 'Coroa'

    if cara_ou_coroa == int(escolha):
        print(f'Você ganhou, deu {resultado}!')
    else:
        print(f'Você perdeu, deu {resultado}. Você escolheu {escolha_texto}.')
    print()

def testa_lancar_valido():
    while True:
        escolha = inicializar()
        if escolha in {'0', '1', '2'}:
            return escolha
        else:
            print(f'{escolha} não é uma opção válida. Escolha novamente.\n')

# Loop principal do jogo
while True:
    escolha = testa_lancar_valido()
    if not testar_lancar(random.randint(1, 2), escolha):
        break