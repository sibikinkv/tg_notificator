# TG_NOTIFICATOR
### Описание
Небольшая утилита для получения оповещений в телеграм откуда угодно. Представляет из себя маленькое Flask-приложение, которому можно отправить в запросе уведомление:
``` bash
192.168.0.1:5000/upload_event?app=<app>&level=<level>&text=<your_text>
```
Все уведомления сохраняются в базе данных и рассылаются в телеграм конкретным полььзователям(настраивается в config.py по имени приложения и уровню уведомления: INFO, WARNING, ERROR) или в общий канал.

### Установка и запуск
```bash
git clone git@github.com:sibikinkv/tg_notificator.git
cd tg_notificator
pip3 install -r requirements.txt
python3 app.py
```

