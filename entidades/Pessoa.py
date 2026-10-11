from abc import ABC, abstractmethod 

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    @property
    @abstractmethod
    def nome(self):
        return self.__nome

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio!')
        self.__nome = nome

    @property
    @abstractmethod
    def cpf(self):
        return self.__cpf

    @cpf.setter
    @abstractmethod
    def cpf(self, cpf):
        if not cpf.strip():
            raise ValueError('O CPF não pode ser vazio!')
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('O CPF deve conter 11 dígitos numéricos!')
        self.__cpf = cpf

    @property
    @abstractmethod
    def telefone(self):
        return self.__telefone

    @telefone.setter
    @abstractmethod
    def telefone(self, telefone):
        if not telefone.strip():
            raise ValueError('O telefone não pode ser vazio!')
        self.__telefone = telefone