#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
timenow = time.localtime(time.time())

year,month,day,hour,minute = timenow[0:5]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))

a = time.asctime()
b = time.ctime()

print(a)
print(b)