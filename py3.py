#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   py3.py
@Time    :   2020/08/31 00:07:05
@Author  :   STY_lcmg
@Version :   1.0
@Contact :   lcmg.sty@gmail.com
@Desc    :   None
'''

# here put the import lib
def send(self, data):
    if self.debug:
        print('Send:', end=' ')
        print(':'.join('%02x' % ord(c) for c in data))
    l0 = len(data.encode('utf-8')) & 0xFF
    l1 = (len(data.encode('utf-8')) >> 8) & 0xFF
    d = chr(l0) + chr(l1) + data
    self.sock.send(d)

def recv(self):
    data = self.sock.recv(2)
    l0 = ord(data[0])
    l1 = ord(data[1])
    plen = l0 + (l1 << 8)
    data = self.sock.recv(plen)
    if self.debug:
        print('Recv:', end=' ')
        print(':'.join('%02x' % ord(c) for c in data))
    return data