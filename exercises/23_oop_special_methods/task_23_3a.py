# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""

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


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def add_link(self, local, remote):
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

    def __add__(self, other):
        result = Topology({})
        result.topology = self.topology.copy()
        for key, value in other.topology.items():
            result.topology[key] = value
        return result

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.topology):
            key = list(self.topology.keys())[self.n]
            value = self.topology[key]
            self.n += 1
            return key, value
        else:
            raise StopIteration


t1 = Topology(topology_example)
for link in t1:
    print(link)
#pprint(t1.topology)
#pprint(t2.topology)
#pprint(t3.topology)
#pprint(t1.topology)