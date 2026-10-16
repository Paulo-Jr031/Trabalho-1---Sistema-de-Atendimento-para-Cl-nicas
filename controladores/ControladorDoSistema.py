from datetime import date as Date, time as Time
from typing import List, Dict
from collections import Counter
from entidades import Clinica, Paciente, ProfissionalSaude, TipoAtendimento, Atendimento, Pagamento

class ControladorDoSistema:
    def __init__(self):
        self.__clinicas: List[Clinica] = []
        self.__pacientes: List[Paciente] = []
        self.__profissionais_saude: List[ProfissionalSaude] = []
        self.__tipos_atendimento: List[TipoAtendimento] = []
        self.__atendimentos: List[Atendimento] = []

        self.__inicializar_tipos_atendimento()

    def __inicializar_tipos_atendimento(self):
        self.__tipos_atendimento.append(TipoAtendimento("Consulta"))
        self.__tipos_atendimento.append(TipoAtendimento("Exame"))
        self.__tipos_atendimento.append(TipoAtendimento("Procedimento"))

    
    @property
    def clinicas(self):
        return self.__clinicas

    @property
    def pacientes(self):
        return self.__pacientes

    @property
    def profissionais_saude(self):
        return self.__profissionais_saude

    @property
    def tipos_atendimento(self):
        return self.__tipos_atendimento

    @property
    def atendimentos(self):
        return self.__atendimentos


    # Clinicas

    def cadastrar_clinica(self, nome: str, localizacao: str, descricao: str, abertura: Time, fechamento: Time):
        nova_clinica = Clinica(nome, localizacao, descricao, abertura, fechamento)
        self.__clinicas.append(nova_clinica)
        return nova_clinica

    def listar_clinicas(self):
        for i, clinica in enumerate(self.__clinicas):
            print(f"{i}. {clinica.nome} | localizacao: {clinica.localizacao} | descricao: {clinica.descricao} | abre às: {clinica.horario_abertura} | fecha às: {clinica.horario_fechamento}  ")

    def alterar_clinica(self, indice: int, novo_nome: str, nova_localizacao: str, nova_descricao: str, novo_abertura, novo_fechamento):
        if 0 <= indice < len(self.__clinicas):
            clinica = self.__clinicas[indice]

            clinica.nome = novo_nome
            clinica.localizacao = nova_localizacao
            clinica.descricao = nova_descricao
            clinica.horario_abertura = novo_abertura
            clinica.horario_fechamento = novo_fechamento
        else:
            raise IndexError("Índice de clínica inválido.")

    def excluir_clinica(self, indice: int):
        if 0 <= indice < len(self.__clinicas):
            self.__clinicas.pop(indice)
        else:
            raise IndexError("Índice de clínica inválido")



    # Pacientes

    def cadastrar_paciente(self, nome: str, telefone: str, cpf: str, data_nascimento: Date):
        novo_paciente = Paciente(nome, telefone, cpf, data_nascimento)
        self.__pacientes.append(novo_paciente)
        return novo_paciente

    def listar_pacientes(self):
        for i, paciente in enumerate(self.__pacientes):
            print(f"{i}. {paciente.nome} - CPF: {paciente.cpf} - Data de Nascimento: {paciente.data_nascimento} - Telefone: {paciente.telefone}")

    def alterar_paciente(self, indice: int, novo_nome: str, novo_cpf: str, novo_telefone: str, nova_data_nascimento: Date):
        if 0 <= indice < len(self.__pacientes):
            paciente = self.__pacientes[indice]

            paciente._Pessoa__nome = novo_nome
            paciente._Pessoa__cpf = novo_cpf
            paciente._Pessoa__telefone = novo_telefone
            paciente.data_nascimento = nova_data_nascimento
        else:
            raise IndexError("Índice de Paciente inválido.")

    def excluir_paciente(self, indice: int):
        if 0 <= indice < len(self.__pacientes):
            self.__pacientes.pop(indice)

        else:
            raise IndexError("Índice de paciente inválido")


    # Profissionais

    def cadastrar_profissional_saude(self, nome: str, cpf: str, telefone: str, especialidade: str, registro_profissional: str):
        novo_profissional = ProfissionalSaude(nome, cpf, telefone, especialidade, registro_profissional)
        self.__profissionais_saude.append(novo_profissional)
        return novo_profissional

    def listar_profissionais(self):
        for i, profissional in enumerate(self.__profissionais_saude):
            print(f"'{i}. {profissional.nome} - Especialidade: {profissional.especialidade}  - Registro Profissional:  {profissional.registro_profissional} - Telefone: {profissional.telefone}")

    def alterar_profissional_saude(self, indice: int, novo_nome: str, novo_cpf: str, novo_telefone: str, nova_especialidade: str, novo_registro: str):
        if 0 <= indice < len(self.__profissionais_saude):
            profissional = self.__profissionais_saude[indice]

            profissional._Pessoa__nome = novo_nome
            profissional._Pessoa__cpf = novo_cpf
            profissional._Pessoa__telefone = novo_telefone
            profissional.especialidade = nova_especialidade
            profissional.registro_profissional = novo_registro
        else:
            raise IndexError("Índice de profissional inválido")

    def excluir_profissional_saude(self, indice: int):
        if 0 <= indice < len(self.__profissionais_saude):
            self.__profissionais_saude.pop(indice)
        else:
            raise IndexError("Índice de profissional inválido")

    def listar_atendimentos(self):
        for i, atendimento in enumerate(self.__atendimentos):
            print(f"{i}. {atendimento}")
    
    # Regrinhas ao agendar

    def agendar_atendimento(self, clinica: Clinica, paciente: Paciente, profissional_saude: ProfissionalSaude, tipo_atendimento: TipoAtendimento, data_atendimento: Date, horario_inicio: Time, horario_fim: Time, custo: float):
        
        # maior de idade
        if paciente.maior_de_idade() == False:
            raise ValueError("O paciente deve ser maior de idade para agendar um atendimento.")
        
        # funcionamento clinica
        if horario_inicio < clinica.horario_abertura or horario_fim > clinica.horario_fechamento:
            raise ValueError("O horário do atendimento deve estar dentro do horário de funcionamento da clínica.")

        novo_atendimento = Atendimento(data_atendimento, horario_inicio, horario_fim, custo, clinica, profissional_saude, tipo_atendimento, paciente)
        self.__atendimentos.append(novo_atendimento)
        return novo_atendimento

    
    def registrar_procedimento_em_atendimento(self, atendimento: Atendimento, descricao: str, preco: float, profissional_saude: ProfissionalSaude):
        atendimento.adicionar_procedimento(atendimento, descricao, preco, profissional_saude)

    
    def registrar_pagamento_em_atendimento(self, atendimento: Atendimento, pagamento: Pagamento):
        if pagamento.data_pagamento > atendimento.data_atendimento:
            raise ValueError("A data do pagamento não pode ser anterior à data do atendimento.")
        atendimento.registrar_pagamento(pagamento)

    def excluir_atendimento(self, indice: int):
        indice = int(indice)

        if 0 <= indice < len(self.__atendimentos):
            self.__atendimentos.pop(indice)
        else:
            raise IndexError("Índice de atendimento inválido.")

    def alterar_atendimento(self, indice: int, nova_clinica, novo_paciente, novo_profissional, novo_tipo, nova_data, novo_inicio, novo_fim, novo_valor):
        indice = int(indice)
        if 0 <= indice < len(self.__atendimentos):
            if not novo_paciente.maior_de_idade():
                raise ValueError("O paciente deve ser maior de idade para agendar um atendimento.")
            if novo_inicio < nova_clinica.horario_abertura or novo_fim > nova_clinica.horario_fechamento:
                raise ValueError("O horário do atendimento deve estar dentro do horário de funcionamento da clínica.")
                
            atendimento = self.__atendimentos[indice]
            atendimento._Atendimento__data_atendimento = nova_data
            atendimento._Atendimento__horario_inicio = novo_inicio
            atendimento._Atendimento__horario_fim = novo_fim
            atendimento._Atendimento__valor_base = novo_valor
            atendimento._Atendimento__clinica = nova_clinica
            atendimento._Atendimento__profissional = novo_profissional
            atendimento._Atendimento__tipo = novo_tipo
            atendimento._Atendimento__paciente = novo_paciente

            atendimento._Atendimento__procedimentos = []
            atendimento._Atendimento__pagamentos = []
        else:
            raise IndexError("\n Índice de atendimento inválido.")

    
    # relatorio

    def relatorio_clinicas_mais_atendimentos(self):
        if not self.__atendimentos:
            return print("Nenhum atendimento registrado.")
        else:
            contagem = Counter(atendimento.clinica for atendimento in self.__atendimentos)
            return [{"clinica": clinica.nome, "atendimentos": qtd} for clinica, qtd in contagem.most_common()]

    def relatorio_atendimentos_mais_caro_mais_barato(self):
        if not self.__atendimentos:
            return print("Nenhum atendimento registrado.")
        else:
            mais_caro = self.__atendimentos[0]
            mais_barato = self.__atendimentos[0]

            for atendimento in self.__atendimentos:
                if atendimento.calcular_valor_total() > mais_caro.calcular_valor_total():
                    mais_caro = atendimento
                if atendimento.calcular_valor_total() < mais_barato.calcular_valor_total():
                    mais_barato = atendimento
                
        return {
            "mais_caro": {"id": mais_caro, "valor": mais_caro.calcular_valor_total()},
            "mais_barato": {"id": mais_barato, "valor": mais_barato.calcular_valor_total()}
        }


    def relatorio_procedimentos_populares(self):
        if not self.__atendimentos:
            return print("Nenhum atendimento registrado.")
        
        else: 
            todos_procedimentos = []
            for atendimento in self.__atendimentos:
                for proc in atendimento.procedimentos:
                    todos_procedimentos.append(proc.descricao)
                
            contagem = Counter(todos_procedimentos)
            return [{"procedimento": desc, "frequencia": qtd} for desc, qtd in contagem.most_common()]

    def relatorio_procedimentos_mais_caros_mais_baratos(self):
        if not self.__atendimentos:
            return print("Nenhum atendimento registrado.")
        else:
            todos_procedimentos = []
            for atendimento in self.__atendimentos:
                todos_procedimentos.extend(atendimento.procedimentos)
            
            if not todos_procedimentos:
                return {"mais_caro": None, "mais_barato": None}
            
            mais_caro = todos_procedimentos[0]
            mais_barato = todos_procedimentos[0]
        
            for proc in todos_procedimentos:
                if proc.preco > mais_caro.preco:
                    mais_caro = proc
                if proc.preco < mais_barato.preco:
                    mais_barato = proc
                
            return {
                "mais_caro": {"descricao": mais_caro.descricao, "custo": mais_caro.preco},
                "mais_barato": {"descricao": mais_barato.descricao, "custo": mais_barato.preco}
            }
