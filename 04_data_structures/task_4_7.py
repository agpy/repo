# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.split(':')
for i in range(len(MAC)):
   MAC[i] = bin(int(MAC[i],16))

MAC = ''.join(MAC)

print(MAC)










