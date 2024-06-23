print('{:=^40} '.format(" Cálculo do Combustível "))

dp = float(input("Distância percorrida: "))
cmd = float(input("Consumo médio do veículo: "))
pl = float(input("Preço por litro: "))

c = dp / cmd
print(f"o consumo do seu veiculo será de {c:.2f}km/l")  

pk = pl * dp
print(f"Você vai gastar R${pk} com o combustivel")
