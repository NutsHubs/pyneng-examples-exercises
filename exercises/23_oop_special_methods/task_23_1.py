# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

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

#x = IPAddress('10.1.1.1/24')
#print(x.ip, x.mask)