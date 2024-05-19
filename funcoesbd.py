import mysql.connector


def cadastro(nome, telefone):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bootatendimento',
    )
    cursor = conexao.cursor()
    comando1 = f'SELECT Nome, Telefone FROM clientes'
    cursor.execute(comando1)
    dados = cursor.fetchall()
    cadastrado = False
    for cliente, numero in dados:
        if int(numero) == int(telefone):
            cadastrado = True
    if cadastrado == False:
        comando = f'INSERT INTO clientes (Nome, Telefone) VALUES ("{nome}", "{telefone}")'
        cursor.execute(comando)
        conexao.commit()
        return str('falso')
    else:
        return str('verdadeiro')
    cursor.close()
    conexao.close()


def cadastrar_email(email, telefone):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bootatendimento',
    )

    cursor = conexao.cursor()
    comando = f"UPDATE `bootatendimento`.`clientes` SET `Email` = '{email[6:].strip()}' WHERE (`Telefone` = '{telefone}')"
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    cursor.close()


def consultar_email(telefone):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bootatendimento',
    )
    cursor = conexao.cursor()
    comando = f'SELECT Email, Telefone FROM clientes WHERE Telefone = {telefone}'
    cursor.execute(comando)
    contato = cursor.fetchall()
    for e_mail, telefone in contato:
        email = e_mail
    return str(email)
    cursor.close()
    conexao.close()
