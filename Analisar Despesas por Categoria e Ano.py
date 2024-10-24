# Simulação de um banco de dados de despesas
despesas = {
    "Energia": {
        2022: 9273.24,
        2023: 10456.78
    },
    "Internet": {
        2022: 1200.50,
        2023: 1500.00
    },
    "Alimentação": {
        2022: 5000.00,
        2023: 6000.00
    }
}

def analisar_despesas():
    while True:
        categoria = input("Digite o tipo de despesa que deseja filtrar (ou 'sair' para encerrar): ")
        if categoria.lower() == 'sair':
            break
        
        ano = input("Digite o ano que deseja filtrar (ex.: 2023): ")
        
        # Verificação se a categoria e ano são válidos
        try:
            ano = int(ano)
            if categoria in despesas and ano in despesas[categoria]:
                total = despesas[categoria][ano]
                print(f"Total de despesas para '{categoria}' no ano {ano}: R$ {total:.2f}")
            else:
                print(f"Nenhum registro encontrado para '{categoria}' no ano {ano}.")
        except ValueError:
            print("Por favor, insira um ano válido.")

analisar_despesas()
