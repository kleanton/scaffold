import requests
import json
import datetime
from gd import postongdoc

import pandas as pd

API_KEY = '0ade8775111c88f7af31bd7d655df0c6'
X_DOMAIN = 'response.dasreda.ru'


DSletters_name= [
    'Дожим_стандарт. Письмо1_24h',
    'Дожим_стандарт. Письмо2_48h',
    'Дожим_стандарт. Письмо3_72h',
    'Дожим_стандарт. Письмо4_96h',
    'Дожим_стандарт. Письмо5_12',
    'Дожим_стандарт. Письмо6_12',
    'Дожим_стандарт. Письмо7',
    'Дожим_вип. Письмо1_24h',
    'Дожим_вип. Письмо2_48h',
    'Дожим_вип. Письмо3_54h',
    'Дожим_вип. Письмо4_72h',
    'Дожим_миникурс_стандарт. Письмо1_24h',
    'Дожим_миникурс_стандарт. Письмо2_48h',
    'Дожим_миникурс_стандарт. Письмо3_72h',
    'Дожим_миникурс_стандарт. Письмо4_96h',
    'Дожим_миникурс_стандарт. Письмо5_120h',
    'Дожим_миникурс_стандарт. Письмо6_120h',
    'Реактивация. Прогрев 1-new links',
    'Реактивация. Прогрев 1-new links-2',
    'Письмо реактивации 2 — Антон',
    'Письмо реактивации 3 — Антон',
    'Письмо реактивации 2 — Алина',
    'Письмо реактивации 3 — Алина',
    'Письмо реактивации 4 — Антон',
    'Письмо реактивации 5 — Антон',
    'Реактивация. Пуш120-1',
    'Реактивация. Пуш120-2-3',
    'Реактивация. Опрос',
    'Реактивация. Последнее письмо',
    '120-микрокурс-Урок-1, Аветов',
    '120-микрокурс-Урок-2, Алексеева',
    '120-микрокурс-Урок-3, Горбунов',
    '120-микрокурс-Урок-4, Косенко',
    '120-микрокурс-Урок-5, Зиновьева',
    '120-микрокурс-финал',
    '120-микрокурс-финал-не смотрели все видео',
    '120мини_авто',
    '120 список лайфхаков',
    '120-инструкция для оплативших',
    '120_транзакционник, TW',
    '120 Апгрейд до ВИП'
]

def get_automation_newsletters():
    url = "https://api3.getresponse360.pl/v3/newsletters"
    querystring = {"query[type]":"automation","fields":"name,subject,status,sendMetrics,clickTracks,campaign","sort[createdOn]":"asc","page":"1,2,3,4","perPage":"100"}
    payload = ""
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_newsletters_stat(newsletterId):
    url = "https://api3.getresponse360.pl/v3/newsletters/"+newsletterId+"/statistics"
    querystring = {"request[groupBy]":"total"}
    payload = "" 
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()


# newsletter['newsletterId'] # перебираем все письма автоматизации по их id
#print(allnewsletters)
#print(get_newsletter_stat(allnewsletters[1]['newsletterId'])) # читаем Id из json массива, выводим статистику по письму с этим Id



allnewsletters=get_automation_newsletters() # получаем все письма автоматизации
letterid,name,subject,st = [],[],[],[]
sent, totalOpened, uniqueOpened = [],[],[]
totalClicked, uniqueClicked = [],[]
unsubscribed,bounced, complaints =[],[],[]
for letter in allnewsletters:
        # if letter['name'] in DSletters_name:
        #     letterid.append(letter['newsletterId'])
        #     name.append(letter['name'])
        #     subject.append(letter['subject'])
        #     get_newsletters_stat(letter['newsletterId'])
        #     for key in get_newsletters_stat(letter['newsletterId']):
        #             sent.append(key['sent'])
        #             uniqueOpened.append(key['uniqueOpened']) 
        
        #             totalClicked.append(key['totalClicked'])
        #             uniqueClicked.append(key['uniqueClicked'])
        #             unsubscribed.append(key['unsubscribed'])
        #             bounced.append(key['bounced'])
        #             complaints.append(key['complaints'])
        letterid.append(letter['newsletterId'])
        name.append(letter['name'])
        subject.append(letter['subject'])
        get_newsletters_stat(letter['newsletterId'])
        for key in get_newsletters_stat(letter['newsletterId']):
                sent.append(key['sent'])
                uniqueOpened.append(key['uniqueOpened']) 
                totalClicked.append(key['totalClicked'])
                uniqueClicked.append(key['uniqueClicked'])
                unsubscribed.append(key['unsubscribed'])
                bounced.append(key['bounced'])
                complaints.append(key['complaints'])


df= pd.DataFrame([letterid,name,subject,sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,unsubscribed,bounced, complaints]).T
postongdoc(df,'kleanton@gmail.com','Статистика по письмам_Антон','stat_on'+str(datetime.datetime.now()))
print('import Done!')
