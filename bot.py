from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import gerencia

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def bot():
    msg_cliente = request.values
    usuario = gerencia.cadastrar_usuario(msg_cliente)
    msg_resposta = gerencia.reply(usuario[0], usuario[1])
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(msg_resposta)
    return str(resp)


@app.route('/')
def status():
    return 'Webhook Online'


if __name__ == '__main__':
    app.run(debug=True)
