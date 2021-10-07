# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
import concurrent.futures as conc
import logging
from datetime import datetime
import time

logging.basicConfig(
    format='%(threadName)s %(name)s: %(message)s',
    level=logging.INFO
)


def ping_ip_addresses(ip_list, thread_max=3):
    reach = list()
    unreach = list()
    logging.info(f'function are starting on {datetime.now().time()}')
    with conc.ThreadPoolExecutor(max_workers=thread_max) as executor:
        result = executor.map(ping_ip_address, ip_list)
        for ip, code in zip(ip_list, result):
            if code == 0:
                reach.append(ip)
            else:
                unreach.append(ip)
    logging.info(f'function was finish on {datetime.now().time()}')
    return reach, unreach


def ping_ip_address(address):
    logging.info(f'"ping {address}" are starting on {datetime.now().time()}')
    result = subprocess.run(['ping', '-c', '3', address], stdout=subprocess.PIPE)
    logging.info(f'"ping {address}" was finish on {datetime.now().time()}')
    return result.returncode


if __name__ == '__main__':
    x = ping_ip_addresses(['8.8.8.8', '8.8.8.9', '192.168.50.1', '192.168.50.3', '192.168.1.1'], 3)
    print(x)


