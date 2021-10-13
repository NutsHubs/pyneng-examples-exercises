# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
import textfsm
from textfsm import clitable

def parse_command_dynamic(command_output,
                          attributes_dict,
                          index_file='index',
                          templ_path='templates'):
    """Return list of dict as result of task_21.1a"""
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    result = []
    for values in cli_table:
        if not(cli_table[0] in values):
            result.append(dict(zip(cli_table[0], values)))
    return result


if __name__ == '__main__':
    attr = {'Command':'show ip int br', 'Vendor':'cisco_ios'}
    with open('output/sh_ip_int_br.txt') as f:
        print(parse_command_dynamic(f.read(), attr))