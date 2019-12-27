from time import sleep
from modules.tg_bot import Bot
import modules.database as db


def poll_tg_bot():
    while True:
        bot = Bot()

        query = """
            SELECT id, level, service, host(host), text, to_char(timestamp, 'HH24:MI:SS\tDD Mon') as time
            FROM service_notifications
            WHERE processed=false
        """

        result = db.exec_query(query)
        for line in result:
            tmp_line = {i: line[i] for i in line if i != 'id'}
            bot.send_msg(tmp_line)

            update_query = '''
                UPDATE service_notifications
                SET processed=true
                WHERE id={}
            '''.format(line['id'])
            db.exec_query(update_query)

        sleep(60)


if __name__ == '__main__':

    bot = Bot()
    # bot.test()
    query = """
        SELECT level, service, host(host), text, to_char(timestamp, 'HH24:MI:SS\tDD Mon') as time
        FROM service_notifications
    """
    msg = db.exec_query(query)
    bot.send_msg(msg['data'][0])
