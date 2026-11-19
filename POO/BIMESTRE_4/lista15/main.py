from datetime import datetime
from service.service import Service

def main():
    # 1. Inserindo registros
    Service.cliente_inserir("Ana Silva", "ana@email.com", "8499999-0001", "1234")
    Service.profissional_inserir("Dr. Carlos", "Fisioterapia", "CREFITO-12345", "carlos@clinica.com", "abcd")
    Service.servico_inserir("Sessão de Fisioterapia", 150.00)

    # 2. Listando registros
    print("--- Clientes ---")
    for c in Service.cliente_listar():
        print(c)

    print("\n--- Profissionais ---")
    for p in Service.profissional_listar():
        print(p)

    print("\n--- Serviços ---")
    for s in Service.servico_listar():
        print(s)

    # 3. Agendando Horário e registrando Atendimento
    Service.horario_inserir(datetime(2026, 11, 25, 14, 0), True, 1, 1, 1)
    Service.atendimento_inserir(datetime(2026, 11, 25, 14, 0), "Avaliação inicial concluída", 1, 1)

    print("\n--- Horários ---")
    for h in Service.horario_listar():
        print(h)

    print("\n--- Atendimentos ---")
    for a in Service.atendimento_listar():
        print(a)

if __name__ == "__main__":
    main()