# -*- coding: utf-8 -*-
'''
Задание 4.1

Обработать строку NAT таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

Ограничение: Все задания надо выполнять используя только пройденные темы.


NAT = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

NAT = NAT.replace('FastEthernet', 'GigabitEthernet')
lng = len(NAT)

print('#'*lng,'\n' + NAT,'\n' + '#'*lng)
'''

#vlan, mac, intf = ['100', '000.000.000', 'FastEthernet0/24']
#oct1, oct2, oct3, oct4 = (192, 168, 0, 1)
ip_list = ['192.168.0.1/24', '172.16.0.1/12', '10.0.0.1/8']

for ip_addr in ip_list:
    ip, mask = ip_addr.split('/')
    print(f"IP: {ip} mask: {mask}")
