### Проект для отображения курса рубля к евро через api с сайта [Exchangeratesapi](https://exchangeratesapi.io/)

### Структура проекта:
```
ilshat2
 └── dollar_to_ruble
     └── dtr_project <-- рабочая папка проекта с кодом проекта
     |   ├──  manage.py
     |   └── dtr_project
     |       ├──  __init__.py
     |       ├──  asgi.py
     |       ├──  settings.py
     |       ├──  urls.py
     |       ├──  wsgi.py
     |   └── exchange_rate
     |       ├──  __init__.py
     |       ├──  apps.py
     |       ├──  models.py
     |       ├──  serializers.py
     |       ├──  urls.py
     |       ├──  views.py
     ├── .gitignore
     ├── README.md
     ├── requirements.txt
```
## В рамках задачи (данного проекта) были выполненны подзадачи:
- **Создание проекта Django:** Инициализация нового проекта, создание приложения для работы с курсом валют.
- **Выбор и интеграция внешнего API:** Исследование доступных API для получения курсов валют, выбор подходящего, написание кода для взаимодействия с API.
- **Создание модели для хранения данных о курсах:** Создание модели в Django для хранения полученных данных о курсах валют (дата, значение).
- **Реализация представления (view):** Написание представления, которое будет обрабатывать запрос `/get-current-usd/`, получать данные от API, сохранять их в базе данных и формировать JSON-ответ с текущим курсом и историей последних 10 значений.
- **Настройка URL:** Добавление путей в файлы `urls.py`.
- **Реализация логики для ограничения частоты запросов:** Добавление паузы между запросами к API.

## Блок вопросов.

### Продакт-менеджеру:
- Какая точность курса требуется?
- Как часто нужно обновлять данные?
- Какие дополнительные данные нужно отображать (например, графики, сравнение с другими валютами)?
- 
### Team Lead:
- Какой стек технологий используется в проекте?
- Какие инструменты для мониторинга будут использоваться?
- Каковы требования к производительности?

---
# Так выглядит ответ
---

![#Так вынлядит ответ](https://i.ibb.co/rktm3D2/2024-11-15-215850.png)

---
