# GS ClimaCode - Pensamento Computacional e Automação com Python
# Laís Salomão RM: 565262

# --- Tarefa 1: Entrada de dados ambientais (simulados) ---
# Vetores com dados de 7 dias para temperatura, umidade e precipitação. 
temperaturas_diarias = [38, 41, 35, 4, 25, 30, 45]
umidades_diarias = [80, 19, 70, 96, 60, 50, 15]
precipitacoes_diarias = [10, 20, 90, 5, 0, 75, 85]

# --- Tarefa 3: Matriz de registros semanais ---
# Matriz 2x5 com valores simulados de temperatura (2 semanas, 5 dias). 
matriz_temperaturas_semanal = [
    [28, 30, 33, 40, 29],  # Semana 1
    [35, 32, 25, 5, 22]    # Semana 2
]

# --- Tarefa 2: Análise condicional com funções ---
def analisar_dados_diarios(temp, umid, precip):
    """
    Aplica regras de decisão simples e retorna uma lista de alertas. 
    """
    alertas_do_dia = []
    # Verifica a temperatura
    if temp >= 40 or temp <= 5:
        alertas_do_dia.append("Alerta de temperatura crítica!") # 
    
    # Verifica a umidade
    if umid <= 20 or umid >= 95:
        alertas_do_dia.append("Alerta de umidade crítica!") # 
        
    # Verifica a precipitação
    if precip >= 80:
        alertas_do_dia.append("Alerta de risco de enchente!") # 
        
    return alertas_do_dia

def analisar_matriz_semanal(matriz_temps):
    """
    Mostra a maior e menor temperatura por semana a partir de uma matriz. 
    """
    print("\n--- Análise Semanal de Temperaturas ---")
    # Itera sobre cada semana na matriz
    for i, semana in enumerate(matriz_temps):
        maior_temp = max(semana)
        menor_temp = min(semana)
        print(f"Semana {i+1}: Maior Temp={maior_temp}°C, Menor Temp={menor_temp}°C")

# --- Função Principal para Orquestrar o Algoritmo ---
def main():
    """
    Função principal que executa o fluxo do programa.
    """
    total_alertas = 0
    print("--- Iniciando Sistema de Monitoramento Climático ClimaCode ---")

    # --- Tarefa 4: Resumo final com repetição ---
    # Loop para processar os dados diários
    for i in range(len(temperaturas_diarias)):
        temp_dia = temperaturas_diarias[i]
        umid_dia = umidades_diarias[i]
        precip_dia = precipitacoes_diarias[i]
        
        print(f"\nAnalisando Dia {i+1}: Temp={temp_dia}°C, Umidade={umid_dia}%, Precipitação={precip_dia}mm")
        
        # Chama a função de análise e recebe os alertas
        alertas = analisar_dados_diarios(temp_dia, umid_dia, precip_dia)
        
        if alertas:
            for alerta in alertas:
                print(f"-> {alerta}")
                total_alertas += 1
        else:
            print("-> Condições normais.")
            
    # Executa a análise da matriz de temperaturas
    analisar_matriz_semanal(matriz_temperaturas_semanal)
    
    # Exibe o resumo final com o total de alertas
    print("\n--- Resumo Final do Período ---")
    print(f"Número total de alertas emitidos: {total_alertas}") # 
    
    # Mensagem final baseada no número de alertas
    if total_alertas > 5:
        print("Mensagem: Risco Alto de Evento Climático Extremo") # 
    else:
        print("Mensagem: Clima sob controle") # 

# --- Execução do Programa ---
if __name__ == "__main__":
    main()