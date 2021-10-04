# -*- coding: utf-8 -*-
"""
Задание 18.2c

Скопировать функцию send_config_commands из задания 18.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка, спросить пользователя надо ли выполнять
остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию,
  поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

"""
from pprint import pprint
import yaml
import re
from netmiko import ConnectHandler


# списки команд с ошибками и без:
commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands

out = 'config term\n'\
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'\
       'R1(config)#a\n'\
       '% Ambiguous command:  "a"\n'\
       'R1(config)#'


def send_config_commands(device, config_commands, log=True):
    good = dict()
    bad = dict()
    errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']

    if log:
        print(f"Connecting to {device['host']}...")
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        ssh.conn_timeout = 10
        error_check = False
        for command in config_commands:
            out = ssh.send_config_set(command)
            for error in errors:
                if out.find(error) > 0:
                    bad[command] = out
                    reg_error = f'({error}.*)\\n'
                    full_error = re.search(r'{}'.format(reg_error), out).group(1)
                    print(f'Command "{command}" was completed with error "{full_error}" on device {device["host"]}')
                    error_check = True
                    break
            if error_check:
                if input('Continue to process commands? [y]/n:') in ['no', 'n']:
                    break
            else:
                good[command] = out


    return good, bad


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        result = send_config_commands(dev, commands)
        good_r, bad_r = result
        pprint(good_r, width=120)
        pprint(bad_r, width=120)

