# artigo-saude-digital-conasems

## 📊 Estudo e Análise de Experiências do CONASEMS

Este repositório contém os scripts e resultados do estudo que realizou uma raspagem de dados, seleção e análise de experiências do catálogo virtual do CONASEMS. O objetivo foi identificar e categorizar as experiências relacionadas à tecnologia digital em saúde no contexto da APS (Atenção Primária à Saúde).

---

## 🔧 Bibliotecas Utilizadas
- **pandas**: Manipulação e análise de dados.
- **matplotlib**: Visualização de dados.
- **geopandas**: Análise espacial e mapas.
- **numpy**: Operações matemáticas.
- **BeautifulSoup**: Raspagem de dados de HTML.
- **streamlit**: Visualização interativa para seleção manual de dados.

---

## 📂 Estrutura do Projeto

```plaintext
artigo-saude-digital-conasems/
├── .gitignore                       # Arquivos ignorados pelo Git
├── README.md                        # Documentação do projeto
├── Todos os scripts scrapping CONASEMS.ipynb
│   ├── Parte 1 - Raspagem de catálogo de experiências (HTML)
│   ├── Parte 2 - Extração do catálogo para JSON/CSV
│   ├── Parte 3 - Raspagem detalhada das experiências (incluindo todo o relato)
│   └── Parte 4 - Integração dos dados do catálogo com as experiências detalhadas
├── Todos os scripts seleção CONASEMS.ipynb
│   ├── Parte 1 - Destacar termos de busca em formato HTML nos relatos de experiência
│   ├── Parte 2 - Seleção automatizada por termos de busca
├── selecao.py                       # Interface gráfica com Streamlit para visualização dos estudos selecionados e termos destacados
├── Todos os scripts classificação e análise CONASEMS.ipynb
│   ├── Parte 1 - Classificação de termos presentes nos relatos (agrupamento por temas)
│   ├── Parte 2 - Contagem de termos/temas
│   ├── Parte 3 - Categorização dos relatos por UF e Região
│   ├── Parte 4 - Proporção de relatos selecionados por ano (em relação ao total de relatos)
│   └── Parte 5 - Geração de Mapas por UF/ano
├── Dados gerados/
│   ├── lista_itens_CONASEMS.json    # Catálogo inicial (apenas informações básicas sobre as experiências)
│   ├── lista_itens_CONASEMS.csv     # Catálogo inicial (CSV)
│   ├── experiencias_completas_CONASEMS.xlsx # Experiências completas (com todo o relato incluso e demais informações)
│   ├── experiencias_filtradas_CONASEMS.json # Experiências filtradas a partir dos termos de busca
│   ├── experiencias_selecionadas_CONASEMS.json # Experiências selecionadas por critérios de inclusão e exclusão
├── Resultados da análise/
│   ├── contagem_termos_e_temas_por_ano_final.xlsx # Frequências de termos e temas presentes nos relatos, por ano
│   ├── tabelas_frequencia_por_ano.xlsx           # Frequência de relatos selecionados por UF e por Região em cada ano
│   ├── proporcao_estudos_selecionados_ano.xlsx   # Proporção de relatos selecionados em relação ao total de relatos do CONASEMS, por ano
│   ├── mapa_calor_uf_2018.png                    # Mapas por ano
│   ├── mapa_calor_uf_2019.png
│   ├── mapa_calor_uf_2021.png
│   ├── mapa_calor_uf_2022.png
│   └── mapa_calor_uf_total.png                   # Mapa consolidado
´´´

## 🚀 Etapas do Estudo

### 1. 🗂️ Raspagem de Dados (Scrapping)
Os scripts realizam a raspagem do catálogo virtual de experiências do CONASEMS e extraem:
- Informações gerais sobre as experiências.
- Detalhes específicos de cada experiência em páginas individuais.

**Arquivos gerados**:
- `lista_itens_CONASEMS.json` e `lista_itens_CONASEMS.csv`
- `experiencias_completas_CONASEMS.json`, `.csv`, `.xlsx`

---

### 2. 🔍 Seleção de Trabalhos
Os scripts destacam termos relevantes no HTML e fazem uma seleção automatizada com base em palavras-chave relacionadas a tecnologia e APS.

**Arquivos gerados**:
- `experiencias_filtradas_CONASEMS.json`, `.csv`, `.xlsx`

Além disso, foi utilizada uma interface gráfica com o script `selecao.py` (via Streamlit) para seleção manual, resultando em:
- `experiencias_selecionadas_CONASEMS.json`, `.csv`, `.xlsx`

---

### 3. 📊 Classificação e Análise
Scripts para análise e classificação dos trabalhos:
- Listagem de tipos de tecnologia em cada trabalho.
- Contagem de termos e temas mais frequentes.
- Análise por UF, Região e proporção anual de estudos.

**Arquivos gerados**:
- `experiencias_selecionadas_tipos_tecnologia_CONASEMS.json`, `.csv`, `.xlsx`
- `contagem_termos_e_temas_por_ano_final.xlsx`
- `proporcao_estudos_selecionados_ano.xlsx`
- `tabelas_frequencia_por_ano.xlsx`

---

### 4. 🗺️ Mapas
Geração de mapas de calor para visualizar a distribuição das experiências por ano e por UF.

**Arquivos gerados**:
- `mapa_calor_uf_2018.png`, `mapa_calor_uf_2019.png`, `mapa_calor_uf_2021.png`, `mapa_calor_uf_2022.png`
- `mapa_calor_uf_total.png`

📬 Contato
Para dúvidas ou sugestões, entre em contato através do email: gustavo.soibelman@gmail.com

---
