"""@autor: Gabriel Marcos Magalhães"""

from unittest import TestCase, main # biblioteca utilizada nos TDDs
from valida_cep import validate_cep # função responsável pela validação dos CEPs

class TesteCEPValido(TestCase):
    """
    Nesta classe estão escritos os TDDs utilizados na elaboração da função
    responsável por validar os CEPs
    """

    # Verifica se existe algum CEP a ser validado
    def teste_cep_vazio(self):
        cep_entrada = ''
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)
    #Verificam se foram fornecidos apenas caracteres validos
    def teste_caracteres_validos(self):
        cep_entrada = '123a45'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    def teste_com_espaco(self):
        cep_entrada = ' 12345'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    # Verifica se o numero de caracteres eh maior que 6 (valor maximo 999999)
    def teste_maximo_caracteres(self):
        cep_entrada = '123456789'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    # Verifica se o numero de caracteres eh menor que 6 (valor minimo 100000)
    def teste_minimo_caracteres(self):
        cep_entrada = '123'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    #Verifica se o CEP eh maior que o valor minimo permitido de 100000
    def teste_valor_minimo(self):
        cep_entrada = '012345'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    #Verifica se existem dígitos alternados repetitivos
    def teste_digitos_alternados_repetitivos(self):
        cep_entrada = '121426'
        retorno_esperado = False
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

    # Realiza a verificação de um CEP válido
    def teste_cep_valido(self):
        cep_entrada = '523563'
        retorno_esperado = True
        self.assertEqual(validate_cep(cep_entrada),retorno_esperado)

main()