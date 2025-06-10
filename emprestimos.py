from livros import *
from usuarios import *
registro_emprestimos = []

def realizar_emprestimo(id_livro, id_usuario, emprestimo):
    """
    Descrição: Função para realizar o empréstimo de um livro a um usuário.\n
    Parâmetros: id_livro (int) - ID do livro a ser emprestado, id_usuario (int) - ID do usuário que está realizando o empréstimo,       emprestimo (dict) - Dicionário contendo informações do empréstimo.\n
    retorno: A função não retorna nada, mas atualiza o registro de empréstimos e a disponibilidade do livro.
    """
    livro = None
    for l in catalogo_livros:
        if l['id'] == id_livro:
            livro = l
            break
    if not livro:
        print(f"Livro com ID {id_livro} não encontrado.")
        return
    if not livro['disponivel']:
        print(f"Livro '{livro['titulo']}' não está disponível.")
        return
    usuario = buscar_usuario_por_id(id_usuario)
    if not usuario:
        print(f"Usuário com ID {id_usuario} não encontrado.")
        return

    registro_emprestimos.append(emprestimo)
    livro['disponivel'] = False

def devolver_livro(id_emprestimo, data_devolucao):
    """
    Descrição: Função para registrar a devolução de um livro emprestado.\n
    Parâmetros: id_emprestimo (int) - ID do empréstimo a ser devolvido, data_devolucao (str) - Data da devolução do livro.\n
    Retorno: True se a devolução foi registrada com sucesso, False caso contrário.
    """
    for emprestimo in registro_emprestimos:
        if emprestimo['id_emprestimo'] == id_emprestimo and emprestimo['data_devolucao'] == data_devolucao:
            emprestimo["data_devolucao"] = data_devolucao
            for livro in catalogo_livros:
                if livro['id'] == emprestimo["id_livro"]:
                    livro['disponivel'] = True
                    break
            print(f"Livro devolvido com sucesso. Data de devolução: {data_devolucao}")
            return True
    print("Empréstimo não encontrado ou livro já devolvido.")
    return False

def listar_emprestimos_ativos():
    """
    Descrição: Função para listar todos os empréstimos ativos (livros que foram emprestados e ainda não devolvidos).\n
    Parâmetros: A função não recebe parâmetros.\n
    Retorno: A função retorna uma lista de empréstimos ativos, imprimindo os detalhes de cada um.
    """
    for emprestimo in registro_emprestimos:
        # Encontrar o livro correspondente ao empréstimo
        livro = None
        for l in catalogo_livros:
            if l['id'] == emprestimo['id_livro']:
                livro = l
                break
        # Verifica se o livro está emprestado (não disponível)
        if livro and not livro['disponivel']:
            usuario = buscar_usuario_por_id(emprestimo['id_usuario'])
            print(f"Livro: {livro['titulo']}, Usuário: {usuario['nome']}, Data devolução: {emprestimo['data_devolucao']}, Status: Ativo")


def historico_emprestimos_usuario(id_usuario):
    """
    Descrição: Função para listar o histórico de empréstimos de um usuário específico.\n
    Parâmetros: id_usuario (int) - ID do usuário cujo histórico de empréstimos será listado.\n
    Retorno: A função retorna o histórico de empréstimos do usuário.
    """
    historico = []
    for emprestimo in registro_emprestimos:
        if emprestimo['id_usuario'] == id_usuario:
            historico.append(emprestimo)
    print(f"\nHistórico de Empréstimos do Usuário {id_usuario}:")
    if not historico:
        print("Nenhum empréstimo encontrado.")
        return
    for e in historico:
        livro = None
        for l in catalogo_livros:
            if l['id'] == e['id_livro']:
                livro = l
                break
        status = "Devolvido" if e['data_devolucao'] else "Ativo"
        print(f"Livro: {livro['titulo']}, Data Empréstimo: {e['data_emprestimo']}, Status: {status}")
        if e['data_devolucao']:
            print(f"Data Devolução: {e['data_devolucao']}")

