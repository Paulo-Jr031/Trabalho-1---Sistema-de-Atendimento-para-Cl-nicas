from __future__ import annotations
from datetime import date as Date, time as Time
from entidades import PagamentoDinheiro, PagamentoPix, PagamentoCartao



class LimitePrincipal:
    def __init__(self, controlador: ControladorDoSistema):
        self.__controlador = controlador

    def exibir_menu_principal(self):
        while True:
            print("\n==========================================")
            print("        SISTEMA DE GESTÃO DE CLÍNICAS ")
            print("========================================== \n")
            print("1. Menu de Cadastros(clínicas, pacientes...)")
            print("2. Agendar Atendimento")
            print("3. Registrar Procedimento em Atendimento")
            print("4. Listar Atendimento")
            print("5. Alterar Dados de Atendimento")
            print("6. Cancelar/Excluir Atendimento")
            print("7. Registrar Pagamento")
            print("8. Painel de Relatórios")
            print("0. Sair")

            try:

                opcao = input("\nEscolha uma opção: ")
                if opcao == "1":
                    self.__menu_cadastros()
                elif opcao == "2":
                    self.__menu_agendar_atendimento()
                elif opcao == "3":
                    self.__registrar_procedimento()
                elif opcao == "4":
                    self.__listar_atendimentos()
                elif opcao =="5":
                    self.__alterar_atendimento()
                elif opcao == "6":
                    self.__excluir_atendimento()
                elif opcao == "7":
                    self.__menu_registrar_pagamento()
                elif opcao == "8":
                    self.__menu_relatorios()
                elif opcao == "0":
                    print("Encerrando o sistema... Até logo!")
                    break
                else:
                    raise IndexError("Índice fora de limite ou inválido")

            except Exception as e:
                print(f"\n Ocorreu um erro inesperado: {e}")


    def __menu_cadastros(self):
        while True:
            print("\n==========================================================")
            print("                 SISTEMA DE  CADASTROS           ")
            print("==========================================================")
            print("  1. Cadastrar Clínica            2. Listar Clínicas")
            print("  3. Alterar Clínica              4. Excluir Clínica")
            print("----------------------------------------------------------")
            print("  5. Cadastrar Paciente           6. Listar Pacientes")
            print("  7. Alterar Paciente             8. Excluir Paciente")
            print("----------------------------------------------------------")
            print("  9. Cadastrar Profissional       10. Listar Profissionais")
            print("  11. Alterar Profissional        12. Excluir Profissional")
            print("---------------------------------------------------------")
            print("             0. Voltar ao Menu Principal")
            print("==========================================================")

            try:

                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    print("\n--- Cadastro de Clínica ---")
                    nome = input("Nome da clínica: ")
                    localizacao = input("Localização da clínica: ")
                    descricao = input("Descrição da clínica: ")
                    abertura = __import__('datetime').datetime.strptime(input("Horário de abertura (HH:MM): "), "%H:%M").time()
                    fechamento = __import__('datetime').datetime.strptime(input("Horário de fechamento (HH:MM): "), "%H:%M").time()
                    self.__controlador.cadastrar_clinica(nome, localizacao, descricao, abertura, fechamento)
                    print("Clínica cadastrada com sucesso!")

                elif opcao == "2":
                    print("\n--- Lista de Clínicas ---")
                    if not self.__controlador.clinicas: 
                        print("Nenhuma clínica cadastrada.")
                    else:
                        self.__controlador.listar_clinicas()

                elif opcao == "3":
                    print("\n--- Alterar Clínica ---")
                    if not self.__controlador.clinicas:
                        print("Nenhuma clínica para alterar.")
                        continue
                    self.__controlador.listar_clinicas()
                    indice = int(input("Digite o número da clínica que deseja alterar: "))
                    print("Digite os novos dados:")
                    nome = input("Novo Nome: ")
                    local = input("Nova Localização: ")
                    descricao = input("Nova Descrição: ")
                    abertura = __import__('datetime').datetime.strptime(input("Novo Horário Abertura (HH:MM): "), "%H:%M").time()
                    fechamento = __import__('datetime').datetime.strptime(input("Novo Horário Fechamento (HH:MM): "), "%H:%M").time()
                    self.__controlador.alterar_clinica(indice, nome, local, descricao, abertura, fechamento)
                    print("Clínica alterada com sucesso!")

                elif opcao == "4":
                    print("\n--- Excluir Clínica ---")
                    if not self.__controlador.clinicas:
                        print("Nenhuma clínica para excluir.")
                        continue
                    self.__controlador.listar_clinicas()
                    indice = int(input("Digite o número da clínica que deseja remover: "))
                    self.__controlador.excluir_clinica(indice)
                    print("Clínica removida com sucesso!")

                
                elif opcao == "5":
                    print("\n--- Cadastro de Paciente ---")
                    nome = input("Nome do paciente: ")
                    cpf = input("CPF do paciente: ")
                    telefone = input("Telefone do paciente: ")
                    data_nascimento = __import__('datetime').datetime.strptime(input("Data de nascimento (DD/MM/AAAA): "), "%d/%m/%Y").date()
                    self.__controlador.cadastrar_paciente(nome, cpf, telefone, data_nascimento)
                    print("Paciente cadastrado com sucesso!")

                elif opcao == "6":
                    print("\n--- Lista de Pacientes ---")
                    if not self.__controlador.pacientes: 
                        print("Nenhum paciente cadastrado.")
                    else:
                        self.__controlador.listar_pacientes()

                elif opcao == "7":
                    print("\n--- Alterar Paciente ---")
                    if not self.__controlador.pacientes:
                        print("Nenhum paciente para alterar.")
                        continue
                    self.__controlador.listar_pacientes()
                    indice = int(input("Digite o número do paciente que deseja alterar: "))
                    nome = input("Novo Nome: ")
                    cpf = input("Novo CPF: ")
                    telefone = input("Novo Telefone: ")
                    nascimento = __import__('datetime').datetime.strptime(input("Nova Data de Nascimento (DD/MM/AAAA): "), "%d/%m/%Y").date()
                    self.__controlador.alterar_paciente(indice, nome, cpf, telefone, nascimento)
                    print("Paciente alterado com sucesso!")

                elif opcao == "8":
                    print("\n--- Excluir Paciente ---")
                    if not self.__controlador.pacientes:
                        print("Nenhum paciente para excluir.")
                        continue
                    self.__controlador.listar_pacientes()
                    indice = int(input("Digite o número do paciente que deseja remover: "))
                    self.__controlador.excluir_paciente(indice)
                    print("Paciente removido com sucesso!")

            
                elif opcao == "9":
                    print("\n--- Cadastro de Profissional de Saúde ---")
                    nome = input("Nome do profissional: ")
                    cpf = input("CPF do profissional: ")
                    telefone = input("Telefone do profissional: ")
                    especialidade = input("Especialidade do profissional: ")
                    registro = input("Registro profissional (ex: CRM/COREN): ")
                    self.__controlador.cadastrar_profissional_saude(nome, cpf, telefone, especialidade, registro)
                    print("Profissional cadastrado com sucesso!")

                elif opcao == "10":
                    print("\n--- Lista de Profissionais de Saúde ---")
                    if not self.__controlador.profissionais_saude: 
                        print("Nenhum profissional de saúde cadastrado.")
                    else:
                        self.__controlador.listar_profissionais()

                elif opcao == "11":
                    print("\n--- Alterar Profissional de Saúde ---")
                    if not self.__controlador.profissionais_saude:
                        print("Nenhum profissional para alterar.")
                        continue
                    self.__controlador.listar_profissionais()
                    indice = int(input("Digite o número do profissional que deseja alterar: "))
                    nome = input("Novo Nome: ")
                    telefone = input("Novo Telefone: ")
                    cpf = input("Novo CPF: ")
                    especialidade = input("Nova Especialidade: ")
                    registro = input("Novo Registro: ")
                    self.__controlador.alterar_profissional_saude(indice, nome, cpf, telefone, especialidade, registro)
                    print("Profissional de saúde alterado com sucesso!")

                elif opcao == "12":
                    print("\n--- Excluir Profissional de Saúde ---")
                    if not self.__controlador.profissionais_saude:
                        print("Nenhum profissional para excluir.")
                        continue
                    self.__controlador.listar_profissionais()
                    indice = int(input("Digite o número do profissional que deseja remover: "))
                    self.__controlador.excluir_profissional_saude(indice)
                    print("Profissional removido com sucesso!")

                elif opcao == "0":
                    break

                else:
                    raise IndexError("Índice fora de limite ou inválido")

            except Exception as e:
                print(f"\n Ocorreu um erro inesperado: {e}")

    
    # agendar atendimentos

    def __menu_agendar_atendimento(self):
        print("\n--- Agendar Novo Atendimento ---  ")
        if not self.__controlador.clinicas or not self.__controlador.pacientes or not self.__controlador.profissionais_saude or not self.__controlador.tipos_atendimento:
            print("Para agendar um atendimento, é necessário ter pelo menos uma clínica, um paciente e um profissional de saúde cadastrados.")
            return

        try:

            print("\nSelecione a clínica:")
            for i, clinica in enumerate(self.__controlador.clinicas):
                print(f"{i}. {clinica.nome}")
            clinica = self.__controlador.clinicas[int(input("Digite o número da clínica: "))]

            print("\nSelecione o paciente:")
            for i, paciente in enumerate(self.__controlador.pacientes):
                print(f"{i}. {paciente.nome}")
            paciente = self.__controlador.pacientes[int(input("Digite o número do paciente: "))]

            print("\nSelecione o profissional de saúde:")
            for i, profissional in enumerate(self.__controlador.profissionais_saude):
                print(f"{i}. {profissional.nome} - {profissional.especialidade}")
            profissional = self.__controlador.profissionais_saude[int(input("Digite o número do profissional: "))]

            print("\nSelecione o tipo de atendimento:")
            for i, tipo in enumerate(self.__controlador.tipos_atendimento):
                print(f"{i}. {tipo.tipo_atendimento}")
            tipo = self.__controlador.tipos_atendimento[int(input("Digite o número do tipo de atendimento: "))]

            data_atendimento = __import__('datetime').datetime.strptime(input("Data do atendimento (DD/MM/AAAA): "), "%d/%m/%Y").date()
            horario_inicio = __import__('datetime').datetime.strptime(input("Horário de início (HH:MM): "), "%H:%M").time()
            horario_fim = __import__('datetime').datetime.strptime(input("Horário de fim (HH:MM): "), "%H:%M").time()
            valor = float(input("Valor base do atendimento (R$): "))

            atendimento = self.__controlador.agendar_atendimento(clinica, paciente, profissional, tipo, data_atendimento, horario_inicio, horario_fim, valor)
            print(f"Atendimento agendado com sucesso!\n{atendimento}")

        except ValueError as e:
            print(f"Erro ao agendar atendimento: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    # registro procedimentos

    def __menu_registrar_procedimento(self):
        print("\n--- Registrar Procedimento em Atendimento ---")
        if not self.__controlador.atendimentos:
            print("Nenhum atendimento foi agendado por enquanto.")
            return

        try:
            print("\nSelecione o atendimento:")
            for i, atendimento in enumerate(self.__controlador.atendimentos):
                print(f"{i}. {atendimento}")
            atendimento = self.__controlador.atendimentos[int(input("Digite o número do atendimento: "))]

            print("\nSelecione o profissional de saúde responsável pelo procedimento:")
            for i, profissional in enumerate(self.__controlador.profissionais_saude):
                print(f"{i}. {profissional.nome} - {profissional.especialidade}")
            profissional = self.__controlador.profissionais_saude[int(input("Digite o número do profissional: "))]

            descricao = input("Descrição do procedimento: ")
            preco = float(input("Preço do procedimento (R$): "))
            
            self.__controlador.registrar_procedimento_em_atendimento(atendimento, descricao, preco, profissional)
            print("Procedimento registrado com sucesso!")

        except ValueError as e:
            print(f"Erro ao registrar procedimento: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    # registro pagamento

    def __menu_registrar_pagamento(self):
        
        try:
           
            print("\n--- Registrar Pagamento ---")
            if not self.__controlador.atendimentos:
                print("Nenhum atendimento foi agendado por enquanto.")


            print("\nSelecione o atendimento:")
            for i, atendimento in enumerate(self.__controlador.atendimentos):
                print(f"{i}. {atendimento}") 
            
            entrada = input("Digite o número do atendimento: ")

            if not entrada.isdigit() or int(entrada) < 0 or int(entrada) >= len(self.__controlador.atendimentos):
                raise IndexError("Índice fora dos limites ou inválido")

            else:
                atendimento = self.__controlador.atendimentos[int(entrada)]

                print(f"Saldo devedor: R${atendimento.calcular_valor_restante():.2f}")
                if atendimento.calcular_valor_restante() <= 0:
                    print("Este atendimento já está totalmente pago.")
                
                data_pagamento = __import__('datetime').datetime.strptime(input("Data do pagamento (DD/MM/AAAA): "), "%d/%m/%Y").date()
                valor_pagamento = float(input("Valor do pagamento (R$): "))
                if valor_pagamento > atendimento.calcular_valor_restante() or valor_pagamento <= 10:
                    raise ValueError("\n O valor informado é maior que o total a pagar ou é menor que o valor minimo, tente novamente com o valor correto.")

                print("\nSelecione a forma de pagamento:")
                print("1. Dinheiro")
                print("2. PIX")
                print("3. Cartão de Crédito/Débito")
                modalidade_pagamento = input("Digite o número da forma de pagamento: ")

                if modalidade_pagamento == "1":
                    pagamento = PagamentoDinheiro(valor_pagamento, data_pagamento)
                elif modalidade_pagamento == "2":
                    cpf_pagador = input("Digite o CPF do pagador: ")
                    pagamento = PagamentoPix(valor_pagamento, data_pagamento, cpf_pagador)
                elif modalidade_pagamento == "3":
                    bandeira_cartao = input("Digite a bandeira do cartão (ex: Visa, MasterCard): ")
                    pagamento = PagamentoCartao(valor_pagamento, data_pagamento, bandeira_cartao)
                else:
                    raise ValueError("\nOpção de pagamento inválida!")
                    return

                self.__controlador.registrar_pagamento_em_atendimento(atendimento, pagamento)
                print(f"Pagamento registrado com sucesso! Saldo devedor atualizado: R${atendimento.calcular_valor_restante():.2f}")

        except ValueError as e:
            print(f"Erro ao registrar procedimento: {e}")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    # listar atendimentos

    def __listar_atendimentos(self):
        print("\n--- Lista de Atendimentos Agendados ---")
        if not self.__controlador.atendimentos:
            print("Nenhum atendimento foi agendado por enquanto.")
        else:
            self.__controlador.listar_atendimentos()


    # apagar/alterar atendimentos

    def __alterar_atendimento(self):
        
        try:
            print("\n--- Alterar Dados de Atendimento ---")
            if not self.__controlador.atendimentos:
                raise IndexError("Não existe um atendimento com esse índice") 

            else:
                for i, at in enumerate(self.__controlador.atendimentos):
                    print(f"{i}. {at}")
                indice = input("Digite o número do atendimento que deseja alterar: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.atendimentos):
                    raise IndexError("Índice fora dos limites ou inválido")

                print("\nSelecione a Nova Clínica:")
                for i, clinica in enumerate(self.__controlador.clinicas):
                    print(f"{i}. {clinica.nome}")
                indice = input("Digite o número da clínica que deseja adicionar: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.clinicas):
                    raise IndexError("Índice fora dos limites ou inválido")
                clinica = self.__controlador.clinicas[int(indice)]

                print("\nSelecione o Novo Paciente:")
                for i, paciente in enumerate(self.__controlador.pacientes):
                    print(f"{i}. {paciente.nome}")
                indice = input("Digite o número do paciente que deseja adicionar: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.pacientes):
                    raise IndexError("Índice fora dos limites ou inválido")
                paciente = self.__controlador.pacientes[int(indice)]

                print("\nSelecione o Novo Profissional:")
                for i, profissional in enumerate(self.__controlador.profissionais_saude):
                    print(f"{i}. {profissional.nome}")
                indice = input("Digite o número do profissional que deseja adicionar: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.profissionais_saude):
                    raise IndexError("Índice fora dos limites ou inválido")
                profissional = self.__controlador.profissionais_saude[int(indice)]

                print("\nSelecione o Novo Tipo:")
                for i, tipo in enumerate(self.__controlador.tipos_atendimento):
                    print(f"{i}. {tipo.tipo_atendimento}")
                indice = input("Digite o número do tipo de atendimento que será realizado: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.tipos_atendimento):
                    raise IndexError("Índice fora dos limites ou inválido")
                tipo = self.__controlador.tipos_atendimento[int(indice)]

                data_atendimento = __import__('datetime').datetime.strptime(input("Nova Data (DD/MM/AAAA): "), "%d/%m/%Y").date()
                horario_inicio = __import__('datetime').datetime.strptime(input("Novo Início (HH:MM): "), "%H:%M").time()
                horario_fim = __import__('datetime').datetime.strptime(input("Novo Fim (HH:MM): "), "%H:%M").time()
                valor = float(input("Novo Valor Base (R$): "))

                self.__controlador.alterar_atendimento(indice, clinica, paciente, profissional, tipo, data_atendimento, horario_inicio, horario_fim, valor)
                print("Atendimento alterado com sucesso!")

        except IndexError as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def __excluir_atendimento(self):

        try:
        
            print("\n--- Cancelar/Excluir Atendimento ---")
            if not self.__controlador.atendimentos:
                print("Nenhum atendimento para excluir.")
            
            else:
                for i, atendimento in enumerate(self.__controlador.atendimentos):
                    print(f"{i}. {atendimento}")
                indice = input("Digite o número do atendimento que deseja remover: ")
                if not indice.isdigit() or int(indice) < 0 or int(indice) >= len(self.__controlador.atendimentos):
                    raise IndexError("Índice fora dos limites ou inválido")
                else:
                    self.__controlador.excluir_atendimento(indice)
                    print("Atendimento cancelado e removido com sucesso!")

        except IndexError as e:
            print(f"\n Erro ao registrar procedimento: {e}")


    # relatorios

    def __menu_relatorios(self):
        while True:
            print("\n      ----- Paínel de Relatórios -----")
            print("---------------------------------------------")
            print("1. Clínicas com maior número de atendimentos")
            print("2. Atendimentos mais caros e mais baratos")
            print("3. Procedimentos mais realizados")
            print("4. Procedimentos mais caros e mais baratos")
            print("0. Voltar ao Menu Principal")

            opcao = input("\nEscolha uma opção: ")   

            try:

                if opcao == "1":
                    relatorio = self.__controlador.relatorio_clinicas_mais_atendimentos()
                    print("\n--- Clínicas com Maior Número de Atendimentos ---")
            
                    if relatorio is None or len(relatorio) == 0:
                        print("Sem dados suficientes de atendimentos cadastrados.")
                    else:
                        for item in relatorio:
                            print(f"-> Clínica: {item['clinica']} | Total de Atendimentos: {item['atendimentos']}")

                elif opcao == "2":
                    relatorio = self.__controlador.relatorio_atendimentos_mais_caro_mais_barato()
                    print("\n--- Atendimentos Mais Caros e Mais Baratos ---")
                
                    if relatorio is None or relatorio["mais_caro"] is None:
                        print("Sem dados suficientes de atendimentos cadastrados.")
                    else:
                        print(f"-> Mais Caro: {relatorio['mais_caro']['id']} (Total: R$ {relatorio['mais_caro']['valor']:.2f})")
                        print(f"-> Mais Barato: {relatorio['mais_barato']['id']} (Total: R$ {relatorio['mais_barato']['valor']:.2f})")

                elif opcao == "3":
                    relatorio = self.__controlador.relatorio_procedimentos_populares()
                    print("\n--- Ranking de Procedimentos mais Populares ---")
                
                    if relatorio is None or len(relatorio) == 0:
                        print("Sem dados suficientes de procedimentos cadastrados.")
                    else:
                        for item in relatorio:
                            print(f"-> Procedimento: {item['procedimento']} | Realizado: {item['frequencia']} vezes")

                elif opcao == "4":
                    relatorio = self.__controlador.relatorio_procedimentos_mais_caros_mais_baratos()
                    print("\n--- Procedimentos Mais Caros e Mais Baratos ---")
                
                    if relatorio is None or relatorio["mais_caro"] is None:
                        print("Sem dados suficientes de procedimentos cadastrados.")
                    else:
                        print(f"-> Procedimento Mais Caro: {relatorio['mais_caro']['descricao']} (Custo: R$ {relatorio['mais_caro']['custo']:.2f})")
                        print(f"-> Procedimento Mais Barato: {relatorio['mais_barato']['descricao']} (Custo: R$ {relatorio['mais_barato']['custo']:.2f})")

                elif opcao == "0":
                    print("Voltando ao Menu Principal...")
                    break

                else:
                    raise IndexError("Índice de profissional inválido")

            except IndexError as e:
                print(f"\n Erro ao registrar procedimento: {e}")
