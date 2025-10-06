import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno

st.set_page_config(page_title="gerenciamento de alunos", page_icon="")

st.title("Sistemas de alunos com postgreSQl")

menu = st.sidebar.radio("menu", ["inserir", "Listar", "Atualizar", "Deletar"])

if menu == "inserir":
    st.subheader("Inserir alunos")
    nome = st.text_input("Nome", placeholder="Seu nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} inserido com sucesso!")
        else:
            st.warning("O campo nome não pode ser vazio")



elif menu == "lista":
    st.subheader("listar alunos")
    alunos = listar_alunos
    if alunos:
        for linha in alunos:
            st.write(f"ID={linha[0]} | NOME={linha[1]} | IDADE{linha[2]}")
    else:
        st.info("nenhum aluno encontrado.")

