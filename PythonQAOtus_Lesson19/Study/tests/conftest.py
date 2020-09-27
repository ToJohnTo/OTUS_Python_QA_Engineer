import csv

from pytest import fixture

from DataBase.postgesql.client import PostgresClient


@fixture(scope='session', name='connect')
def create_connect():
    conn = PostgresClient()
    return conn


@fixture(scope='function', name='data')
def create_data(connect):
    new = []
    with open('data.csv', 'r') as file:
        raws = csv.reader(file, delimiter=' ')
        for item in raws:
            new.append(tuple(item[0].split(',')))

    columns = ','.join(['name', 'surname', 'phone', 'flight_num'])
    connect.insert_many_rows('passenger_info', columns, new)


@fixture(scope='function', name='new_user')
def add_user(connect):
    entity_dct = {
        'name': 'Петр',
        'surname': 'Иванов',
        'phone': '890453564738',
        'flight_num': 11111
    }
    id_ = connect.insert_entity('passenger_info', entity_dct)[0]
    yield id_
    connect.delete_rows('passenger_info', f'id={id_}')
