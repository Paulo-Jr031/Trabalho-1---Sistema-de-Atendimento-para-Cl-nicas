from entidades.ProfissionalSaude import ProfissionalSaude

class Procedimento:
    def __init__(self, nome: str, descricao: str, preco: float, profissional_saude: ProfissionalSaude = None):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__profissional_saude = profissional_saude

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError('O nome do procedimento não pode ser vazio!')
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not descricao.strip():
            raise ValueError('A descrição do procedimento não pode ser vazio!')
        self.__descricao = descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if not isinstance(preco, (int, float)):
            raise TypeError('O preço do procedimento deve ser um número!')
        if preco < 0:
            raise ValueError('O preço do procedimento não pode ser negativo!')
        self.__preco = preco

    @property
    def profissional_saude(self):
        return self.__profissional_saude

    @profissional_saude.setter
    def profissional_saude(self, profissional_saude):
        if not isinstance(profissional_saude, ProfissionalSaude):
            raise TypeError('O profissional de saúde deve ser uma instância da classe ProfissionalSaude!')
        self.__profissional_saude = profissional_saude

