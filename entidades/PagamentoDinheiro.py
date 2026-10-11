from datetime import date as Date
import Pagamento from entidades.Pagamento

class PagamentoDinheiro(Pagamento):
    def __init__(self, valor):
        super().__init__(valor, Date.today())

    