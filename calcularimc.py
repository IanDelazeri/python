
print('Calcule seu IMC')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.6 <= imc < 24.9:
    print('Você está com o peso ideal')
elif 25 <= imc < 29.9:
    print('Você está levemente acima do peso')
elif 30 <= imc < 34.9:
    print('Você está com obesidade grau I')
elif 35 <= imc < 39.9:
    print('Você está com obesidade grau II')
elif imc >= 40:
    print('Você está com obesidade grau III')
