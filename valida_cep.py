###==================================================================================
### Neste arquivo está a função responsável por validar os CEPs
### Autor: Gabriel Marcos Magalhães
###==================================================================================

import re

def val_cep(cep):
    # Validação do formato do CEP
    res = re.match(r'^[1-9]\d{5}$',cep)
    if(res==None): return "Invalido"

    return "Valido"