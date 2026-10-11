from abc import ABC, abstractmethod
from datetime import date as Date


class Pagamento(ABC):
    def __init__(self, valor: float, data_pagamento: Date):
        self.valor = valor
        self.data_pagamento = data_pagamento

    @property
    @abstractmethod
    def valor(self):
        return self.__valor 

    @valor.setter
    @abstractmethod
    def valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor do pagamento deve ser maior que zero.")
        self.__valor = valor

    @property
    @abstractmethod
    def data_pagamento(self):
        return self.__data_pagamento

    @data_pagamento.setter
    @abstractmethod
    def data_pagamento(self, data_pagamento):
        if not isinstance(data_pagamento, Date):
            raise ValueError("A data de pagamento deve ser uma instância da classe Date.")
        self.__data_pagamento = data_pagamento