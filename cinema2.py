# Inicializa a matriz do cinema com True (indicando assentos livres)
cinema = [[True for _ in range(4)] for _ in range(4)]

#menu de interação
def menu(cinema):
    while True:
        print ('''
[ 1 ] Mostrar assentos
[ 2 ] Escolher assento 
[ 3 ] Excluir reserva 
[ 0 ] Sair''')
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 1:
            mostrar_assentos(cinema)
        elif opcao == 2:
            escolher_assento(cinema)
        elif opcao == 3:
            excluir_reserva(cinema)
        elif opcao == 0:
            print('Saindo do programa.')
            break
        else:
            print('Opção inválida! Tente novamente.')

def mostrar_assentos(cinema):
    print('Assentos: (💺 = Livre | ✅ = Reservado)\n')
    for l in range(len(cinema)):
        fila = ['💺' if assento else '✅' for assento in cinema[l]]
        print(f'Fileira {l + 1}: {fila}')

def escolher_assento(cinema):
    while True:
        mostrar_assentos(cinema)
        fila = int(input('\nEscolha a fileira de 1 a 5 ou aperte 0 para sair: ')) - 1
        if fila == -1:
            break
        coluna = int(input('\nEscolha o número do assento 1 a 5: ')) - 1

        # Verifica se a escolha está dentro dos limites
        if 0 <= fila < len(cinema) and 0 <= coluna < len(cinema[fila]):
            if cinema[fila][coluna]: 
                print('Assento reservado com sucesso! ✅ ')
                cinema[fila][coluna] = False  # Reserva o assento
            else:
                print('Assento já está reservado! ❌ ')
        else:
            print('Escolha inválida! Tente novamente.')

def excluir_reserva(cinema):
    while True:
        mostrar_assentos(cinema)
        fila = int(input('\nCancelar reserva, escolha a fileira  de 1 a 5 ou aperte 0 para sair: ')) - 1
        if fila == -1:
            break
        coluna = int(input('\nEscolha o  assento  que deseja para cancelar: ')) - 1

        # Verifica se a escolha está dentro dos limites
        if 0 <= fila < len(cinema) and 0 <= coluna < len(cinema[fila]):
            if not cinema[fila][coluna]:  # O assento está reservado (False)
                print('Reserva excluída com sucesso! ❌ ')
                cinema[fila][coluna] = True  # Libera o assento (tornado True)
            else:
                print('Este assento não estava reservado!')
        else:
            print('Escolha inválida! Tente novamente.')


menu(cinema)

