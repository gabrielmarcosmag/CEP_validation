"""@autor: Gabriel Marcos Magalhães"""
from valida_cep import validate_cep

"""
Neste arquivo está um programa que utiliza a função val_cep para
validar um CEP fornecido pelo usuário
Argumento: CEP fornecido pelo usuário (string)
Retorno: Imprime na tela "CEP válido" caso o CEP fornecido atenda aos
requisitos. Caso não atenda, imprime "CEP inválido"
"""
print("Digite o CEP (somente números):")
cep = input() # Lê o CEP fornecido pelo usuário
if validate_cep(cep):
    print("CEP válido")
else:
    print("CEP inválido")