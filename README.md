# CoinGeckoParser 
[![DevPerion](https://img.shields.io/badge/made%20by-DevPerion-success)](https://github.com/Devperion)

Парсер топ-500 монет с криптобиржи CoinGecko с последующей загрузкой данных в Google Sheets каждые 5 мин. [Пример](https://docs.google.com/spreadsheets/d/1mhViI6J75NxQGz-n03Gi6Jpp6KmJ1ITd0f6cOB8_Uu4/edit?usp=sharing)
  
## Настройка
Для загрузки данных в Google Sheets нужнен json файл с сервисным аккаунтом Google, включенным Google Sheets API и разрешением на изменение файла

#### Сервисный аккаунт
* Создать проект в Google Cloud Platform
* APIs & Services -> Credentials -> Create Credentials -> Service Account
* Ввести имя -> Create and Continue -> Done
* Внизу в списке выбрать созданный аккаунт -> Keys -> Add new key -> JSON
* Скачаный JSON переместить в папку с проектом и переименовать в service_account.json

#### Включение API
В Google Cloud Platform на странице APIs & Services выбираем сверху +ENABLE APIS AND SERVICES, через поиск ищем Google Sheets API, выбираем и включаем

В проекте есть файл конфигурации config.json, где нужно указать id своей Google таблицы. 
```
"SPREADSHEET_ID": "1mhViI6J75NxQGz-n03Gi6Jpp6KmJ1ITd0f6cOB8_Uu4",
```
Узнать id можно посмотрев свою ссылку на таблицу, к примеру 
`https://docs.google.com/spreadsheets/d/1mhViI6J75NxQGz-n03Gi6Jpp6KmJ1ITd0f6cOB8_Uu4`, где 1mhViI6J75NxQGz-n03Gi6Jpp6KmJ1ITd0f6cOB8_Uu4 и есть id
```
"RANGE_NAME": "Лист1!A2:Z"
```
Лист1!A2:Z - Название листа и диапазон для заполнения 
## Установка зависимостей
```
pip install -r requirments.txt
```
## Запуск
```
python main.py
```
