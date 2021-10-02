# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод
команды show dhcp snooping binding из разных файлов и записывает обработанные
данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

Первый столбец в csv файле имя коммутатора надо получить из имени файла,
остальные - из содержимого в файлах.

Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.

"""
import re
import csv


def write_dhcp_snooping_to_csv(filenames: list, output: str):
    regex = re.compile(r'^(?P<mac>(?:[0-9A-F]{2}:){5}[0-9A-F]{2}).*'
                       r'\b(?P<ip>(?:\d+\.){3}\d+).*'
                       r'\b(?P<vlan>\d+) *'
                       r'\b(?P<intf>\S+)$',
                       re.MULTILINE)
    header = ['switch', 'mac', 'ip', 'vlan', 'interface']
    output_list = list()
    output_list.append(header)
    for file in filenames:
        switch = re.match(r'^[^_]+', file).group()
        with open(file) as f:
            for match in regex.finditer(f.read()):
                tmp = [t for t in match.groups()]
                tmp.insert(0, switch)
                output_list.append(tmp)
    with open(output, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in output_list:
            writer.writerow(row)


if __name__ == '__main__':
    files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    write_dhcp_snooping_to_csv(files, 'out.csv')