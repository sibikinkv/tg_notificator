from flask import Flask, request
from threading import Thread
from datetime import datetime, timedelta

from modules.event import Event
from modules.templates import *
from modules.tg_api import poll_tg_bot
import modules.database as db

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.remote_addr)
    return 'Hello World!\n'


@app.route('/upload_event')
def upload_event():
    try:
        data = {
            'author': request.args.get('app'),
            'level': request.args.get('level').upper(),
            'text': request.args.get('text').replace('_', ' ')
        }
    except AttributeError:
        return failure_response('Usage: /upload_event?app=<app>&level=<level>&text=<your_text>')

    event = Event.from_json(data, host=request.remote_addr)

    return event.to_db()


@app.route('/get_events')
def get_events():
    try:
        date = request.args.get('date')
    except AttributeError:
        return failure_response('Usage: /get_events?date=<YYYY-MM-DD>')

    start_timestamp = datetime.strptime(date, '%Y-%m-%d')
    end_timestamp = start_timestamp + timedelta(days=1)
    query = '''
        SELECT *
        FROM service_notifications
        WHERE timestamp BETWEEN '{}' and '{}'
    '''.format(start_timestamp, end_timestamp)
    return db.exec_query(query)


if __name__ == '__main__':
    thread = Thread(target=poll_tg_bot)
    thread.start()

    app.debug = False
    app.run(host='0.0.0.0', port='5000')
