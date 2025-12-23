# Cálculo da área de um jardim circular e do valor total a pagar pela grama

import math

# Solicita o raio da área circular:
raio = float(input("Digite o raio do jardim circular (em metros): "))

# Define o preço do metro quadrado da grama:
preco = 25.00

# Calcula a área do círculo:
area = math.pi * math.pow(raio, 2)

# Calcula o valor total:
valor_total = area * preco

# Exibe os resultados:
print(f"\nÁrea total do jardim: {area:.2f} m²")
print(f"O valor total a pagar é: R$ {valor_total:.2f}")
