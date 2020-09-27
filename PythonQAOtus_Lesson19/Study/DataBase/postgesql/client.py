import psycopg2


class PostgresClient:

    def __init__(self):
        self.connect = psycopg2.connect(
            host='localhost',
            database='test_postgres',
            port=5432,
            user='test_postgres',
            password='test_postgres'
        )

    def execute_query(self, query: str):
        """
        Выполняет входящий запрос
        :param query:
        :return:
        """
        cursor = self.connect.cursor()
        return cursor.execute(query)

    def insert_entity(self, table_name: str, data: dict):
        """
        Выполнение запроса добавления данных
        :param data:
        :param table_name:
        :return:
        """
        cursor = self.connect.cursor()
        columns = ','.join(list(data.keys()))

        new = []
        for item in list(data.values()):
            if isinstance(item, int):
                new.append(f'{item}')
            if isinstance(item, str):
                value = item.replace("'", "''") if "'" in item else item
                new.append(f"'{value}'")
        new = ','.join(new)
        insert_str = f'INSERT INTO {table_name} ({columns}) VALUES ' \
                     f'({new}) RETURNING *'
        cursor.execute(insert_str)

        self.connect.commit()
        return cursor.fetchall()[0]

    def insert_many_rows(self, table_name: str, columns: str, data):
        cursor = self.connect.cursor()

        insert_str = f'INSERT INTO {table_name} ({columns}) VALUES (%s,%s,%s,%s)'
        cursor.executemany(insert_str, data)

        self.connect.commit()
        return self.connect.commit()

    def select_entity(self, table_name: str, condition: str):
        """
        :param table_name:
        :param condition:
        """
        cursor = self.connect.cursor()

        select_str = f'SELECT * FROM {table_name} WHERE {condition}'
        cursor.execute(select_str)
        return cursor.fetchall()

    def delete_rows(self, table_name: str, condition: str = None):
        cursor = self.connect.cursor()
        if condition:
            del_str = f'DELETE FROM {table_name} WHERE {condition}'
        else:
            del_str = f'DELETE FROM {table_name}'
        cursor.execute(del_str)

        self.connect.commit()
        return self.connect.commit()

    def update_entity(self, table_name: str, condition: str, data: dict):
        cursor = self.connect.cursor()

        new = []
        for key, val in data.items():
            if isinstance(val, str):
                value = val.replace("'", "''") if "'" in val else val
                new.append(f"{key}='{value}'")
            else:
                new.append(f'{key}={val}')
        query = ','.join(new)

        upd_query = f'UPDATE {table_name} SET {query}  WHERE {condition}'
        cursor.execute(upd_query)

        self.connect.commit()
        return self.connect.commit()
