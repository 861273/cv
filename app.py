from pathlib import Path
import streamlit as st
from PIL import Image

# Configurações Estruturais #
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_css = diretorio / "styles" / "geral.css"
arquivo_pdf = diretorio / "assets" / "Curriculum.pdf"
arquivo_img = diretorio / "assets" / "fr.jpeg"

# Configurações Geral das Informações #

TITULO = "Curriculum | Rodrigo de Sousa Rodrigues"
NOME = "Rodrigo de Sousa Rodrigues"
DESCRICAO = """
    Assistente Administrativo Pleno com 3 anos de atuação em empresas comerciais. Especializado na organização e gerenciamento das atividades diárias, com foco na modernização de processos visando o aumento da produtividade geral. Destaque para habilidades de planejamento, comunicação, resolução de problemas, bem como criatividade para implementar novas ideias para melhoria de processos.
"""
EMAIL = "liverodrigo1@gmail.com"
MIDIA_SOCIAL = {
    "LinkedIn": "https://www.linkedin.com/in/rodrigo-rodrigues-927591204/",
    "GitHub": "https://github.com/861273",
    "VSCO": "http://vsco.co/rod-1-2"
}

CURSOS = {
    "🎯 11/2012 - MBA Gestão Portuária, Logística Empresarial e Negociação Internacional - Laboro - São Luís ":"",
    "🎯 07/2022 - MBA Gestão Estratégica de Pessoas - Administração de Pessoal - INEX - São Luís ":"",
    "🎯 06/2021 - Graduação: Gestão Comercial - Cruzeiro do Sul - São Luís ":"",
    "🎯 12/2021 - Curso de Comércio Exterior COMEX .220 : Comércio Exterior - Concept Trading - São Luís, MA - 40 horas ":"",
    "🎯 06/2021 - Curso online English in Brazil : Inglês - 200 horas - English In Brazil by Carina Fragoso - São Paulo, SP  ":"",
    "🎯 05/2023 - Curso de Assistente Administrativo Portuário: Tranship ":"",
    "🎯 05/2023 - Curso de Inglês Técnico Portuário: Tranship":"",
    "🎯 11/2023 - Análise de Dados com Python":"",
    "🎯 11/2023 - Desenvolvendo Dashboards e Data Apps com Streamlit [2023]":"",
    "🎯 02/2022 - Power Bi Expert na Prática - VISCARI":"",
    "🎯 11/2022 - 38300 - Power Bi Data Analyst (PL-300) - Ka Solution":"",
    "🎯 11/2023 - MYSQL [40HORAS] Curso em Vídeo":"",
    "🎯 11/2023 - Excel do Zero ao Avançado - Aline Elias Treinamento e Desenvolvimento LTD":"",
    "🎯 11/2023 - Curso online English in Brazil by Carina Fragoso - São Paulo, SP: Inglês - 200 horas ":"",
}

st.set_page_config(
    page_title=TITULO
)

# Carregando Assets #

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()), unsafe_allow_html=True)
with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_img)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(imagem, width=250)
with col2:
    st.title(NOME)
    st.write(DESCRICAO)
    st.download_button(
        label="Download Curriculum",
        data=pdfLeitura,
        file_name=arquivo_pdf.name,
        mime="application/octet-stream"
    )
    st.write("✉️", EMAIL)

# Mídias Sociais #
st.write("#")
colunas = st.columns(len(MIDIA_SOCIAL))
for indice, (plataforma, link) in enumerate(MIDIA_SOCIAL.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# Experiências #
st.write("#")
st.subheader("Experiências")
st.write(
    """        
        - 💹 Participei da implantação da filial da Rofe Distribuidora em Belém - PA. Ministração de treinamento das atividades e sistemas relacionados a montagem de cargas dentro do processo logístico;   
        - 💹 Treinamento para as atividade de análise de entregas em Nova Hamburgo - RS;
    """
)

# Skills #
st.write("#")
st.subheader("Skills")
st.write(
    """
      - 📉 Visualização de Dados: Power BI
      - 📊 Tratamento de bases e criação de relatórios com Excel Avançado
      - 📝 Organizaçao, Planejamento e Criatividade
      - 🖥️ Operação de sistemas ERP como Winthor, Fusion Track DMS e CISSPoder
      - 🗽 Inglês Intermediário: B1
    """
)

# Histórico de Trabalho #
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

# Job 1 #
st.write("📜", "**Assistente Administrativo Pleno - Revest**")
st.write("02/2023 -  Atualmente")
st.write(
    """
        - 💹 Levantamento de dados e produção de todos os indicadores logísticos, com base na estipulação de metas, apuração e acompanhamento.
        - 💹 Produção de dashboards no Power Bi para a visualização de dados e tomada de decisões.
        - 💹 Produção de relatórios em Excel conforme a necessidade do setor.
        """
)

# Job 2 #
st.write("📜", "**Analista de Entregas - Calçados Beira Rio**")
st.write("01/2023 - 02/2023")
st.write(
    """
        - 💹 Responsável pelo pós-vendas, emissão de notas de devolução, suporte aos clientes internos e externos.
        - 💹 Produção de dashboards para acompanhamento das devoluções de todos os representantes da regional.
        - 💹 Organizão do showroom.        
    """
)

# Job 3 #
st.write("📜", "**Assistente de Transporte II  - Rofe Distribuidora**")
st.write("04/2019 - 12/2022")
st.write(
    """
        - 💹 Roteirização, montagem de cargas, feedbacks aos motoristas e clientes.
        - 💹 Produção de dashboards para acompanhamento das notas fiscais fora de carregamento.
        - 💹 Acompanhamento e preenchimento em Excel dos indicadores do setor de transporte.        
    """
)

# Job 4 #
st.write("📜", "**Consultor de Vendas - E-Galeno**")
st.write("12/2017 - 10/2018")
st.write(
    """
        - 💹 Criação de novos clientes, venda de mais produtos para clientes antigos e atuação como solucionador de problemas do cliente.
        - 💹 Panfletagem em prédios, estacionamentos e vias públicas.      
    """
)

# Job 4 #
st.write("📜", "**Técnico em Segurança do Trabalho - SempreVerde Jardins LTDA**")
st.write("06/2008 - 12/2009")
st.write(
    """
        - 💹 Informar o empregador, através de parecer técnico, planilhas, gráficos e outros recursos sobre os riscos exigentes nos ambientes de trabalho; Levantamento de riscos existentes do ambiente de trabalho e orientações sobre eliminação e neutralização dos mesmos; Análise de métodos e processos do trabalho, identificando fatores de risco de acidente, doenças do trabalho, propondo eliminação ou controle desses riscos; Promoção de debates, encontros, campanhas, seminários, palestras, reuniões, treinamentos e utilização de outros recursos de ordem didática.
    """
)

# Cursos #
st.write("#")
st.subheader("Formações e Cursos")
st.write("---")
for curso, link in CURSOS.items():
    st.write(f"[{curso}]({link})")