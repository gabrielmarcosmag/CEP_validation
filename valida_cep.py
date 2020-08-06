"""@autor: Gabriel Marcos Magalhães"""
import re # biblioteca para utilizar expressões regulares

def validate_cep(cep):
    """
    Função responsável por realizar a validação de um CEP fornecido
    Argumento: CEP a ser validado (string)
    Retorno: Valido se o CEP estiver de acordo e Invalido
            caso não esteja (string)
    """

    # Validação do formato do CEP: RegEx utilizada para determinar que o CEP não deve
    # começar em com 0 e que deve conter exatamente 6 caracateres numéricos
    if(re.match(r'^[1-9]\d{5}$',cep) == None): return False

    #Verifica se existem digitos alternados repetitivos em par
    if(re.match(r'.*(\d).\1.*', cep) != None): return False

    return True

def main():
        """
        Função principal que utiliza a função val_cep para
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

if __name__ == '__main__':
    main()