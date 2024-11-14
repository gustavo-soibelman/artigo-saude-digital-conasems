import streamlit as st
import pandas as pd
import math

# Carregar o arquivo JSON filtrado
data = pd.read_json("experiencias_filtradas_CONASEMS.json", orient="records", lines=True)

# Selecionar as colunas de interesse
colunas_selecionadas = [
    'id', 'titulo', 'cidade', 'estado', 'ano', 'autoria', 'coautoria', 'resumo_completo_html', 'link_experiencia'
]
data = data[colunas_selecionadas]

# Definir o número de artigos por página
artigos_por_pagina = 20

# Calcular o número total de páginas
total_paginas = math.ceil(len(data) / artigos_por_pagina)

# Controle da página atual
pagina_atual = st.number_input("Página", min_value=1, max_value=total_paginas, step=1, value=1)

# Calcular o índice inicial e final para a página atual
inicio = (pagina_atual - 1) * artigos_por_pagina
fim = inicio + artigos_por_pagina

# Filtrar os dados para a página atual
dados_paginados = data.iloc[inicio:fim]

# Exibir cada artigo na página atual
st.title(f"Página {pagina_atual} de {total_paginas}")
for index, row in dados_paginados.iterrows():
    st.write(f"**ID:** {row['id']}")
    st.write(f"**Título:** {row['titulo']}")
    st.write(f"**Cidade:** {row['cidade']}")
    st.write(f"**Estado:** {row['estado']}")
    st.write(f"**Ano:** {row['ano']}")
    st.write(f"**Autoria:** {row['autoria']}")
    st.write(f"**Coautoria:** {row['coautoria']}")
    
    # Renderizar o conteúdo HTML em resumo_completo_html
    st.markdown(row['resumo_completo_html'], unsafe_allow_html=True)
    
    # Link para a experiência
    st.write(f"[Link para Experiência]({row['link_experiencia']})")
    
    # Linha de separação entre artigos
    st.markdown("---")
