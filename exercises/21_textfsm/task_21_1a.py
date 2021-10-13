# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""
import textfsm
import tabulate

def parse_output_to_dict(template, command_output):
    """Return list of dict.
    Dict key = Value names of template
    Dict value = values"""
    with open(template) as tf:
        fsm = textfsm.TextFSM(tf)
    parse = fsm.ParseText(command_output)
    result = []
    for out in parse:
        out_list = {}
        for key, value in zip(fsm.header, out):
            out_list[key] = value
        result.append(dict(zip(fsm.header, out)))
    return result


if __name__ == '__main__':
    with open('output/sh_ip_int_br.txt') as f:
        p = parse_output_to_dict('templates/sh_ip_int_br.template', f.read())
        print(p)

