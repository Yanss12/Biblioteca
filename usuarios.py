cadastro_usuarios = []

def adicionar_usuario(novo_usuario : dict) -> None:
   '''
      Descrição: Função para adicionar novo cliente no sistema(lista).\n
      Parâmetro: A função recebe um novo_usuario do tipo dict.\n
      Retorno: A função não retorna nada.
   '''    
   cadastro_usuarios.append(novo_usuario)

def listar_usuarios() -> list:
   '''
      Descrição: Função para retornar os usuarios no sistema(lista).\n
      Parâmetro: A função não recebe valores do parametro.\n
      Retorno: A função retorna uma lista com todos os usuarios.
   '''
   return cadastro_usuarios

def buscar_usuario_por_id(id_usuario: int):
   '''
      Descrição: Função para buscar usuario pelo id no sistema.\n
      Parâmetro: id (int) - id do usuario a ser buscado.\n
      Retorno: Cadastro de usuario que corresponde ao id informado.
   '''
   for usuario in cadastro_usuarios:
      if usuario.get('id') == id_usuario:
         return usuario
   print("Usuario não cadastrado")
   return None

def atualizar_email_por_id(id_usuario: int, novo_email: str) -> bool:
    '''
        Descrição: Função para atualizar o email de um usuário pelo id.\n
        Parâmetro: id_usuario (int) - id do usuário a ser atualizado.\n
                   novo_email (str) - novo email do usuário.\n
        Retorno: True se o email foi atualizado, False caso contrário.
    '''
    for usuario in cadastro_usuarios:
        if usuario.get("id") == id_usuario:
            usuario["email"] = novo_email
            return True
    return False