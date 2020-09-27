# PythonQAOtus_Lesson16

Запускаем selenoid \
Цель: Научиться самостоятельно поднимать селеноид и прогонять тесты в нём. \
Для выполнения домашнего задания нужно: 
1. поднять селеноид, запустить в нём прогон тестового проекта.
2. добавить несколько версий других доступных браузеров.

Notes:
1. Сначала необходимо установить docker
a. https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
2. https://github.com/aerokube/cm
a. ./cm selenoid start
b. ./cm selenoid stop
c. ./cm selenoid status
d. .aerokube
3. Проверить что там {HOST}:4444/status {HOST}:4444/ping
4. Передаем для удаленного запуска {HOST}/4444/wd/hub
5. Запускаем selenoid-ui {HOST}:8080
a. ./cm selenoid-ui start
6. Записываем видео “enableVideo”: True + selenoid/video-recorder
7. Сохраняем логи сессий “enableLog”: True
8. Включаем vnc через “enableVnc”: True
9. Добавляем браузер
a. docker pull {REQUIRED_BROWSER}
b. добавляем браузер в конфиг
c. https://aerokube.com/selenoid/latest/#_updating_browsers:
./cm selenoid stop \
./cm selenoid start \
10. Добавляем нод --vnc --args "-limit=10"

В качестве ответа приложить скриншот работающего селеноида и бегущих в нем тестов с vnc, вкладки с доступными новыми браузерами.
