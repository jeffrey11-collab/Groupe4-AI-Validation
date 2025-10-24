import os
import sys
import smtplib
from email.message import EmailMessage

# Fonction d'analyse du commit
def check_quality(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    if 'TODO' in content:
        return False
    return True

# Fonction pour envoyer email
def send_email(to_email, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Commit rejeté par l\'IA'
    msg['From'] = 'monemail@example.com'
    msg['To'] = to_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('monemail@example.com', 'password_app')
        smtp.send_message(msg)

# Liste des fichiers modifiés
modified_files = [f for f in os.listdir('src') if f.endswith('.py')]

# Analyse
for file in modified_files:
    if not check_quality(os.path.join('src', file)):
        send_email('auteur@example.com', f'Votre commit a échoué la validation IA: {file}')
        print(f'Rejected: {file}')
        sys.exit(1)

print('Commit validé par l\'IA !')
Explications : - Vérifie que les fichiers Python dans src/ ne contiennent pas “TODO”. - Si problème, envoie un email à l’auteur et le workflow échoue (exit(1)). - Sinon, le commit est validé.

