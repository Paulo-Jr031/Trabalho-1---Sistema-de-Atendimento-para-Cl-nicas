from datetime import date as Date
from entidades.Pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def __init__(self, valor: float, data_pagamento: Date, bandeira: str):
        super().__init__(valor, data_pagamento)
        self.__bandeira = bandeira

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        if not bandeira.strip():
            raise ValueError('A bandeira não pode ser vazio!')
        self.__bandeira = bandeira