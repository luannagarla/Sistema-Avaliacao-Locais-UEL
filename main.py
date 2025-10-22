from crud import criar_usuario, listar_usuarios, criar_local, listar_locais, criar_avaliacao, listar_avaliacoes
from datetime import date

def menu():
    while True:
        print("\n=== Sistema de Avaliação do Campus ===")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Cadastrar Local")
        print("4 - Listar Locais")
        print("5 - Fazer Avaliação")
        print("6 - Listar Avaliações")
        print("0 - Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            tipo = input("Tipo (aluno/professor): ")
            curso = input("Curso: ")
            dept = input("Departamento: ")
            id_novo = criar_usuario(nome, email, tipo, curso, dept)
            print(f"Usuário criado com ID {id_novo}")

        elif opcao == "2":
            for u in listar_usuarios():
                print(u)

        elif opcao == "3":
            nome = input("Nome do local: ")
            desc = input("Descrição: ")
            loc = input("Localização: ")
            cat = input("Categoria: ")
            img = input("URL da imagem: ")
            id_local = criar_local(nome, desc, loc, cat, img)
            print(f"Local criado com ID {id_local}")

        elif opcao == "4":
            for l in listar_locais():
                print(l)

        elif opcao == "5":
            id_user = int(input("ID do usuário: "))
            id_local = int(input("ID do local: "))
            nota = int(input("Nota (1 a 5): "))
            id_av = criar_avaliacao(id_user, id_local, nota, date.today())
            print(f"Avaliação registrada com ID {id_av}")

        elif opcao == "6":
            for a in listar_avaliacoes():
                print(a)

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
