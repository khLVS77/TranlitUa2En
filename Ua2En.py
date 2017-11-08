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

from DictionsMods import *
from tkinter import *
import sys

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.LName=Label(self, text="Транслітерація тексту...")
        self.LName.grid(row=0, column=0, columnspan=9)
        
        self.LVersion=Label(self, text="Версія 1.0")
        self.LVersion.grid(row=1, column=0, columnspan=9)
        
        self.LUa=Label(self, text="Український текст:")
        self.LUa.grid(row=2, column=1)
        
        self.UaTxt=Text(self, width=25, height=10, wrap=WORD)
        self.UaTxt.grid(row=3, column=1)
        
        self.BTrans=Button(self, text="-->\nПерекласти...", command=self.Ua2En, cursor="hand2")
        self.BTrans.grid(row=3, column=2)
        
        self.LUa=Label(self, text="Транслітерований текст:")
        self.LUa.grid(row=2, column=4)
        
        self.EnTxt=Text(self, width=25, height=10, wrap=WORD)
        self.EnTxt.grid(row=3, column=4)
        
        self.BExit=Button(self, text="Вихід", command=quit, cursor="hand2")
        self.BExit.grid(column=1)
        
    def quit(self):
        sys.exit()


    def Ua2En(self):
        '''
        транслітерація параметра-рядка (S) згідно з параметром-словником (d)
        '''
        S=self.UaTxt.get(0.0, END)
        #print(S)
        d=USA_dic
        Rez=""
        for i in S:
            try:
                if i.isupper():
                    Rez=Rez+d[i.lower()].upper()
                else:
                    Rez=Rez+d[i.lower()]
            except:
                Rez=Rez+i
        self.EnTxt.delete(0.0,END)
        self.EnTxt.insert(0.0,Rez)


root=Tk()
root.title("Транслітератор Ua2En")
root.geometry("480x250")
app=Application(root)
root.mainloop()
