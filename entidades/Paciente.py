from datetime import date as Date
import Pessoa from entidades.Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, data_nascimento: Date, endereco: str):
        super().__init__(nome, cpf, telefone)
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio!')
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf   
    
    @cpf.setter
    def cpf(self, cpf): 
        if not cpf.strip():
            raise ValueError('O CPF não pode ser vazio!')
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('O CPF deve conter 11 dígitos numéricos!')
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        if not telefone.strip():
            raise ValueError('O telefone não pode ser vazio!')
        self.__telefone = telefone

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if not data_nascimento.strip():
            raise ValueError('A data de nascimento não pode ser vazio!')
        self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        if not endereco.strip():
            raise ValueError('O endereço não pode ser vazio!')
        self.__endereco = endereco