import mysql.connector

# Conectar ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="he182555@",
    database="sistema_escolar"
)

cursor = db.cursor()

# Funções para manipulação dos dados


def adicionar_aluno(nome, idade, endereco):
    query = "INSERT INTO alunos (nome, idade, endereco) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, idade, endereco))
    db.commit()


def listar_alunos():
    query = "SELECT * FROM alunos"
    cursor.execute(query)
    return cursor.fetchall()


def adicionar_funcionario(nome, cargo):
    query = "INSERT INTO funcionarios (nome, cargo) VALUES (%s, %s)"
    cursor.execute(query, (nome, cargo))
    db.commit()


def listar_funcionarios():
    query = "SELECT * FROM funcionarios"
    cursor.execute(query)
    return cursor.fetchall()


def adicionar_nota(aluno_id, disciplina, nota):
    query = "INSERT INTO notas (aluno_id, disciplina, nota) VALUES (%s, %s, %s)"
    cursor.execute(query, (aluno_id, disciplina, nota))
    db.commit()


def listar_notas_aluno(aluno_id):
    query = "SELECT * FROM notas WHERE aluno_id = %s"
    cursor.execute(query, (aluno_id,))
    return cursor.fetchall()


def adicionar_informacoes_escola(nome_escola, endereco, telefone, diretor):
    query = "INSERT INTO informacoes_escola (nome_escola, endereco, telefone, diretor) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome_escola, endereco, telefone, diretor))
    db.commit()


def obter_informacoes_escola():
    query = "SELECT * FROM informacoes_escola"
    cursor.execute(query)
    return cursor.fetchone()

# Exemplos de Uso


# Adicionar alunos
adicionar_aluno("João", 15, "Rua A, 123")
adicionar_aluno("Maria", 16, "Rua B, 456")

# Listar alunos
print("Alunos:")
for aluno in listar_alunos():
    print(aluno)

# Adicionar funcionários
adicionar_funcionario("José", "Professor")
adicionar_funcionario("Ana", "Secretária")

# Listar funcionários
print("\nFuncionários:")
for funcionario in listar_funcionarios():
    print(funcionario)

# Adicionar notas
adicionar_nota(1, "Matemática", 8.5)
adicionar_nota(1, "Português", 7.0)
adicionar_nota(2, "Matemática", 9.0)
adicionar_nota(2, "Português", 8.0)

# Listar notas de um aluno específico
print("\nNotas do aluno João:")
for nota in listar_notas_aluno(1):
    print(nota)

# Adicionar informações da escola
adicionar_informacoes_escola(
    "Escola XYZ", "Rua C, 789", "(11) 1234-5678", "Fernanda Silva")

# Obter informações da escola
print("\nInformações da Escola:")
print(obter_informacoes_escola())

# Fechar conexão com o banco de dados
db.close()
