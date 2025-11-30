dolar = 5.34

input_valor = input("Quanto voce tem em reais? R$ ")
valor_reais = float(input_valor)
valor_dolar = valor_reais / dolar

print(f"Com R$ {valor_reais:.2f}, voce pode comprar US$ {valor_dolar:.2f}.")