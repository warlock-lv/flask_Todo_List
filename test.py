# !/usr/bin/env python
# coding:    utf-8
# ----------------------------------------------
# Author:    warlock
# Email:     457880341@qq.com
# Time:      2017-10-22 20:44
# Software:  PyCharm Pro Edition 4.5
# Description:   
# ----------------------------------------------

from flask_mongoengine import MongoEngine

import datetime

aa = datetime.datetime.now()
aa = aa.strftime('%Y-%m-%d %H:%M:%S.%f')

print(aa)
print(type(aa))



#'%Y-%m-%d %H:%M:%S %f'

#print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


if __name__ == '__main__':
    pass
