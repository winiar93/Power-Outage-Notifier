import requests
import re
import smtplib
from email.message import EmailMessage
import datetime
import logging
import config


logging.basicConfig(level=logging.INFO)

url = config.url

def send_mail_notification(mail_body_text):
    date_object = datetime.date.today()
    msg = EmailMessage()
    msg['From'] = config.mail_from 
    msg['To'] = config.mail_to 
    msg['Subject'] = f'Blackouts {date_object}'
    msg.set_content(f'{mail_body_text}')

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.ehlo()
        server.login(config.mail_from, config.password)
        server.send_message(msg)
        server.close()
        logging.info('Mail sent')
    except Exception as e:
        logging.info(e)
        logging.info('Found connection error')


def blackouts_information(url, village_name):
    cnt = 0
    errors_list = []
    mail_text = ''
    output = requests.get(url).json()
    for outages in output:
        for i in output[outages]:
            if len(re.findall(village_name, i['Message'])) != 0:
                cnt += 1
                txt = f'OD : ' + f"{output[outages][0]['StartDate']} " + f' OD : ' + f"{output[outages][0]['EndDate']}"
                errors_list.append(txt)

    tmp_text =  '\n'.join(errors_list)
    mail_text = f"Ilość planowanych awarii : {cnt} \n"
    
    return willage_name + "\n" +mail_text + tmp_text


if __name__ == "__main__":
    send_mail_notification(blackouts_information(url, willage_name=config.village_name))
