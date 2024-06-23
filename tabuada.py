while True:
    print('''Escolha a uma opção abaixo
    [ 1 ] Multiplicação
    [ 2 ] Divisão
    [ 3 ] Adição
    [ 4 ] Subtração
    [ 5 ] Sair''')

    opção = int(input("Digite a opção que deseja: "))
    
    if opção == 5:

        print('''
        ============
        Saindo...
        ============''')
        break

    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))

    if opção == 1: 
        total = n1 * n2
        print("Multiplicação")
    elif opção == 2:
        total = n1 / n2
        print("Divisão")
    elif opção == 3:
        total = n1 + n2
        print("Adição")
    elif opção == 4:
        total = n1 - n2
        print("Subtração")
    else:
        total = 0 
        print("OPÇÃO INVÁLIDA. Tente Novamente! ")

    print(f'''======================
    O resultado é {total}\n======================''')
