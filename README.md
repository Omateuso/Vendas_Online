# 📊 Análise de Vendas Online

## 📝 Descrição
Este projeto realiza uma análise aprofundada de dados de vendas online utilizando Python, Pandas, Matplotlib, Seaborn e SQLite. O objetivo é transformar dados brutos em insights valiosos por meio de limpeza, processamento, consultas SQL e visualizações gráficas.

## 🚀 Funcionalidades
- 🔹 **Tratamento de Dados:** Preenchimento de valores ausentes, remoção de duplicatas e conversão de tipos para garantir consistência.
- 🔹 **Armazenamento em Banco de Dados:** Exportação dos dados tratados para um banco SQLite para fácil manipulação.
- 🔹 **Consultas SQL:** Extração de informações essenciais, como:
  - Receita total por região.
  - Produtos mais vendidos.
  - Receita mensal consolidada.
  - Métodos de pagamento mais utilizados.
- 🔹 **Visualização de Dados:** Geração de gráficos para melhor interpretação das métricas de vendas.

## 🛠️ Tecnologias Utilizadas
- 🐍 Python
- 📊 Pandas
- 📉 Matplotlib
- 🎨 Seaborn
- 🗄️ SQLite

## 📌 Como Usar
1. Certifique-se de ter o **Python 3.8 ou superior** instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas matplotlib seaborn sqlite3
   ```
3. Certifique-se de que o dataset **OnlineSalesData.csv** está localizado na pasta **DataSet/**.
4. Execute o script principal:
   ```bash
   vendas.py
   ```
5. O programa processará os dados, armazenará no banco de dados SQLite e exibirá os gráficos gerados automaticamente.

📊 Exemplos de Visualizações Geradas
- Total de Vendas por Região: Gráfico de barras comparando o faturamento de diferentes regiões.

- Top 10 Produtos Mais Vendidos: Comparação dos itens mais populares com base na quantidade vendida.

- Receita Mensal ao Longo do Tempo: Gráfico de linha mostrando a evolução das vendas mês a mês
