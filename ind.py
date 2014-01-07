#!/usr/bin/python
#-*-coding:utf-8-*-

import pynotify
import os
pynotify.init('PySozluk-V1.0')
file = open("kelime.txt","r")

for kel in file:
	bir = kel.split("=")[0]
	iki = kel.split("=")[1]
	n = pynotify.Notification('%s'%bir,'%s'%iki)
	n.set_timeout(0)
	n.show()
	os.system("sleep 5")
