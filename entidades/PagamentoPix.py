import Pagamento from entidades.Pagamento

class PagamnetoPix(Pagamento):
    def __init__(self, cpf_pagador: str):
        super().__init__(valor, Date.today())
        self.cpf__pagador = cpf_pagador
    
    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador):
        if not cpf_pagador.strip():
            raise ValueError('O CPF do pagador não pode ser vazio!')
        if len(cpf_pagador) != 11 or not cpf_pagador.isdigit():
            raise ValueError('O CPF do pagador deve conter 11 dígitos numéricos!')
        self.__cpf_pagador = cpf_pagador
