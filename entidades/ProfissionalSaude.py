class ProfssionalSaude:
    def __init__(self, nome: str, especialidade: str, registro_profissional: str):
        self.__nome = nome
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