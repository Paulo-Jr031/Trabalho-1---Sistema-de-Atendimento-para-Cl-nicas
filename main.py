from datetime import date, time
from controladores.ControladorDoSistema import ControladorDoSistema
from limites.LimitePrincipal import LimitePrincipal

def dados_teste(controlador):
    
    try:
        # Cadastrar Clínicas
        c1 = controlador.cadastrar_clinica("Clínica Saúde Centro", "Florianópolis", "Atendimento Geral", time(8, 0), time(18, 0))
        c2 = controlador.cadastrar_clinica("Clínica Universitária Trindade", "Florianópolis", "Pronto Atendimento", time(7, 0), time(22, 0))

        #  Cadastrar Pacientes 
        p1 = controlador.cadastrar_paciente("João da Silva","000.111.222-33", "48999991111", date(1990, 5, 15))
        
        # Cadastrar Profissionais de Saúde 
        med1 = controlador.cadastrar_profissional_saude("Dr. Carlos Alberto", "111.222.333-44", "48988881111", "Cardiologia", "CRM/SC 12345")
        med2 = controlador.cadastrar_profissional_saude("Dra. Mariana Souza", "555.666.777-88", "48988882222", "Pediatria", "CRM/SC 67890")
        
        # tipos de atendimento
        tipo_consulta = controlador.tipos_atendimento[0] 
        tipo_exame = controlador.tipos_atendimento[1]    
        
        #  Atendimentos 
        at1 = controlador.agendar_atendimento(c1, p1, med1, tipo_consulta, date(2026, 10, 9), time(9, 30), time(10, 15), 150.00)       
        at2 = controlador.agendar_atendimento(c2, p1, med2, tipo_exame, date(2026, 10, 10), time(14, 0), time(15, 0), 300.00)

        
        # procedimentos
        controlador.registrar_procedimento_em_atendimento(at1, "Eletrocardiograma", 80.00, med1)
        controlador.registrar_procedimento_em_atendimento(at2, "Hemograma Completo", 45.00, med2)
        
        print("Dados de teste injetados com sucesso!")

    except Exception as e:
        print(f"Inserção dos dados de teste falhou. motivo: {e}")


if __name__ == "__main__":
    
    controlador_sistema = ControladorDoSistema()
    
    dados_teste(controlador_sistema)
    
    tela_principal = LimitePrincipal(controlador_sistema)

    tela_principal.exibir_menu_principal()
