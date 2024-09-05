import requests
import smtplib
import paramiko
import os

import schedule

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SSH_KEY_PASSWORD = os.environ.get('SSH_KEY_PASSWORD')


def sent_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, 'support@bytepark.ru', email_msg)


def monitor_application():
    try:
        response = requests.get('http://bytepark.ru/')
        if response.status_code == 200:
            print('Application is running successfully!')
        else:
            print('Application Down. Fix it!')
            # send email to me
            msg = f'Subject: SITE DOWN\nApplication returned {response.status_code}'
            # sent_notification(msg)

            # restart the application
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('bytepark.ru',
                        username='adwiz',
                        key_filename='/Users/adwiz/.ssh/id_ed25519',
                        passphrase=SSH_KEY_PASSWORD)
            stdin, stdout, stderr = ssh.exec_command('ls -lah')
            print(stdin)
            dir_content = ''.join(stdout.readlines())
            ssh.close()
            sent_notification(dir_content.encode('utf8'))

    except Exception as ex:
        print(f'Connection error happened {ex}')
        msg = 'Subject: SITE DOWN\nApplication not accessible at all. Fix the issue.'
        sent_notification(msg)


schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
