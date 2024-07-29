"""
Nome do programa: teste
Descricao: Calculadora que permita as quatro operacoes matematicas, utilizando valores digitados pelos usuarios
Autor: Evando Chaves
Criado em: 15/07/2024
"""

numero_1 = input('Entre com o Numero 1:')
numero_2 = input('Entre com o Numero 2:')

num_1 = int(numero_1)
num_2 = int(numero_2)

soma          = num_1 + num_2
subtracao     = num_2 - num_1
multiplicacao = num_1 * num_2
divisao       = num_2 / num_1

print('O Resultado da Calculadora para:')
print('Resultado da adicao........: ',soma)
print('Resultado da Subtracao.....: ',subtracao)
print('Resultado da Multiplicacao.: ',multiplicacao)
print('Resultado da Divisao.......: ',divisao)

