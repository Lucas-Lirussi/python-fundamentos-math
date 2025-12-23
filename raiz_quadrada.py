# Cálculo da raiz quadrada de uma lista de números
# e verificação de quais possuem raiz inteira

import math

# Lista de números que serão processados:
numeros = [2, 8, 15, 23, 91, 112, 256]

# Percorre cada número da lista:
for numero in numeros:
    # Calcula a raiz quadrada:
    raiz = math.sqrt(numero)

    # Arredonda o resultado para até 2 casas decimais (apenas para exibição):
    raiz_arredondada = round(raiz, 2)

    print(f"Raiz quadrada de {numero}: {raiz_arredondada}")

    # Verifica se a raiz é um número inteiro:
    if raiz.is_integer():
        print("O número possui raiz inteira!")
    else:
        print("O número não possui raiz inteira!")

    # Linha em branco para separar os resultados:
    print()
