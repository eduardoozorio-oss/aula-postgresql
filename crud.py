from db import conectar

def criar_aluno(nome, idade):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO alunos (nome, idade) VALUES (%s, %s)",
                (nome, idade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar aluno: {erro}")
        finally:
            cursor.close()
            conexao.close()  

def listar_alunos():
    conexao, cusor = conectar()
    if conexao:
        try:
            cusor.execute("SELECT * FROM alunos ORDER BY id")
            return cusor.fetchall()
        except Exception as erro:
            print(f"erro ao tentar listar alunos: {erro}")
        finally:
            cusor.close()
            conexao.close()

def atualizar_idade(id_aluno, nova_idade):
    conexao, cusor = conectar()
    if conexao:
        try:
            cusor.execute(
                "UPDATE alunos SET idade = %s WHERE id = %s"
                (nova_idade, id_aluno)
                )
            conexao.comit()
        except Exception as erro:
            print(f"erro ao tentar listar alunos: {erro}")
        finally:
            cusor.close()
            conexao.close()

id = int(input("digite o id do alunoque deseja atualizar:"))
nova_idade = int(input("digite a nova idade:"))
atualizar_idade(id, nova_idade)


    