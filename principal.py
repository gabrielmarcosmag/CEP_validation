from valida_cep import val_cep

print("Digite o CEP:")
cep = input()
if val_cep(cep) == "Valido":
    print("CEP válido")
else:
    print("CEP inválido")