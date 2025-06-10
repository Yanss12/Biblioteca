from livros import *
from usuarios import *
import pprint

while True:
    opção_menu = int(input("\nInforme sua opção: (1 - Gerenciar livros) (2 - Gerenciar usuario): "))
    
    # Gerenciamento de livros
    if opção_menu == 1:
        opcao_livro = int(input("\nInforme sua opção: (1 - Adicionar livro) (2 - Exibir catalogo) (3 - Buscar titulo) (4 = Verificar) "))

        
        if opcao_livro == 1:
            id_livro = gerar_id()
            titulo = input("Informe o titulo: ")
            autor = input("informe o nome do autor: ")
            ano_publicacao = int(input("informe o ano de publicação: "))
            print(f"o id do livro {titulo} é {id_livro}")

            livros = {
                "id" : id_livro,
                "titulo" : titulo,
                "autor" : autor,
                "ano_publicacao" : ano_publicacao
            }

            adicionar_livro(livros)

        elif opcao_livro == 2:
            catalogo_livros = listar_livros()
            pprint.pprint(catalogo_livros)
        
        elif opcao_livro == 3:
            titulo = input("Informe o titulo: ")
            resultado_livro = buscar_livro_por_titulo(titulo)
            print(resultado_livro)

    # Gerenciamento de usuario
    elif opção_menu == 2:
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

                status = atualizar_email_por_id(id_usuario, novo_email)

                if status:
                    print('Email atualizado com sucesso')
                else:
                    print('Usuario não encontrado')