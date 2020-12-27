import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

if __name__ == '__main__':
    html = Template(Path('index.html').read_text())

    email = EmailMessage()
    email['from'] = 'Ivan Valadez'
    email['to'] = 'ivan.valadez.0902@gmail.com'
    email['subject'] = 'Test email'
    email.set_content(html.substitute(name='Ivan'))

    # port 587 by convention
    with smtplib.SMTP(host='smtp.hotmail.com', port=587) as smtp:
        smtp.ehlo()  # Part of the protocol
        smtp.starttls()  # Connection
        smtp.login('ivan_valadez_11@hotmail.com', 'Chiva-valad11%')
        smtp.send_message(email)
        print('All good')
