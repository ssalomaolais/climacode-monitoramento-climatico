# ClimaCode: Previsão de Eventos Extremos com Lógica em Python

![Instituição](https://img.shields.io/badge/FIAP-Global%20Solution-red) 
![Linguagem](https://img.shields.io/badge/Linguagem-Python-3776AB?logo=python)
![Disciplina](https://img.shields.io/badge/Disciplina-Pensamento%20Computacional-blue) 
## 📖 Sobre o Projeto

**ClimaCode** é um projeto acadêmico desenvolvido para a Global Solution da disciplina de "Pensamento Computacional e Automação com Python" do curso de Ciência da Computação da FIAP.

O objetivo do projeto é simular um sistema de monitoramento e alerta climático.O algoritmo utiliza estruturas de repetição, condicionais, funções e a manipulação de vetores e matrizes para analisar dados ambientais simulados e identificar potenciais eventos climáticos extremos, como ondas de calor, frio intenso, umidade crítica e risco de enchentes.

**Autora:**
* Laís Salomão

## ✔️ Tarefas Implementadas

O código implementa todas as tarefas obrigatórias definidas na avaliação:

1.  **Entrada de Dados Ambientais:** Utiliza vetores (listas em Python) para armazenar dados simulados de uma semana de temperatura, umidade e precipitação.
2. **Análise Condicional com Funções:** Uma função `analisar_dados_diarios` verifica os dados de cada dia com base em regras pré-definidas e emite alertas:
    * "Alerta de temperatura crítica!" se a temperatura for $\ge40^{\circ}C$ ou $\le5^{\circ}C$.
    * "Alerta de umidade crítica!" se a umidade for $\le20\%$ ou $\ge95\%$.
    * "Alerta de risco de enchente!" se a precipitação for $\ge80mm$.
3.  **Matriz de Registros Semanais:** Uma matriz 2x5 armazena temperaturas de duas semanas, e uma função `analisar_matriz_semanal` calcula e exibe a maior e a menor temperatura de cada semana.
4.  **Resumo Final com Repetição:** Um loop processa os dados diários, e ao final, o sistema exibe o número total de alertas emitidos. Com base nesse total, uma mensagem final é exibida:
    * "Risco Alto de Evento Climático Extremo" se mais de 5 alertas forem emitidos.
    * "Clima sob controle" caso contrário.

## 🚀 Como Executar

O projeto consiste em um único script Python. Para executá-lo, basta ter o Python instalado em sua máquina.

1.  **Clone o repositório (ou tenha o arquivo `clima_code.py` em uma pasta):**
    ```bash
    git clone [https://github.com/SEU-USUARIO/climacode-monitoramento-climatico.git](https://github.com/SEU-USUARIO/climacode-monitoramento-climatico.git)
    cd climacode-monitoramento-climatico
    ```

2.  **Execute o script através do terminal:**
    ```bash
    python clima_code.py
    ```
