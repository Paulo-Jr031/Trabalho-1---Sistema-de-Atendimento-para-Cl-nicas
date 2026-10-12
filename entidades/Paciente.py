from datetime import date as Date
from entidades.Pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, data_nascimento: Date):
        super().__init__(nome, cpf, telefone)
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio!')
        super().nome = nome

    @property
    def cpf(self):
        return super().cpf   
    
    @cpf.setter
    def cpf(self, cpf): 
        if not cpf.strip():
            raise ValueError('O CPF não pode ser vazio!')
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('O CPF deve conter 11 dígitos numéricos!')
        super().cpf = cpf

    @property
    def telefone(self):
        return super().telefone

    @telefone.setter
    def telefone(self, telefone):
        if not telefone.strip():
            raise ValueError('O telefone não pode ser vazio!')
        super().telefone = telefone

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if not data_nascimento:
            raise ValueError('A data de nascimento não pode ser vazio!')
        self.__data_nascimento = data_nascimento

    def maior_de_idade(self):
        hoje = Date.today()
        idade = hoje.year - self.__data_nascimento.year - ((hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day))
        return idade >= 18