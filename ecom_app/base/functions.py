from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives
import threading

def send_email(subject='', body='', rcpt=[]):

    subject = subject
    body = body

    conn = get_connection(host='smtp.gmail.com',
                          port=465,
                          username='pruebas@opalo.com.co',
                          password='DeV.2020',
                          use_tls=False,
                          use_ssl=True)

    email = EmailMultiAlternatives()
    email.subject = subject
    email.cc = []
    email.bcc = []
    email.reply_to = []
    email.content_subtype = "html"
    email.text_content = body
    email.body = body
    email.from_email = 'Notificaciones Eceom App'
    email.to = ['cardona.zero@gmail.com']
    email.connection = conn
    email.html_message = True
    mailThread = threading.Thread(target=lambda x: x.send(), args=(email,))
    mailThread.start()

    return True