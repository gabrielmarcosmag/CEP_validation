# CEP_validation
This program is used to validate the CEP of a famous city where a famous bat lives.


# Problema abordado:

O sistema dos correios de Gotham City tiveram um problema e perderam seu validador de CEPs. Hoje, sua missão é criar um validador de CEPs baseados em algumas pequenas regras listadas abaixo:
* O CEP é um número maior que 100000 e menor que 999999
* O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares
  * 121426 # Aqui, 1 é um dígito repetitivo alternado em par.
  * 523563 # Aqui nenhum digito é alternado.
  * 552523 # Aqui os números 2 e 5 são dígitos alternados repetitivos em par.
  
# Instruções

O código foi escrito para ser executado em **Python 3**

Existem duas ações possíveis: validar um CEP ou executar os testes unitários implementados.

## Opção 1: Execução dos testes unitários

Para que os testes sejam realizados basta executar o arquivo *testes.py*.
Esse arquivo é composto por oito testes e o resultado apresentado deve ser

........
----------------------------------------------------------------------
Ran 8 tests in x s

OK

## Opção 2: Validação de um CEP

Para realizar a validação de um CEP escolhido pelo usuário basta executar o arquivo *valida_cep.py*.
Será solicitado que o usuário insira o CEP que deseja validar e logo após será exibido na tela o resultado **CEP válido** caso o CEP atenda aos padrões exigidos ou **CEP inválido** caso o CEP não atenda tais padrões.
