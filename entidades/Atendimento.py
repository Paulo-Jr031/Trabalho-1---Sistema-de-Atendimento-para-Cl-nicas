from date time import date as Date
from typing import List
from entidades.Clinica import Clinica
from entidades.ProfissionalSaude import ProfissionalSaude
from entidades.TipoAtendimento import TipoAtendimento
from entidades.Procedimento import Procedimento
from entidades.Paciente import Paciente
from entidades.Pagamento import Pagamento

class Atendimento:
    def __init__(self, data_atendimento: Date, horario_inicio: Time, horario_fim: Time, 
                valor_base: float,clinica: Clinica, profissional_saude: ProfissionalSaude, 
                tipo_atendimento: TipoAtendimento, paciente: Paciente):


        self.__data_atendimento = data_atendimento
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor_base = valor_base

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional_saude = profissional_saude
        self.__tipo_atendimento = tipo_atendimento
        
        self.__procedimentos: List[Procedimento] = []
        self.__pagamentos: List[Pagamento] = []

    @property
    def clinica(self):
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica):
        if not isinstance(clinica, Clinica):
            raise ValueError("A clínica deve ser uma instância da classe Clinica.")
        self.__clinica = clinica

    @property
    def data_atendimento(self):
        return self.__data_atendimento

    @data_atendimento.setter
    def data_atendimento(self, data_atendimento):
        if not isinstance(data_atendimento, Date):
            raise ValueError("A data do atendimento deve ser uma instância da classe Date.")
        self.__data_atendimento = data_atendimento

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        if not isinstance(horario_inicio, Time):
            raise ValueError("O horário de início deve ser uma instância da classe Time.")
        self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        if not isinstance(horario_fim, Time):
            raise ValueError("O horário de fim deve ser uma instância da classe Time.")
        self.__horario_fim = horario_fim

    @property
    def profissional_saude(self):
        return self.__profissional_saude

    @profissional_saude.setter
    def profissional_saude(self, profissional_saude):
        if not isinstance(profissional_saude, ProfissionalSaude):
            raise ValueError("O profissional de saúde deve ser uma instância da classe ProfissionalSaude.")
        self.__profissional_saude = profissional_saude

    @property
    def valor_base(self):
        return self.__valor_base

    @valor_base.setter
    def valor_base(self, valor_base):
        if not isinstance(valor_base, (int, float)):
            raise TypeError("O valor base deve ser um número.")
        if valor_base < 0:
            raise ValueError("O valor base não pode ser negativo.")
        self.__valor_base = valor_base


    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento):
        if not isinstance(tipo_atendimento, TipoAtendimento):
            raise ValueError("O tipo de atendimento deve ser uma instância da classe TipoAtendimento.")
        self.__tipo_atendimento = tipo_atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise ValueError("O paciente deve ser uma instância da classe Paciente.")
        self.__paciente = paciente

    @property
    def procedimentos(self):
        return self.__procedimentos

    @property
    def pagamentos(self):
        return self.__pagamentos


    def adicionar_procedimento(self, descricao: str, preco: float, profissional_saude: ProfissionalSaude):
        procedimento = Procedimento(descricao, preco, profissional_saude)
        if not isinstance(procedimento, Procedimento):
            raise ValueError("O procedimento deve ser uma instância da classe Procedimento.")
        self.__procedimentos.append(procedimento)

    def registrar_pagamento(self, pagamento: Pagamento):
        if not isinstance(pagamento, Pagamento):
            raise ValueError("O pagamento deve ser uma instância da classe Pagamento.")
        self.__pagamentos.append(pagamento)

    def calcular_valor_total(self):
        valor_total = self.__valor_base
        for procedimento in self.__procedimentos:
            valor_total += procedimento.preco
        return valor_total

    def calcular_valor_restante(self):
        valor_total = self.calcular_valor_total()
        valor_pago = sum(pagamento.valor for pagamento in self.__pagamentos)
        return valor_total - valor_pago

    def __str__(self):
        data_atendimento_str = self.__data_atendimento.strftime("%d/%m/%Y")
        total = self.calcular_valor_total()
        restante = self.calcular_valor_restante()
        return f"Atendimento em {data_atendimento_str} na clínica {self.__clinica.nome} com o profissional 
        {self.__profissional_saude.nome}. Valor total: R${total:.2f}, Valor restante: R${restante:.2f}"