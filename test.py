import psycopg2
from credentials import username as username_db, password as password_db, database, host, port


def get_data_equipment(apteka_id):
    sql_request = (f"""
            SELECT equipment_type, equipment_model, serial_number, invoice_number, invoice_date, purchase_org, comments
            FROM main_equipment 
            WHERE apteka_id = '{apteka_id}' 
            ORDER BY id ASC
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

        equipment_list = cursor_call_count.fetchall()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:
        if connection:
            cursor_call_count.close()
            connection.close()

    return equipment_list


def main():
    apteks_list = get_data_equipment(1)
    print(apteks_list)


if __name__ == '__main__':
    main()
