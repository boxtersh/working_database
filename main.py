import pymysql
import connecting_database as conn_BD
from connecting_database import dict_query as dt
from connecting_database import creating_tables as table


host, user, password, database = conn_BD.connecting_database()
connection = False
try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    requests = table()

    with connection.cursor() as cursor:
        for request in requests:
            if request:
                cursor.execute(request)
        connection.commit()


except pymysql.MySQLError as text:
    print(f'Ошибка: {text}')

# finally:
#     if connection:
#         connection.close()
# if result is None:
#     print(f'Ошибка соединения')
#
# elif result:
#     for tuple_ in result:
#         print(tuple_)
# else:
#     print(f'Нет данных')

# try:
#     # Подключение к базе данных
#     connection = pymysql.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )
#
#     with connection.cursor() as cursor:
#         # # Создание новой записи
#         # sql = "INSERT INTO Authors (Name, Age, City, Price) VALUES (%s, %s, %s, %s)"
#         # cursor.execute(sql, ('Иван', 25, 'Волжский', 313))
#         # connection.commit()  # Сохранение изменений
#
#         # Получение данных
#         sql = f"{dt['Название животного на Л']}"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#
#
# except pymysql.MySQLError as text:
#     result = None
#     print(f'Ошибка: {text}')