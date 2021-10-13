# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


"""
from pprint import pprint


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def add_link(self, local, remote):
        is_exists = False
        if local in self.topology:
            if self.topology[local] == remote:
                print('Такое соединение существует')
                return
            print('Cоединение с одним из портов существует')
            return
        self.topology[local] = remote


    def delete_link(self, local, remote):
        key = local
        if not(local in self.topology):
            if not(remote in self.topology):
                print('Такого соединения нет')
                return
            else:
                key = remote
        self.topology.pop(key)

    def delete_node(self, node):
        is_exists = False
        for key in list(self.topology):
            node_delete = key
            if not(node in list(key)):
                if not(node in list(self.topology[key])):
                    continue
            is_exists = True
            self.topology.pop(node_delete)
        if not is_exists:
            print('Такого устройства нет')

    def _normalize(self, topology_dict):
        topology_result = topology_dict
        for key in list(topology_dict.keys()):
            if key in topology_dict.values():
                if topology_dict[topology_dict[key]] == key:
                    topology_result.pop(key)
        return topology_result


topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

t = Topology(topology_example)
pprint(t.topology)
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
pprint(t.topology)
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))