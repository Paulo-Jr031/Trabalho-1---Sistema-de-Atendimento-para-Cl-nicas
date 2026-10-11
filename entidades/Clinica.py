from datetime import time as Time

class Clinica:
    def __init__(self, nome: str, cnpj: str, localizacao: str, descricao: str, horario_abertura: Time, horario_fechamento: Time):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome não pode ser vazio!')
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if not cnpj.strip():
            raise ValueError('O CNPJ não pode ser vazio!')
        if len(cnpj) != 14 or not cnpj.isdigit():
            raise ValueError('O CNPJ deve conter 14 dígitos numéricos!')
        self.__cnpj = cnpj

    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, localizacao):
        if not localizacao.strip():
            raise ValueError('A localização não pode ser vazia!')
        self.__localizacao = localizacao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not descricao.strip():
            raise ValueError('A descrição não pode ser vazia!')
        self.__descricao = descricao

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura):
        if not isinstance(horario_abertura, Time):
            raise ValueError('O horário de abertura deve ser um objeto do tipo Time!')
        self.__horario_abertura = horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento):
        if not isinstance(horario_fechamento, Time):
            raise ValueError('O horário de fechamento deve ser um objeto do tipo Time!')
        self.__horario_fechamento = horario_fechamento

    def __str__(self):
        abertura = self.__horario_abertura.strftime("%H:%M")
        fechamento = self.__horario_fechamento.strftime("%H:%M")
        return f"Clínica: {self.__nome}\nCNPJ: {self.__cnpj}\nLocalização: {self.__localizacao} | Exp: {abertura} às {fechamento}"    