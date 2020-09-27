from sys import argv
from os import path
from time import sleep
from glob import glob
from collections import Counter
from json import dumps
import subprocess
import re
import logging


logging.basicConfig(format='%(levelname)s::%(filename)s::%(funcName)s::%(message)s', filename="output.log")
LOG_LEVEL = 10  # DEBUG


class Parser(object):
    """Парсер"""

    def __init__(self, path=None):
        # путь до log файла
        self.path = path
        # Логгер
        self.logger = logging.getLogger('parser')
        self.logger.setLevel(LOG_LEVEL)

    def by_path(self):
        """ Определяет по пути, что передано - каталог или файл """
        _path = self.path
        if path.isfile(_path):
            self.parsing_file(_path)
        elif path.isdir(_path):
            _path = glob(path.join(_path, "*.log"))
            self.find_log_in_directory(_path)
        else:
            print("You enter wrong path!!!")
            sleep(4)
            return 1

    def find_log_in_directory(self, dir_path):
        """ Ищет логи в каталоге по указанному пути """
        logs_list = dir_path
        self.logger.debug(" Файлы в каталоге:{}".format(logs_list))
        if len(logs_list) == 1:
            self.parsing_file(logs_list[0])
        else:
            self.parsing_file(logs_list[0])
            self.find_log_in_directory(dir_path[1:])

    def parsing_file(self, file):
        """ Парсит лог файл и записывает результаты в json файл"""
        print("Имя парсируемого файла: ", file)
        # Считали данные из log файла
        with open(file, "r") as lf:
            logfile = lf.read()
        ip_row = (subprocess.Popen("awk '{print $1}' %s" % file,
                                encoding='utf-8',
                                shell=True,
                                stdout=subprocess.PIPE).stdout).read()
        slow_rows = (subprocess.Popen("awk '{print $10 $6 $11 $1}' %s" % file,
                                encoding='utf-8',
                                shell=True,
                                stdout=subprocess.PIPE).stdout).readlines()
        time_row = (subprocess.Popen("awk '{print $10}' %s" % file,
                                encoding='utf-8',
                                shell=True,
                                stdout=subprocess.PIPE).stdout).readlines()
        cs_rows = (subprocess.Popen("awk '{print $9 $6 $11 $1}' %s" % file,
                                encoding='utf-8',
                                shell=True,
                                stdout=subprocess.PIPE).stdout).readlines()
        status_row = (subprocess.Popen("awk '{print $9}' %s" % file,
                                encoding='utf-8',
                                shell=True,
                                stdout=subprocess.PIPE).stdout).read()

        all_query = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', ip_row)
        get_query = re.findall(r'GET', logfile)
        post_query = re.findall(r'POST', logfile)
        top_ip = Counter(all_query)
        time_10 = sorted(time_row, key=int, reverse=True)[:10]
        client_errs = re.findall(r'[4][0-9][0-9]', status_row)[:10]
        server_errs = re.findall(r'[5][0-9][0-9]', status_row)[:10]
        print("Общее количество выполненных запросов: {}".format(len(all_query)))
        print("Количество запросов по типу: GET - {}".format(len(get_query)))
        print("Количество запросов по типу: POST - {}".format(len(post_query)))
        print("Топ 10 IP адресов, с которых были сделаны запросы: {}".format(top_ip.most_common(10)))
        print("Топ 10 самых долгих запросов (метод, url, ip, время запроса): ")
        slow_list = []
        for time in time_10:
            for line in slow_rows:
                if time.strip() in line:
                    print(line, end='\n')
                    slow_list += line.split()
                    break
        print("Топ 10 запросов, которые завершились клиентской ошибкой (статус код, метод, url, ip адрес): ")
        client_errs_list = []
        for status in client_errs:
            for cl in cs_rows:
                if status in cl:
                    print(cl, end='\n')
                    client_errs_list.append(cl)
                    break
        print("Топ 10 запросов, которые завершились ошибкой со стороны сервера (статус код, метод, url, ip адрес): ")
        server_errs_list = []
        for status in server_errs:
            for ser in cs_rows:
                if status in ser:
                    print(ser, end='\n')
                    server_errs_list.append(ser)
                    break

        library = []

        # Формируем словарь
        library = {'name': file,
                   'count_all_queries': len(all_query),
                   'get_query': len(get_query),
                   'post_query': len(post_query),
                   'top_ip': top_ip.most_common(10),
                   'slow_query': slow_list,
                   'top_client_errs': client_errs_list,
                   'top_server_errs': server_errs_list
                   }

        print(library)

        # Добавляем в новый json файл
        with open("./parsing_result.json", "w") as fw:
            s = dumps(library, indent=4)
            fw.write(s)


if __name__ == "__main__":
    logger = logging.getLogger('main')
    logger.setLevel(LOG_LEVEL)
    logger.debug(" Файлы в каталоге:{}".format(argv[1]))
    p = Parser(argv[1])
    p.by_path()
