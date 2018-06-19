"""import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='smtp.office365.com', port=587)
MY_ADDRESS = 'firozhc@experiture.com'
PASSWORD = 'Apple_123'
s.starttls()
print(s.login(MY_ADDRESS, PASSWORD))
"""

import imaplib

username = 'firozhc@experiture.com'
password = 'Apple_123'

with imaplib.IMAP4_SSL('outlook.office365.com') as imap4:
    imap4.login(username, password)

    # retrieve a list of the mailboxes and select one
    result, mailboxes = imap4.list()
    imap4.select("inbox")