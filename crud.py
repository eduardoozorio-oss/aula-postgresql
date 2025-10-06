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

lista = listar_alunos()
print(lista)
for aluno in lista:
    print(aluno)
    