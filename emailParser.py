import smtplib
import time
import imaplib
import email
import re
import mysql.connector
from mysql.connector import Error

FROM_EMAIL  = ""
FROM_PWD    = ""
SMTP_SERVER = ""
SMTP_PORT   = 993
SUBJECT     = "UIT Student Employee Program Application - Submission"
BODY        = ' '

def connectToDB():
    try:
        conn = mysql.connector.connect(host='localhost', database='candidatesdb', user='root', password=FROM_PWD)
        if conn.is_connected():
            print("Connection successful\n")
            return conn
    except Error as e:
        print(e)

def disconnectFromDB(conn):
    conn.close()
    print ("Connection terminated\n")

def createNewApplicant(conn, info):
    cursor = conn.cursor()
    ## check uNID
    stage = 'received'
    numGroups = len(info[10].split(', '))

    sqlCan = "INSERT INTO candidates (uNID, firstName, lastName, phone, email, stage) VALUES (%s, %s, %s, %s, %s, %s)"
    argsCan = (info[3], info[1], info[2], info[5], info[4], stage)
    sqlDeets = "INSERT INTO appDetails VALUES (%s, %s, %s, %s, %s, %s, %s)"
    argsDeets = (info[3], info[7], info[6], info[8], info[9], info[13], info[14])
    cursor.execute(sqlCan, argsCan)
    cursor.execute(sqlDeets, argsDeets)
    info[10] = info[10].replace("&amp;", "And").replace(" ", "")
    s_vals = str(('%s',) * (numGroups + 1)).replace("'", "")
    sqlGroups = "INSERT INTO groups (uNID, " + info[10] + ") VALUES " + s_vals
    argsGroups = (info[3],) + (0,) * numGroups
    cursor.execute(sqlGroups, argsGroups)
    conn.commit()

def readEmail(conn):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'UNSEEN')
        if(len(data[0]) > 0):
            for i in data[0].split(' '):
                typ, data = mail.fetch(i, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print('From : ' + email_from)
                        print('Subject : ' + email_subject)
                        if msg.is_multipart() and email_subject == SUBJECT:
                            for payload in msg.get_payload():
                                if(payload.get_content_type()== 'text/html'):
                                    body = payload.get_payload()
                                    sqldata = parse_body(body)
                                    createNewApplicant(conn, sqldata)
                        else:
                            print(msg.get_payload())

                        print('\n')
        return conn
    except Exception, e:
        print(str(e))

def parse_body(body):
    body = body.translate(None, '=')
    #print body
    text = body.split('\r\n')
    for chunk in text:
        re.sub('\s+', ' ', chunk).strip()
    # print text
    filtered = [tag for tag in text if (tag.startswith('<td>') or not tag.startswith('<'))]
    filterchunk = ''.join(filtered)
    filtered = filterchunk.split('</td><td>')
    filtered[3] = filtered[3].lower()
    filtered[5] = re.sub('-', '', filtered[5])
    filtered[6] = filtered[6].lower()
    filtered[13] = re.sub('<[^<]+?>', '', filtered[13])
    filtered[14] = re.sub('<[^<]+?>', '', filtered[14])
    #for i in range(0, len(filtered)):
        #print(str(i) + " - " + filtered[i])
    #print len(filtered)
    return filtered

def main():
    conn = connectToDB()
    readEmail(conn)

    disconnectFromDB(conn)

if __name__== "__main__":
    main()