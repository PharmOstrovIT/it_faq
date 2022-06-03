import psycopg2
from credentials import *


def get_data_apteka():
    sql_request = (f"""
                SELECT * FROM apteka
                ORDER BY id ASC 
    """)

    try:
        connection = psycopg2.connect(database=database,
                                      user=username,
                                      password=password,
                                      host=host,
                                      port=port
                                      )

        cursor_call_count = connection.cursor()
        cursor_call_count.execute(str(sql_request))

        apteks = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor_call_count.close()
            connection.close()

    return apteks


def main():
    apteks_list = get_data_apteka()
    print(apteks_list)


if __name__ == '__main__':
    main()
