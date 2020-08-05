###==================================================================================
### Neste arquivo estão escritos os TDDs utilizados na elaboração da função
### responsável por validar os CEPs
### Autor: Gabriel Marcos Magalhães
###==================================================================================

from unittest import TestCase, main
from valida_cep import val_cep

class TesteCEPValido(TestCase):
    # Verifica se existe algum CEP a ser validado
    def teste_cep_vazio(self):
        cep_entrada = ''
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)
    #Verificam se foram fornecidos apenas caracteres validos
    def teste_caracteres_validos(self):
        cep_entrada = '123a45'
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)

    def teste_com_espaco(self):
        cep_entrada = ' 12345'
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)

    # Verifica se o numero de caracteres eh maior que 6 (valor maximo 999999)
    def teste_maximo_caracteres(self):
        cep_entrada = '123456789'
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)

    # Verifica se o numero de caracteres eh menor que 6 (valor minimo 100000)
    def teste_minimo_caracteres(self):
        cep_entrada = '123'
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)

    #Verifica se o CEP eh maior que o valor minimo permitido de 100000
    def teste_valor_minimo(self):
        cep_entrada = '012345'
        retorno_esperado = 'Invalido'
        self.assertEqual(val_cep(cep_entrada),retorno_esperado)

main()