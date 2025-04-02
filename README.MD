### **Etapas do Projeto e Justificativas**  

---

#### **1. Coleta de Dados**  
**O que foi feito:**  
- Extração de dados brutos de um banco SQLite, com tabelas como `dados_gerais`.  
- Consulta SQL para listar tabelas disponíveis e carregar a tabela `dados_gerais` em um DataFrame do Pandas.  

**Por quê:**  
- O banco SQLite já continha dados estruturados da pesquisa [Origem-Destino 2017](https://www.kaggle.com/datasets/sillas/pesquisa-origem-destino-2017-metr-so-paulo?resource=download), garantindo confiabilidade.  
- A extração via SQL permitiu selecionar apenas as tabelas relevantes, evitando sobrecarga de dados.  

---

#### **2. Tratamento e Limpeza**  
**O que foi feito:**  
- **Remoção de colunas nulas:**  
  ```python  
  df_dados_gerais = df_dados_gerais.dropna(axis=1, how='all')  
  ```  
- **Preenchimento de `RENDA_FA`:**  
  ```python  
  df_dados_gerais.fillna({'RENDA_FA': df_dados_gerais['RENDA_FA'].median()}, inplace=True)  
  ```  
- **Criação de `FAIXA_ETARIA`:**  
  ```python  
  bins = [0, 18, 30, 45, 60, 100]  
  labels = ['0-18', '19-30', '31-45', '46-60', '60+']  
  df_dados_gerais['FAIXA_ETARIA'] = pd.cut(df_dados_gerais['IDADE'], bins=bins, labels=labels, right=False)  
  ```  

**Por quê:**  
- **Colunas nulas:** Foram removidas para simplificar a análise e reduzir ruídos.  
- **Preenchimento com mediana:** Evitou distorções por outliers e manteve a distribuição original de renda.  
- **Faixa etária categorizada:** Transformar idade numérica em categorias facilitou a análise segmentada.  

---

#### **3. Análise Exploratória (SQL)**  
**O que foi feito:**  
- Consultas para identificar:  
  - **Top 10 zonas com mais viagens:**  
    ```sql  
    SELECT COD_ZONA_ORIGEM, COUNT(*) AS total_viagens  
    FROM viagens_diarias  
    GROUP BY COD_ZONA_ORIGEM  
    ORDER BY total_viagens DESC  
    LIMIT 10;  
    ```  
  - **Renda média por zona:**  
    ```sql  
    SELECT ZONA, AVG(RENDA_FA) AS renda_media  
    FROM dados_gerais  
    GROUP BY ZONA  
    ORDER BY renda_media DESC;  
    ```  

**Por quê:**  
- Identificar zonas críticas (alta demanda de viagens e baixa renda) direcionou o foco para áreas prioritárias de intervenção.  

---

#### **4. Visualização no Power BI**  
**O que foi feito:**  
- Criação de gráficos interativos:  
  - **Tempo médio de deslocamento por renda familiar**.  
  - **Média de renda por faixa etária**.  
  - **Percentual de estudantes com deslocamento entre 30-120 minutos**.  
  - **Total de famílias/pessoas por faixa etária**.  

**Por quê:**  
- **Gráfico de dispersão:** Mostra a relação clara entre renda e tempo de deslocamento, reforçando a desigualdade.  
- **Gráfico de barras:** Destaca picos de renda em faixas etárias específicas.  
- **Gráfico de pizza:** Simplifica a compreensão de proporções.  
- **Filtros interativos:** Permitem explorar dados por idade, tornando a análise flexível.  

---

#### **5. Storytelling e Personas**  
**O que foi feito:**  
- Criação de personas como **Ana (22 anos)** e **Carlos (50 anos)** para ilustrar contrastes:  
  - Ana: Baixa renda, deslocamento longo (ônibus).  
  - Carlos: Alta renda, deslocamento curto (carro).  

**Por quê:**  
- **Humanizar os dados:** Facilita a conexão emocional e a compreensão do impacto social.  
- **Comunicação não técnica:** Ajuda gestores públicos a visualizarem problemas reais.  

---

### **Por Que Essa Abordagem Funcionou?**  
1. **Foco em Dados Relevantes:**  
   - A categorização de `FAIXA_ETARIA` evitaram análise dispersa.  
2. **Ferramentas Complementares:**  
   - **Python:** Ideal para tratamento massivo de dados.  
   - **SQL:** Eficaz para consultas rápidas e agregações.  
   - **Power BI:** Permitiu visualizações interativas e acessíveis.  
3. **Narrativa Baseada em Evidências:**  
   - Todas as decisões foram respaldadas por padrões estatísticos, garantindo credibilidade.  