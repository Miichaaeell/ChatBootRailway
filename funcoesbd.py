import mysql.connector
import os
import smtplib
import email.message

key_email = os.getenv("EMAIL_KEY")
my_email = os.getenv("MY_EMAIL")
key_bd = os.getenv("BD_KEY")


def cadastro(nome, telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
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
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
    )

    cursor = conexao.cursor()
    comando = f"UPDATE `railway`.`clientes` SET `Email` = '{email[6:].strip()}' WHERE (`Telefone` = '{telefone}')"
    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    cursor.close()


def consultar_email(telefone):
    conexao = mysql.connector.connect(
        host='monorail.proxy.rlwy.net',
        port='34425',
        user='root',
        password=f'{key_bd}',
        database='railway',
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


def enviar_email(nome='', telefone='', msg=''):
    adress = consultar_email(telefone)
    corpo_email = f"""
    Olá {nome}, seu pedido de orçamento foi realizado com Sucesso!
    {msg}
    """
    msg = email.message.Message()
    msg['Subject'] = 'Confirmação do pedido de orçamento - no reply'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{adress}'
    password = f'{key_email}'
    msg.add_header('Content-Type', 'Text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(msg['From'], password)
    print(msg['To'])
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso!')
