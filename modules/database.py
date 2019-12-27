import psycopg2
from contextlib import closing

from modules.templates import *
from cfg.config import DATABASE_CONNECTION


def exec_query(query):
    operation = query.strip().split(' ')[0].upper()     # get first word, SELECT, INSERT etc.
    try:
        with closing(psycopg2.connect(DATABASE_CONNECTION)
                     ) as conn:

            with conn.cursor() as cursor:

                cursor.execute(query)
                conn.commit()

                if operation == "SELECT":
                    columns = [desc[0] for desc in cursor.description]
                    result = cursor.fetchall()
                    json_rows = []

                    for row in result:
                        row_data = dict(zip(columns, row))
                        json_rows.append(row_data)

                    return json_rows

                return success_response(None)

    except Exception as e:
        print(e)
        return failure_response(e)
