from datetime import date as Date
from .Pagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def __init__(self, valor: float, data_pagamento: Date):
        super().__init__(valor, data_pagamento)


    