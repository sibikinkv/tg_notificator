import datetime
import json

import modules.database as db


class Event:
    __slots__ = ('author', 'level', 'text', 'timestamp', 'host')

    def __init__(self, author, text, level, host):
        self.author = author
        self.level = level
        self.host = host
        self.text = text
        self.timestamp = datetime.datetime.now()

    @classmethod
    def from_json(cls, json_str: json, host: str) -> 'Event':
        # event = json.loads(json_str)
        return cls(author=json_str['author'],
                   host=host,
                   level=json_str['level'],
                   text=json_str['text']
                   )

    def to_db(self):
        query = '''
        INSERT INTO service_notifications(service, host, timestamp, text, level)
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')'''.format(
            self.author,
            self.host,
            self.timestamp,
            self.text,
            self.level
        )

        return db.exec_query(query)

    def to_json(self):
        return {key: getattr(self, key, None) for key in self.__slots__}

    def __str__(self):
        return '{0} {1} : {2}'.format(self.timestamp, self.author, self.text)
