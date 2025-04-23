userData = []

def cadastrar(nome, email, senha, cpf):
#    for usuario in userData:
#        if usuario["email"] == email:
#            return "email já cadastrado"


    usuario = {
        "nome":nome,
        "email":email,
        "senha":senha,
        "cpf":cpf
    }

    for usuario in userData:

        if usuario["email"] == email:
            return "email já cadastrado"

    else:
        userData.append(usuario)
        return "sucesso"



#def cadastrar(nome, email):
#    userData = []
#
#    usuario = {
#        "nome":nome,
#        "email":email
#    }
#
#    if usuario["email"] not in userData:
#
#        userData.append(usuario)
#        return "sucesso"
#
#    else:
#        return "email já cadastrado"



# controller
#def cadastro(nome, email, senha, cpf):
#    new_user = {
#        "nome": nome,
#        "email":email,
#        "senha":senha,
#        "cpf": cpf
#    }
#    return save(new_user)

# service
#def save(new_user):
#    if new_user["nome"] and new_user["cpf"]:
#        return True #salvo no DB
#    return False #erro ao salvar no DB



def listar_todos_usuarios():
    return userData



def listar_usuario(cpf):
    for usuario in userData:
        if usuario["cpf"] == cpf:
            return usuario
    return "cpf não encontrado"



def deletar_usuario(cpf):
    for usuario in userData:
        if usuario["cpf"] == cpf:
            userData.remove(usuario)
    return True
