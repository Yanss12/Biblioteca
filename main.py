from livros import *
from usuarios import *
from emprestimos import *
import pprint

while True:
    opcao_menu = int(input("\nInforme sua opção: (1 - Gerenciar livros) (2 - Gerenciar usuario) (3 - Gerenciar emprestimos): "))
    
    # Gerenciamento de livros
    if opcao_menu == 1:
        opcao_livro = int(input("\nInforme sua opção: (1 - Adicionar livro) (2 - Exibir catalogo) (3 - Buscar titulo) (4 - definir disponibilidade de livro): "))

        
        if opcao_livro == 1:
            id_livro = gerar_id()
            titulo = input("Informe o titulo: ")
            autor = input("informe o nome do autor: ")
            ano_publicacao = int(input("informe o ano de publicação: "))
            disponivel = True
            print(f"o id do livro {titulo} é {id_livro}")

            livros = {
                "id" : id_livro,
                "titulo" : titulo,
                "autor" : autor,
                "ano_publicacao" : ano_publicacao,
                "disponivel" : disponivel
            }

            adicionar_livro(livros)

        elif opcao_livro == 2:
            catalogo_livros = listar_livros()
            pprint.pprint(catalogo_livros)
        
        elif opcao_livro == 3:
            titulo = input("Informe o titulo: ")
            resultado_livro = buscar_livro_por_titulo(titulo)
            print(resultado_livro)

        elif opcao_livro == 4:
            id_livro = int(input("Informe o ID do livro que deseja atualizar a disponibilidade: "))
            atualizar_disponibilidade_livro(id_livro)

    # Gerenciamento de usuario
    elif opcao_menu == 2:
        opcao_usuario = int(input("\nInforme sua opção: (1 - Adicionar cliente) (2 - Exibir clientes) (3 - buscar cliente) (4 - Atualizar email): "))

        if opcao_usuario == 1:
            id_usuario = gerar_id()
            nome = input("Informe o nome: ")
            email = input("Informe o email: ")
            print(f"o id do usuario {nome} é {id_usuario}")

            usuario = {
                "id" : id_usuario,
                "nome" : nome,
                "email" : email,
            }

            adicionar_usuario(usuario)
    
        elif opcao_usuario == 2:
            cadastro_usuarios = listar_usuarios()
            pprint.pprint(cadastro_usuarios)

        elif opcao_usuario == 3:
            id = int(input("informe o id: "))
            resultado_cliente = buscar_usuario_por_id(id)
            print(resultado_cliente)
        
        elif opcao_usuario == 4:
                id_usuario = int(input("Informe o ID do usuario que deseja alterar o email: "))
                novo_email = input("Informe o novo email: ")

                cadastro_usuarios = listar_usuarios()

                status_email = atualizar_email_por_id(id_usuario, novo_email)

                if status_email:
                    print('Email atualizado com sucesso')
                else:
                    print('Usuario não encontrado')

    elif opcao_menu == 3: 
        opcao_emprestimo = int(input("\nInforme sua opção: (1 - Realizar emprestimo) (2 - Devolver emprestimo) (3 - Listar emprestimos ativos) (4 - Listar historico de um usuario): "))

        if opcao_emprestimo == 1:
            id_emprestimo = gerar_id()
            id_livro = int(input("Informe o id do livro que deseja emprestar: "))
            id_usuario = int(input("Informe o id do usuario que deseja o livro: "))
            data_emprestimo = str(input("Informe a data que o livro foi emprestado (Formato DD-MM-AAAA): "))
            data_devolucao = str(input("Informe a data da devolução (Formato DD-MM-AAAA): "))

            emprestimos = {
            "id_emprestimo": id_emprestimo,
            "id_livro": id_livro,
            "id_usuario": id_usuario,
            "data_emprestimo": data_emprestimo,
            "data_devolucao": data_devolucao
            }

            realizar_emprestimo(id_livro, id_usuario, emprestimos)
            print(f"O id do emprestimo realizado é {id_emprestimo}")

        elif opcao_emprestimo == 2:
            id_emprestimo = int(input("Informe o ID do empréstimo a ser devolvido: "))
            data_devolucao = str(input("Informe a data de devolução do emprestimo a ser devolvido: "))
            devolver_livro(id_emprestimo, data_devolucao)

        elif opcao_emprestimo == 3:
            listar_emprestimos_ativos()

        elif opcao_emprestimo == 4:
            id_usuario = int(input("Informe o id do usuario que deseja o historico: "))
            historico_emprestimos_usuario(id_usuario)