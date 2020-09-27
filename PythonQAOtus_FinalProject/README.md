# PythonQAOtus_FinalProject

#### Проектная работа
Тема: Автоматизация тестирования Web User Interface сайта hh.ru


hh.ru \
login: otus_final_project@mail.ru \
pass: Otus25082020


Запуск тестов: \
./cm selenoid start
./cm selenoid-ui start --port 8082
pytest --alluredir ./Allure_report/ ./Tests/TestsFinal.py


Генерация отчётов:
1. Аllure отчёт. В терминале: \
allure serve ./Allure-reports/
2. Selenoid-ui. В браузере: \
http://127.0.0.1:8082/ \
*Note:* Удаление видео из selenoid-ui. В терминале: \
cd /home/john/.aerokube/selenoid/video \
sudo rm -f ./*
