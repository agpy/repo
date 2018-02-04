# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_names = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']

ospf_route = ospf_route.replace('O', 'OSPF').replace('via','').split()
for out_ospf in range(len(ospf_route)):
    ospf_route[out_ospf] = (ospf_route[out_ospf]).strip('[],')
    print('{:23} {}'.format(ospf_names[out_ospf],ospf_route[out_ospf]))
    

            
