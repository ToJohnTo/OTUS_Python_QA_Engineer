class TestPassengers:

    def test_check_flight(self, connect, data):
        """
        Тест проверяет, присутствуют ли пассажиры на рейс 100500
        :param connect:
        :param data:
        :return:
        """
        res = connect.select_entity('passenger_info', "flight_num='100500'")
        ids = [i[0] for i in res]
        assert len(ids) != 0, 'Пассажиры на рейс 100500 отсутствуют в системе'

    def test_check_del_passenger(self, connect, data):
        """
        Тест проверяет, удалились ли пользователи на рейс 100500
        :param connect:
        :param data:
        :return:
        """
        connect.delete_rows('passenger_info', "flight_num='100500'")
        res = connect.select_entity('passenger_info', "flight_num='100500'")
        assert len(res) == 0, 'Пассажиры на рейс 100500 есть в системе'

    def test_update_user_data(self, connect, new_user):
        """
        Тест проверяет обновление данных пассажира
        :return:
        """
        flight_num = 1234545
        connect.update_entity('passenger_info', f'id={new_user}', {'flight_num': flight_num})
        res = connect.select_entity('passenger_info', f'id={new_user}')
        flight_num_updated = res[0][5]
        assert flight_num == flight_num_updated
