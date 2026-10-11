from datetime import date as Date
import Pagamento from entidades.Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self, valor: float, bandeira: str):
        super().__init__(valor, Date.today())
        self.__bandeira = bandeira

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira):
        if not bandeira.strip():
            raise ValueError('A bandeira não pode ser vazio!')
        self.__bandeira = bandeira