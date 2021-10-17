# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
import re

class IPAddress:
    def __init__(self, ip_mask):
        self.ip, self.mask = self._check_ip_mask(ip_mask)

    def _check_ip_mask(self, check):
        regex = re.compile(r'(\d+(\.\d+){3})/(\d+)')
        match_ip_mask = regex.fullmatch(check)
        if regex.fullmatch(check) is not None:
            for octet in match_ip_mask.group(1).split('.'):
                if not (0 <= int(octet) <= 255):
                    raise ValueError('Incorrect IPv4 address')
            if not (8 <= int(match_ip_mask.group(3)) <= 32):
                raise ValueError('Incorrect mask')
        else:
            raise ValueError('Incorrect IPv4 address')
        return match_ip_mask.group(1), int(match_ip_mask.group(3))

    def __str__(self):
        return f'IP address {self.ip}/{self.mask}'

    def __repr__(self):
        return f"{type(self).__name__}('{self.ip}/{self.mask}')"


#x = IPAddress('10.1.1.1/24')
#l = [x]
#print(x, str(x), l, sep='\n')