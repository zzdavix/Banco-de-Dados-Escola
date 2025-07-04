import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha',
    database='escola',
)

cursor = conexao.cursor()


################################################################ MENU #########################################################################
def exibir_menu():
    print()
    print("====== MENU PRINCIPAL ======")
    print()
    print("1. Inserir")
    print("2. Alterar")
    print("3. Pesquisar por nome")
    print("4. Remover")
    print("5. Listar todos")
    print("6. Exibir um")
    print("7. Exibir view")
    print("8. Chamar stored procedure")
    print("9. Sair")


############################################################## INSERIR ###########1#############################################################
def insere_aluno(nome, mat, turma):
    try:
        comando = 'INSERT INTO aluno (nome, mat, turma) VALUES (%s, %s, %s)'
        cursor.execute(comando, (nome, mat, turma))
        conexao.commit()
        print("Aluno inserido com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir aluno: {err}\n")


def insere_prof(nome, matricula, disciplina, salario):
    try:
        comando = 'INSERT INTO professor (nome, matricula, disciplina, salario) VALUES (%s, %s, %s, %s)'
        cursor.execute(comando, (nome, matricula, disciplina, salario))
        conexao.commit()
        print("Professor inserido com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir professor: {err}\n")

def insere_disc(nome, cod):
    try:
        comando = 'INSERT INTO disciplina (nome, cod) VALUES (%s, %s)'
        cursor.execute(comando, (nome, cod))
        conexao.commit()
        print("Disciplina inserida com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao inserir disciplina: {err}\n")

def matricula_aluno(mat, cod):
    try:
        conta_aluno = 'SELECT COUNT(*) FROM matricula WHERE disciplina_cod = %s' #Limite de 3 alunos por disciplina
        cursor.execute(conta_aluno, (cod,))
        total_matriculados = cursor.fetchone()[0]
        limite = 3

        if total_matriculados < limite:
            comando = 'INSERT INTO matricula (aluno_mat, disciplina_cod) VALUES (%s, %s)'
            cursor.execute(comando, (mat, cod))
            conexao.commit()
            print("Matricula inserida com sucesso!\n")
        else:
            print(f"Limite de {limite} alunos atingido para a disciplina {cod}.\n")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir matricula: {err}\n")
        

############################################################## ALTERAR ALUNO ########################################################################
def altera_nome_aluno(Novonome, Matricula):
    try:
        comando = 'UPDATE aluno SET nome = %s WHERE mat = %s'
        cursor.execute(comando, (Novonome, Matricula))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.\n")
        else:
            print("Nome do aluno alterado com sucesso!\n")

    except mysql.connector.Error as err:
        print(f"Erro ao alterar nome do aluno: {err}\n")


def altera_matricula_aluno(Novamatricula, Matricula):
    try:
        comando = 'UPDATE aluno SET mat = %s WHERE mat = %s'
        cursor.execute(comando, (Novamatricula, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Aluno não encontrado. Matrícula não alterada.\n")
        else:
            print("Matrícula do aluno alterada com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar matrícula do aluno: {err}\n")

def altera_turma_aluno(Novaturma, Matricula):
    try:
        comando = 'UPDATE aluno SET turma = %s WHERE mat = %s'
        cursor.execute(comando, (Novaturma, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Aluno não encontrado. Turma não alterada.\n")
        else:
            print("Turma do aluno alterada com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar turma do aluno: {err}\n")


############################################################## ALTERAR PROFESSOR ########################################################################
def altera_nome_professor(Novonome, Matricula):
    try:
        comando = 'UPDATE professor SET nome = %s WHERE matricula = %s'
        cursor.execute(comando, (Novonome, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Professor não encontrado. Nome não alterado.\n")
        else:
            print("Nome do professor alterado com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar nome do professor: {err}\n")

def altera_matricula_professor(Novamatricula, Matricula):
    try:
        comando = 'UPDATE professor SET matricula = %s WHERE matricula = %s'
        cursor.execute(comando, (Novamatricula, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Professor não encontrado. Matrícula não alterada.\n")
        else:
            print("Matrícula do professor alterada com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar matrícula do professor: {err}\n")

def altera_disciplina_professor(Novadisc, Matricula):
    try:
        comando = 'UPDATE professor SET disciplina = %s WHERE matricula = %s'
        cursor.execute(comando, (Novadisc, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Professor não encontrado. Disciplina não alterada.\n")
        else:
            print("Disciplina do professor alterada com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar disciplina do professor: {err}\n")

def altera_salario_professor(Novosal, Matricula):
    try:
        comando = 'UPDATE professor SET salario = %s WHERE matricula = %s'
        cursor.execute(comando, (Novosal, Matricula))
        conexao.commit()
        
        if cursor.rowcount == 0:
            print("Professor não encontrado. Salário não alterado.\n")
        else:
            print("Salário do professor alterado com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar salário do professor: {err}\n")


############################################################## ALTERAR DISCIPLINA ########################################################################
def altera_nome_disc(Novonome, Codigo):
    try:
        comando = 'UPDATE disciplina SET nome = %s WHERE cod = %s'
        cursor.execute(comando, (Novonome, Codigo))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Disciplina não encontrada. Nome não alterado.\n")
        else:
            print("Nome da disciplina alterado com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar nome da disciplina: {err}\n")

def altera_cod_disc(Novocod, Codigo):
    try:
        comando = 'UPDATE disciplina SET cod = %s WHERE cod = %s'
        cursor.execute(comando, (Novocod, Codigo))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Disciplina não encontrada. Código não alterado.\n")
        else:
            print("Código da disciplina alterado com sucesso!\n")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar código da disciplina: {err}\n")


############################################################## REMOVER #########################################################################
def remove_aluno(mat):
    try:
        comando = 'DELETE FROM aluno WHERE mat = %s'
        cursor.execute(comando, (mat,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.\n")
        else:
            print("Aluno removido com sucesso!\n")

    except mysql.connector.Error as err:
        print(f"Erro ao remover aluno: {err}\n")

def remove_prof(mat):
    try:
        comando = 'DELETE FROM professor WHERE matricula = %s'
        cursor.execute(comando, (mat,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Professor não encontrado.\n")
        else:
            print("Professor removido com sucesso!\n")

    except mysql.connector.Error as err:
        print(f"Erro ao remover professor: {err}\n")

def remove_disc(cod):
    try:
        comando = 'DELETE FROM disciplina WHERE cod = %s'
        cursor.execute(comando, (cod,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Disciplina não encontrada.\n")
        else:
            print("Disciplina removida com sucesso!\n")

    except mysql.connector.Error as err:
        print(f"Erro ao remover disciplina: {err}\n")

def remove_mat(mat, cod):
    try:
        comando = 'DELETE FROM matricula WHERE aluno_mat = %s AND disciplina_cod = %s'
        cursor.execute(comando, (mat, cod,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Matricula não encontrada.\n")
        else:
            print("Matricula removida com sucesso!\n")

    except mysql.connector.Error as err:
        print(f"Erro ao remover matricula: {err}\n")


################################################################ PESQUISAR POR NOME ##########################################################################
def busca_aluno(nome):
    try:
        comando = 'SELECT * FROM aluno WHERE nome LIKE %s ORDER BY id'
        cursor.execute(comando, (f"{nome}%",))
        resultado = cursor.fetchall()

        if not resultado:
            print(f"Nenhum aluno encontrado com o nome '{nome}'.\n")
        else:
            print()
            for linha in resultado:
                print(linha)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao buscar aluno: {err}\n")

def busca_prof(nome):
    try:
        comando = 'SELECT * FROM professor WHERE nome LIKE %s ORDER BY id'
        cursor.execute(comando, (f"{nome}%",))
        resultado = cursor.fetchall()

        if not resultado:
            print(f"Nenhum professor encontrado com o nome '{nome}'.\n")
        else:
            print()
            for linha in resultado:
                print(linha)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao buscar professor: {err}\n")


def busca_disc(cod):
    try:
        comando = 'SELECT * FROM disciplina WHERE cod LIKE %s ORDER BY id'
        cursor.execute(comando, (f"{cod}%",))
        resultado = cursor.fetchall()

        if not resultado:
            print(f"Nenhuma disciplina encontrada com o codigo '{cod}'.\n")
        else:
            print()
            for linha in resultado:
                print(linha)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao buscar disciplina: {err}\n")


################################################################ EXIBIR UM ########################################################################
def exibe_aluno(ID):
    try:
        comando = 'SELECT * FROM aluno WHERE id = %s'
        cursor.execute(comando, (ID,))
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Aluno não encontrado.\n")
        else:
            print()
            for aluno in resultado:
                print(aluno)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao exibir aluno: {err}\n")


def exibe_prof(ID):
    try:
        comando = 'SELECT * FROM professor WHERE id = %s'
        cursor.execute(comando, (ID,))
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Professor não encontrado.\n")
        else:
            print()
            for professor in resultado:
                print(professor)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao exibir professor: {err}\n")

def exibe_disc(ID):
    try:
        comando = 'SELECT * FROM disciplina WHERE id = %s'
        cursor.execute(comando, (ID,))
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Disciplina não encontrada.\n")
        else:
            print()
            for disciplina in resultado:
                print(disciplina)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao exibir disciplina: {err}\n")


################################################################ LISTAR TODOS ##########################################################################
def lista_aluno():
    try:
        comando = f'SELECT * FROM aluno ORDER BY id'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Nenhum aluno cadastrado.\n")
        else:
            print()
            for aluno in resultado:
                print(aluno)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao listar alunos: {err}\n")


def lista_prof():
    try:
        comando = f'SELECT * FROM professor ORDER BY id'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Nenhum professor cadastrado.\n")
        else:
            print()
            for professor in resultado:
                print(professor)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao listar professores: {err}\n")

def lista_disc():
    try:
        comando = f'SELECT * FROM disciplina ORDER BY id'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        
        if not resultado:
            print("Nenhuma disciplina cadastrada.\n")
        else:
            print()
            for disciplina in resultado:
                print(disciplina)
            print()
    except mysql.connector.Error as err:
        print(f"Erro ao listar disciplinas: {err}\n")


################################################################ EXIBIR VIEW ##########################################################################
def exibir_view_turmas():
    try:
        comando = f'SELECT * FROM vw_aluno_professor_disciplina ORDER BY nome_aluno'
        cursor.execute(comando)
        resultados = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        larguras = [20, 20, 20, 20, 15]

        print()
        for i, col in enumerate(colunas):
            print(col.ljust(larguras[i]), end=' | ')
        print("\n" + "-" * sum(larguras))


        for linha in resultados:
            for i, item in enumerate(linha):
                print(str(item).ljust(larguras[i]), end=' | ')
            print()

    except mysql.connector.Error as err:
        print(f"Erro ao buscar dados: {err}\n")

def exibir_view_aluno_turma():
    try:
        comando = f'SELECT * FROM vw_aluno_turma ORDER BY nome_aluno'
        cursor.execute(comando)
        resultados = cursor.fetchall()

        colunas = [desc[0] for desc in cursor.description]
        larguras = [25, 25, 10]

        print()
        for i, col in enumerate(colunas):
            print(col.ljust(larguras[i]), end=' | ')
        print("\n" + "-" * sum(larguras))


        for linha in resultados:
            for i, item in enumerate(linha):
                print(str(item).ljust(larguras[i]), end=' | ')
            print()

    except mysql.connector.Error as err:
        print(f"Erro ao buscar dados: {err}\n")

################################################################ STORED PROCEDURES ##########################################################################
def exibir_alunos_por_disciplina(cod_disciplina):
    try:
        cursor.callproc('sp_exibir_alunos_por_disciplina', [cod_disciplina])

        for resultado in cursor.stored_results():
            dados = resultado.fetchall()
            colunas = [desc[0] for desc in resultado.description]
            larguras = [25, 20, 10, 15]

        print()
        for i, col in enumerate(colunas):
            print(col.ljust(larguras[i]), end=' | ')
        print("\n" + "-" * sum(larguras))

        for linha in dados:
            for i, item in enumerate(linha):
                print(str(item).ljust(larguras[i]), end=' | ')
            print()

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou buscar dados: {erro}")

def exibir_disciplinas_por_aluno(matricula_aluno):
    try:
        cursor.callproc('sp_disciplinas_por_aluno', [matricula_aluno])

        for resultado in cursor.stored_results():
            dados = resultado.fetchall()
            colunas = [desc[0] for desc in resultado.description]
            larguras = [25, 20, 30, 20]
        
        print()
        for i, col in enumerate(colunas):
            print(col.ljust(larguras[i]), end=' | ')
        print("\n" + "-" * sum(larguras))

        for linha in dados:
            for i, item in enumerate(linha):
                print(str(item).ljust(larguras[i]), end=' | ')
            print()

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou buscar dados: {erro}")

################################################################ MAIN ##########################################################################
def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")


############################################################## INSERIR ########################################################################
        if escolha == '1':
            while True:
                print("\n====== SELECIONE UMA OPCAO ======")
                print()
                print("1. Aluno")
                print("2. Professor")
                print("3. Disciplina")
                print("4. Matricular Aluno")
                print("5. Voltar")
                tipo = input("Escolha uma opção: ")
                
                if tipo == '1':
                    nome = input("Digite o nome do aluno: ")
                    mat = input("Digite a matrícula do aluno: ")
                    turma = input("Digite a turma do aluno: ")
                    insere_aluno(nome, mat, turma)

                elif tipo == '2':
                    nome = input("Digite o nome do professor: ")
                    matricula = input("Digite a matrícula do professor: ")
                    disciplina = input("Digite o código da disciplina do professor: ")
                    salario = input("Digite o salário do professor: ")
                    insere_prof(nome, matricula, disciplina, salario)

                elif tipo == '3':
                    nome = input("Digite o nome da disciplina: ")
                    cod = input("Digite o código da disciplina: ")
                    insere_disc(nome, cod)

                elif tipo == '4':
                    mat = input("Digite a matricula do aluno: ")
                    cod = input("Digite o código da disciplina: ")
                    matricula_aluno(mat, cod)

                elif tipo == '5':
                    break

                else:
                    print("Digite um valor válido")


############################################################## ALTERAR ########################################################################
        elif escolha == '2':
            while True:
                print("\nSELECIONE UMA OPÇÃO =====")
                print()
                print("1. Aluno")
                print("2. Professor")
                print("3. Disciplina")
                print("4. Voltar")
                tipo = input("Escolha uma opção: ")

                if tipo == '1':
                    while True:
                        print("\nO QUE DESEJA ALTERAR? ======")
                        print()
                        print("1. Nome")
                        print("2. Matrícula")
                        print("3. Turma")
                        print("4. Voltar")
                        opcao = input("Escolha uma opção: ")

                        if opcao == '1':
                            Matricula = input("Digite a matrícula do aluno: ")
                            Novonome = input("Digite o novo nome do aluno: ")
                            altera_nome_aluno(Novonome, Matricula)

                        elif opcao == '2':
                            Matricula = input("Digite a matrícula do aluno: ")
                            Novamatricula = input("Digite a nova matrícula do aluno: ")
                            altera_matricula_aluno(Novamatricula, Matricula)

                        elif opcao == '3':
                            Matricula = input("Digite a matrícula do aluno: ")
                            Novaturma = input("Digite a nova turma do aluno: ")
                            altera_turma_aluno(Novaturma, Matricula)

                        elif opcao == '4':
                            break  

                elif tipo == '2':
                    while True:
                        print("\nO QUE DESEJA ALTERAR? ======")
                        print()
                        print("1. Nome")
                        print("2. Matrícula")
                        print("3. Disciplina")
                        print("4. Salário")
                        print("5. Voltar")
                        opcao = input("Escolha uma opção: ")

                        if opcao == '1':
                            Matricula = input("Digite a matrícula do professor: ")
                            Novonome = input("Digite o novo nome do professor: ")
                            altera_nome_professor(Novonome, Matricula)

                        elif opcao == '2':
                            Matricula = input("Digite a matrícula do professor: ")
                            Novamatricula = input("Digite a nova matrícula do professor: ")
                            altera_matricula_professor(Novamatricula, Matricula)

                        elif opcao == '3':
                            Matricula = input("Digite a matrícula do professor: ")
                            Novadisc = input("Digite a nova disciplina do professor: ")
                            altera_disciplina_professor(Novadisc, Matricula)

                        elif opcao == '4':
                            Matricula = input("Digite a matrícula do professor: ")
                            Novosal = input("Digite o novo salário do professor: ")
                            altera_salario_professor(Novosal, Matricula)
                        
                        elif opcao == '5':
                            break  
                    

                elif tipo == '3':
                    while True:
                        print("\nO QUE DESEJA ALTERAR? ======")
                        print()
                        print("1. Nome")
                        print("2. Código")
                        print("3. Voltar")
                        opcao = input("Escolha uma opção: ")

                        if opcao == '1':
                            Codigo = input("Digite o código da disciplina: ")
                            Novonome = input("Digite o novo nome da disciplina: ")
                            altera_nome_disc(Novonome, Codigo)

                        elif opcao == '2':
                            Codigo = input("Digite o código da disciplina: ")
                            Novocod = input("Digite o novo código da disciplina: ")
                            altera_cod_disc(Novocod, Codigo)

                        elif opcao == '4':
                            break

                elif tipo == '4':
                    break


########################################################## PESQUISAR POR NOME ################################################################### 
        elif escolha == '3':
            while True:
                print("\n====== SELECIONE O QUE DESEJA BUSCAR ======")
                print()
                print("1. Aluno")
                print("2. Professor")
                print("3. Disciplina")
                print("4. Voltar")
                tipo = input("Escolha uma opção: ")

                if tipo == '1':
                    nome = input("Digite o nome do aluno que deseja buscar: ")
                    busca_aluno(nome)

                elif tipo == '2':
                    nome = input("Digite o nome do professor que deseja buscar: ")
                    busca_prof(nome)

                elif tipo == '3':
                    cod = input("Digite o código da disciplina que deseja buscar: ")
                    busca_disc(cod)
                
                elif tipo == '4':
                    break

                else:
                    print("Digite um valor válido")


############################################################## REMOVER #########################################################################
        elif escolha == '4':
            while True:
                print("\n====== SELECIONE O QUE DESEJA REMOVER ======")
                print()
                print("1. Aluno")
                print("2. Professor")
                print("3. Disciplina")
                print("4. Matricula")
                print("5. Voltar")
                tipo = input("Escolha uma opção: ")

                if tipo == '1':
                    mat = input("Digite a matricula do aluno que deseja remover: ")
                    remove_aluno(mat)
                
                elif tipo == '2':
                    mat = input("Digite a matricula do professor que deseja remover: ")
                    remove_prof(mat)
                    
                elif tipo == '3':
                    cod = input("Digite o código da disciplina que deseja remover: ")
                    remove_disc(cod)
                    
                elif tipo == '4':
                    mat = input("Digite a matricula do aluno que deseja remover: ")
                    cod = input("Digite a o código da disciplina que deseja remover: ")
                    remove_mat(mat, cod)

                elif tipo == '5':
                    break

                else:
                    print("Digite um valor válido")
        

################################################################ LISTAR TODOS #########################################################################
        elif escolha == '5':
            while True:
                print("\n====== SELECIONE O QUE DESEJA LISTAR ======")
                print()
                print("1. Aluno")
                print("2. Professor")
                print("3. Disciplina")
                print("4. Voltar")
                tipo = input("Escolha uma opção: ")

                if tipo == '1':
                    lista_aluno()
                
                elif tipo == '2':
                    lista_prof()
                    
                elif tipo == '3':
                    lista_disc()
                
                elif tipo == '4':
                    break

                else:
                    print("Digite um valor válido")

##################################################################### EXIBIR UM #########################################################################
        elif escolha == '6':
                    while True:
                        print("\n====== SELECIONE O QUE DESEJA EXIBIR ======")
                        print()
                        print("1. Aluno")
                        print("2. Professor")
                        print("3. Disciplina")
                        print("4. Voltar")
                        tipo = input("Escolha uma opção: ")

                        if tipo == '1':
                            ID = input("Digite o ID de aluno que deseja exibir: ")
                            exibe_aluno(ID)

                        elif tipo == '2':
                            ID = input("Digite o ID do professor que deseja exibir: ")
                            exibe_prof(ID)

                        elif tipo == '3':
                            ID = input("Digite o ID da disciplina que deseja exibir: ")
                            exibe_disc(ID)
                        
                        elif tipo == '4':
                            break

                        else:
                            print("Digite um valor válido")


######################################################################## EXIBIR VIEW #########################################################################
        elif escolha == '7':
                    while True:
                        print("\n====== SELECIONE O QUE DESEJA EXIBIR ======")
                        print()
                        print("1. Aluno, Professor, Disciplina e Turma")
                        print("2. Aluno e Turma")
                        print("3. Voltar")
                        tipo = input("Escolha uma opção: ")

                        if tipo == '1':
                            exibir_view_turmas()
                            
                        if tipo == '2':
                            exibir_view_aluno_turma()
                            
                        if tipo == '3':
                            break


######################################################################## CHAMAR STORED PROCEDURE #########################################################################
        elif escolha == '8':
                    while True:
                        print("\n====== SELECIONE A PROCEDURE ======")
                        print()
                        print("1. Listar Alunos de uma Disciplina")
                        print("2. Listar Disciplinas de um Aluno")
                        print("3. Voltar")
                        tipo = input("Escolha uma opção: ")

                        if tipo == '1':
                            codigo = input("Digite o código da disciplina que deseja listar: ")
                            exibir_alunos_por_disciplina(codigo)
                            
                        if tipo == '2':
                            matricula = input("Digite a matricula do aluno que deseja listar: ")
                            exibir_disciplinas_por_aluno(matricula)
                            
                        if tipo == '3':
                            break


######################################################################## SAIR #########################################################################
        elif escolha == '9':
            print("Saindo...")
            break

        
################################################################## OPÇÃO INVÁLIDA ######################################################################
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()


cursor.close()
conexao.close()
