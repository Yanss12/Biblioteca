import random
catalogo_livros = []

def adicionar_livro(novo_livro : dict) -> None:
   '''
      Descrição: Função para adicionar novo livro no catalogo(lista).\n
      Parâmetro: A função recebe um novo_livro do tipo dict.\n
      Retorno: A função não retorna nada.
   '''    
   catalogo_livros.append(novo_livro)

def gerar_id(min_val=1,max_val=1000):
   '''
      Descrição: Função para gerar um id aleatorio para os livros.\n
      parâmetro: A função recebe um numero aleatorio que define o id.\n
      Retorno: A função retorna um id aleatorio para cada livro.
   '''
   return random.randint(min_val,max_val)

def listar_livros() -> list:
   '''
      Descrição: função para retornar os livros no catalogo(lista).\n
      Parâmetro: a função não recebe valores do parametro.\n
      Retorno: A função retorna uma lista com todos os livros.
   '''
   return catalogo_livros

def buscar_livro_por_titulo(titulo: str) -> list:
   '''
      Descrição: Função para buscar livros pelo título no catálogo.\n
      Parâmetro: titulo (str) - título do livro a ser buscado.\n
      Retorno: Lista de livros que correspondem ao título informado.
   '''
   for livro in catalogo_livros:
      if livro.get('titulo').lower() == titulo.lower():
         return livro
   print("livro não cadastrado")
   return None

def atualizar_disponibilidade_livro(id_livro):
   """
      Descrição: Função para atualizar a disponibilidade de um livro no catálogo.\n
      Parâmetro: id_livro (int) - ID do livro cuja disponibilidade será atualizada.\n
      Retorno: True se a disponibilidade foi atualizada com sucesso, False caso contrário.
   """
   for livro in catalogo_livros:
      if livro.get('id') == id_livro:
         while True:
            resposta = input("O livro está disponível? (s/n): ").strip().lower()
            if resposta == 's':
               livro['disponivel'] = True
               print("disponibilidade atualizada para: disponivel")
               return True
            
            elif resposta == 'n':
               livro['disponivel'] = False
               print("disponibilidade atualizada para: indisponivel")
               return True            
            else:
               print("Resposta inválida. Use 's' para sim ou 'n' para não.")
   print("livro não encontrado")
   return False

