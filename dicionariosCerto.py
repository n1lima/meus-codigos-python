agenda_pagamento = {}

def adicionar_pagamento(data, valor):
    if data in agenda_pagamento:
        print("Já existe um pagamento agendado para esta data.")
    else:
        agenda_pagamento[data] = valor
        print(f"Pagamento agendado para {data}: R${valor}")

def excluir_pagamento(data):
    if data in agenda_pagamento:
        del agenda_pagamento[data]
        print(f"Pagamento na data {data} removido.")
    else:
        print("Não há pagamento agendado para esta data.")

def exibir_datas_pagamento():
    if not agenda_pagamento:
        print("Não há eventos de pagamento agendados.")
    else:
        print("Datas de eventos de pagamento:")
        for data in agenda_pagamento:
            print(data)

while True:
    print("\nMenu:")
    print("1. Adicionar evento de pagamento")
    print("2. Excluir evento de pagamento")
    print("3. Exibir lista de datas de eventos de pagamento")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        data = input("Digite a data (DDMM): ")
        valor = float(input("Digite o valor do pagamento: "))
        adicionar_pagamento(data, valor)
    elif opcao == "2":
        data = input("Digite a data do pagamento que deseja excluir (DDMM): ")
        excluir_pagamento(data)
    elif opcao == "3":
        exibir_datas_pagamento()
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
