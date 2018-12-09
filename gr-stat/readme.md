"""
 Узнать статистику по письму

https://api3.getresponse360.pl/v3/newsletters/0x/statistics?
request[groupBy]=total

0x - это ID письма

---
Python код
---
import requests

url = "https://api3.getresponse360.pl/v3/newsletters/ae/statistics"

querystring = {"request[groupBy]":"total"}

payload = ""
headers = {
    'X-Domain': "response.dasreda.ru",
    'X-Auth-Token': "api-key 0ade8775111c88f7af31bd7d655df0c6",
    'cache-control': "no-cache",
    'Postman-Token': "e247c478-b35c-4cef-89a3-455437097fc6"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

---
 
Найти ID всех писем автоматизации+Заголовки писем автоматизации
https://api3.getresponse360.pl/v3/newsletters?
query[type]=automation&fields=name,subject,status,sendMetrics,clickTracks,
campaign&sort[createdOn]=asc&page=1,2,3&perPage=200

---
Python код
---
import requests

url = "https://api3.getresponse360.pl/v3/newsletters"

querystring = {"query[type]":"automation","fields":"name,subject,status,sendMetrics,clickTracks,campaign","sort[createdOn]":"asc","page":"1,2,3","perPage":"200"}

payload = ""
headers = {
    'X-Domain': "response.dasreda.ru",
    'X-Auth-Token': "api-key 0ade8775111c88f7af31bd7d655df0c6",
    'cache-control': "no-cache",
    'Postman-Token': "9f00cc8e-9daa-4d73-8698-623b38906d61"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)
---
Параметры компаний
to_activate['p']
120demo['4t']
platform_digest['40']

platform['O']
___technical_company['j']

----------------------

ЗАДАЧА — получить json где будет

Имя письма 'name'

Тема письма 'subject'

Отправлено 'sent'

Открыто, всего 'totalOpened'

Открыто, уник 'uniqueOpened'

Коверсия заголовка (рассчитывается = uniqueOpened / sent)

Клики, всего 'totalClicked'

Клики, уник 'uniqueClicked'

Конверсия письма (процент кликов от открывших = uniqueClicked / uniqueOpened)

Отписки 'unsubscribed'

Ошибки 'bounced'

Жалобы 'complaints'

-------------------------

БЭКЛОГ
По каждому письму вытащить ссылки из письма, 
отсортированные по частоте уникальных кликов

-------------------------

АЛГОРИТМ

БЭК
1) Получаем newsletterId, name,subject писем, 
которые совпадают с нужными нам темами (массив тем задается в коде)
2) Поочередно подставляем newsletterId в запрос на получение статистики по каждому письму.
Сохраняем полученные поля sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,
unsubscribed,bounced, complaints в тот же json где лежит newsletterId по которому итерируемся
3) Выводим json со всеми newsletterId, name,subject, sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,
unsubscribed,bounced, complaints

ФРОНТ - MVP
1) На основании json строим таблицу. Таблицу отдаём в гугл-таблицу


"""


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


1F1OkBmNztO9aDshDZYRwrVITcbzVuEiCQv7uelBXj7w