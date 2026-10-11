import Pessoa from entidades.Pessoa

class ProfssionalSaude(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, especialidade: str, registro_profissional: str):
        super().__init__(nome, cpf, telefone)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

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
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        if not especialidade.strip():
            raise ValueError('A especialidade não pode ser vazio!')
        self.__especialidade = especialidade

    @property
    def registro_profissional(self):
        return self.__registro_profissional

    @registro_profissional.setter
    def registro_profissional(self, registro_profissional):
        if not registro_profissional.strip():
            raise ValueError('O registro profissional não pode ser vazio!')
        self.__registro_profissional = registro_profissional