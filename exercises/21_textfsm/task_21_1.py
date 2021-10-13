# -*- coding: utf-8 -*-
"""
Задание 21.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды sh ip int br с оборудования
и шаблоне templates/sh_ip_int_br.template.

"""
from netmiko import ConnectHandler
import textfsm
from textfsm import clitable
from tabulate import tabulate


def parse_command_output(template, command_output):
    """Return list() = [[headers], [processed_out], ..]"""
    with open(template) as ft:
        fsm = textfsm.TextFSM(ft)
    cli_table = clitable.CliTable('index', 'templates')
    processed_output = fsm.ParseText(command_output)
    return [fsm.header] + processed_output

# вызов функции должен выглядеть так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    '''with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    '''
    with open('output/sh_ip_int_br.txt') as f:
        result = parse_command_output("templates/sh_ip_int_br.template", f.read())
        print(tabulate(result))
