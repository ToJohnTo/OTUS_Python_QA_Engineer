# PythonQAOtus_Lesson8

## Подготовительные процедуры
1. Установить docker.
2. Установить docker-compose.
3. Прописать команду:
```
sudo usermod -aG docker $USER 
```
4. Скачать .yml файл opencart'a:
```
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-opencart/master/docker-compose.yml > docker-compose.yml 
```
5. Выдать файлу права на исполнение:
```
sudo chmod +x docker-compose.yml 
```
6. Запустить докер контейнер с opencart'ом в фоновом режиме:
```
docker-compose up -d 
```



## Пример установки webriver'a для firefox:
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-linux64.tar.gz
tar -xvzf geckodriver-v0.15.0-linux64.tar.gz
sudo chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
```


### Рабочая команда запуска теста:
```
pytest test_example.py --browser=chrome --default_url=http://localhost/index.php?route=common/home 
```