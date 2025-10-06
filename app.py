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



elif menu == "Atualizar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_alunos = st.selectbox("EScolha o id do aluno para atualizar", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=16, step=1)
        if st.button("Atuaizar"):
            atualizar_idade(id_alunos, nova_idade)
            st.success(f"Idade do aluno atualizando com sucesso.")
    else:
        st.info("Nenhum aluno disponivel para atulizar.")




elif menu == "Deletar":
    st.subheader("Atualizar idade")
    alunos = listar_alunos()
    if alunos:
        id_alunos = st.selectbox("EScolha o id do aluno para atualizar", [linha[0] for linha in alunos])
        nova_idade = st.number_input("Nova idade", min_value=16, step=1)
        if st.button("Deletar"):
            deletar_aluno(id_alunos, nova_idade)
            st.success(f"aluno deletado com sucesso.")
    else:
        st.info("Nenhum aluno disponivel para atulizar.")