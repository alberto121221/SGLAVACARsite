from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', '123')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-mail')
def test_mail():
    msg = Message(
        'PRUEBA SG LAVACAR',
        recipients=[app.config['MAIL_USERNAME']],
        body='Si llegó este correo, Flask-Mail funciona.'
    )
    print("📤 Enviando correo...")
    mail.send(msg)
    return 'Correo de prueba enviado'
@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']

        msg = Message(
            f'Nuevo mensaje SG Lavacar - {nombre}',
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],
            reply_to=correo
        )

        msg.body = f"""
Nombre: {nombre}
Correo: {correo}

Mensaje:
{mensaje}
"""

        mail.send(msg)
        flash("Mensaje enviado correctamente ✅", "success")
        

    except Exception as e:
        print(e)
        flash("Error al enviar el mensaje ❌", "danger")

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
