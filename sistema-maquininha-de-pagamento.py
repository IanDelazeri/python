print('{:=^40} '.format(' LOJA BOA VENDA '))
preço = float(input('preço das compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista dinheiro cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input(' qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção ==3:
    total = preço + (preço * 5 / 100)   
    parcela = total / 2
    print('sua compra será parcelada em 2x de   R${:.2f} SEM JUROS!!  ' .format(parcela))    
elif opção == 4:
     total = preço + (preço * 20 / 100)    
     totparc = int(input('quantas parcelas? '))
     parcela = total / totparc
     print('sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(totparc, parcela ))
else:
    total = 0 
    print('OPÇÃO INVALIDA de pagamento. Tente Novamente! ') 
print('Sua compra de R${:.2f} vai custar R${:.2f} no final ' .format(preço, total))