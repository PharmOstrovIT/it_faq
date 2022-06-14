import psycopg2
from credentials import username as username_db, password as password_db, database, host, port


def get_apteka_id(apteka_name):
    cursor_call_count, connection = None, None
    apteka_id = []
    sql_request = (f"""
                        SELECT id 
                        FROM public.main_apteka
                        WHERE name = '{apteka_name}'
        """)

    try:
        connection = psycopg2.connect(database=database,
                                      user=username_db,
                                      password=password_db,
                                      host=host,
                                      port=port
                                      )

        cursor_call_count = connection.cursor()
        cursor_call_count.execute(str(sql_request))

        apteka_id = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection is not None:
            cursor_call_count.close()
            connection.close()

    return apteka_id[0][0]


def main():
    apteks_list = get_apteka_id('Аптека №1')
    print(apteks_list)


if __name__ == '__main__':
    main()
