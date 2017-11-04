#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ua2En.py
#
#  Програма транслітерації  Ua -> En
#  Copyright 2017 Lytvynenko Viktor <Viktor.S.Litvinenko@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from DictionsMods import *

def Ua2En(S, d):
    '''
    транслітерація параметра-рядка (S) згідно з параметром-словником (d)
    '''
    Rez=""
    for i in S:
        try:
            if i.isupper():
                Rez=Rez+d[i.lower()].upper()
            else:
                Rez=Rez+d[i.lower()]
        except:
            Rez=Rez+i
    return Rez


def main(args):
    inp=input("Введіть рядок для транлітерації: ")
    print(Ua2En(inp, USA_dic))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
