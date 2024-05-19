import respostas
from funcoesbd import cadastro


class clientes:
    def __init__(self, nome, telefone, msg):
        self.nome = nome
        self.telefone = telefone
        self.msg = msg


def cadastrar_usuario(dados):
    cliente = clientes(dados['ProfileName'], dados['From'][10:], dados['Body'].lower())
    cadastrado = cadastro(cliente.nome, cliente.telefone)
    return cliente, cadastrado


def reply(usuario, validacao):
    if usuario.msg in 'bom dia boa tarde boa noite ola oi':
        return respostas.boas_vindas(usuario.nome, validacao)
    elif usuario.msg in 'orçamento , orcamento':
        return respostas.orcamento1(usuario.nome)
    elif 'email:' in usuario.msg:
        return respostas.orcamento(usuario.nome, usuario.msg, usuario.telefone)
    elif usuario.msg in 'serviços servico':
        return respostas.servicos(usuario.nome)
    elif 'automação' in usuario.msg or 'automacao' in usuario.msg or 'sistema' in usuario.msg:
        return respostas.despedida(usuario.nome, usuario.telefone, usuario.msg)
    else:
        return 'Desculpe, mas faltou alguma informação, poderia me enviar os dados novamente, lembrando que todas as informações são essências para nosso atendimento'
