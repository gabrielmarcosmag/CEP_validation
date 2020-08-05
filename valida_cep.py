"""@autor: Gabriel Marcos Magalhães"""
import re # biblioteca para utilizar expressões regulares

def val_cep(cep):
    """
    Função responsável por realizar a validação de um CEP fornecido
    Argumento: CEP a ser validado (string)
    Retorno: Valido se o CEP estiver de acordo e Invalido
            caso não esteja (string)
    """

    # Validação do formato do CEP: RegEx utilizada para determinar que o CEP não deve
    # começar em com 0 e que deve conter exatamente 6 caracateres numéricos
    res = re.match(r'^[1-9]\d{5}$',cep)
    if(res==None): return "Invalido"

    #Verifica se existem digitos alternados repetitivos em par
    for i in range(4):
        if(cep[i] == cep[i+2]): return "Invalido"

    return "Valido"