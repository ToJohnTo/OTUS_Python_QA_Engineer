# PythonQAOtus_Lesson30

Расширенное использование RobotFramework и расширение библиотек RobotFramework на Python \
Цель: 
1. Научиться использовать дополнительные библиотеки для RobotFramework \
1.1. Подключить к тестам библиотеку DatabaseLibrary \
1.2. Написать тест-кейс в RobotFramework на редактирование нового товара в администраторской панели OpenCart \
1.3. Сделать в этом же тесте проверку что нужные атрибуты изменились

2. Научиться писать собственные модули для RobotFramework на Python \
2.1.Создать тестсьюит на RobotFramework по тестированию логина (в админку и в клиентское приложение) \
2.2. Написать тест для логина в админку \
2.3. Для теста логина клиента (Клиент логинится в интерфейсе OpenCart) \
Критерии оценки: Реализованы тесты с использованием фреймворка Robot Framework


Ход работы:
1. Скачать докер опенкарта: \
$ docker pull bitnami/opencart \
$ curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml \
2. Пробросить порт 3306 наружу. Для этого в файле docker-compose.yml дописать строку "ports: - '3306:3306'" в блоке "mariadb" \
3. Поднять контейнер: \
$ docker-compose up -d \
4. Запустить тесты:
$ robot -L DEBUG -d Results/ Tests/Example_BDT_2.robot

