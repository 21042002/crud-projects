import sqlite3, re, time

# Conectando ao banco de dados
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criação da tabela
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT,
        email TEXT,
        idade INTEGER )""")


create_table()

# Cadastro de user 
def inserir_usuario():
    nome = input("\nDigite nome completo: ").strip()

    # Validação de dados
    if len(nome) <= 3:
        print("Erro: O nome deve ter pelo menos 3 caracteres.")

    try:
        idade = input("Digite a idade: ").strip()
        idade = int(idade)
        if idade < 0 or idade > 120:
            print("Erro: Idade inválida.")
        elif idade < 18:
            print("Aviso: Usuário menor de idade.")
    except ValueError:
        print("Erro: A idade deve ser um número.")

    email = input("\nDigite o seu email: ").strip()

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Erro: Formato de e-mail inválido.")
    else:
        cursor.execute("SELECT email FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            print("Erro: Este e-mail já está cadastrado.")

    cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (?,?,?)", (nome, email, idade))
    
    conexao.commit()
    print('Dados inseridos com sucesso!')


# Consutar dados 
def consultar_user():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário encontrado.")
    else:
        print(f"\nSegue todos os usuários: \n{usuarios}")

def atualizar_idade(user_id, idade):
    cursor.execute("""
        UPDATE usuarios
        SET idade = ? 
        WHERE id = ?
    """,(idade, user_id))

    conexao.commit()
    print("Dados atualizado com sucesso!")

def deletar_usuario(usuario_id):
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id))

    conexao.commit()
    print("Usuário deletado com sucesso.")


# Validação: Não permitir email duplicado | Não permitir menor de idade

# Cadastro de usuario 
while True:
    print("\n ====== CADASTRO DE CLIENTES ========")
    print("MENU: \n1. Cadastrar cliente. \n2. Verificar todos os clientes") 
    print("3. Atualizar idade. \n4. Deletar usuário \n5. Sair.")

    opcao = input("\nDigite a opção: ")

    if opcao == "1":
        inserir_usuario()

    elif opcao == "2":
        consultar_user()

    elif opcao == "3":
        id_user = input("\nDigite o id do usuário que deseja alterar: ").strip()
        idade = input("Digite a idade: ").strip()

        atualizar_idade(id_user, idade)

    elif opcao == "4":
        delete_user = input('\nDigite o "id" do usuario para excluir: ').strip()

        deletar_usuario(delete_user)
    elif opcao == "5":
        time.sleep(2)
        print("Saindo...")
        break
    
    else:
        print("\nDigite uma das opções.")

print("Encerramento da conexão...")
conexao.close()