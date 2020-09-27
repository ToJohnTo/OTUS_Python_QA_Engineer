import subprocess
import os


with open("output.txt", "w") as file:
    file.write("1. Список всех процессов: \n")
    output = subprocess.check_output(['ps', '-ef'])
    file.write(output.decode("utf-8"))
    print("Задание 1 выполнено! Результат записан в файл output.txt")

    file.write("\n\n2. Информацию о конкретном процессе (по pid текущего скрипта): \n")
    current_pid = os.getpid()
    output = subprocess.check_output(f'ps --pid {current_pid}', shell=True)
    file.write(output.decode("utf-8"))
    print("Задание 2 выполнено! Результат записан в файл output.txt")

    file.write("\n\n3. Список в файлов в директории (указать директорию): \n")
    input_path = input("Укажите директорию:")
    file.write(f'Путь к директории: {input_path}\n')
    file.write(f'Список файлов:\n')
    for el in os.listdir(input_path):
        file.writelines(el + "\n")
    print("Задание 3 выполнено! Результат записан в файл output.txt")

    file.write("\n\n4. Текущую директорию и список в файлов в ней: \n")
    file.write(f'Путь к директории: {os.getcwd()}\n')
    file.write(f'Список файлов:\n')
    for el in os.listdir(os.getcwd()):
        file.writelines(el + "\n")
    print("Задание 4 выполнено! Результат записан в файл output.txt")

    file.write("\n\n5. Версию ядра: \n")
    output = subprocess.check_output('uname -r', shell=True)
    file.write(output.decode("utf-8"))
    print("Задание 5 выполнено! Результат записан в файл output.txt")

    file.write("\n\n6. Версию операционной системы: \n")
    output = subprocess.check_output('lsb_release -a', shell=True)
    file.write(output.decode("utf-8"))
    print("Задание 6 выполнено! Результат записан в файл output.txt")
